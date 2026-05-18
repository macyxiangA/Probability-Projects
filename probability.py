import string
import sys
import math
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def get_parameter_vectors():
    '''
    This function parses e.txt and s.txt to get the  26-dimensional multinomial
    parameter vector (characters probabilities of English and Spanish) as
    descibed in section 1.2 of the writeup

    Returns: tuple of vectors e and s
    '''
    #Implementing vectors e,s as lists (arrays) of length 26
    #with p[0] being the probability of 'A' and so on
    e=[0]*26
    s=[0]*26

    with open(BASE_DIR / 'e.txt',encoding='utf-8') as f:
        for line in f:
            #strip: removes the newline character
            #split: split the string on space character
            char,prob=line.strip().split(" ")
            #ord('E') gives the ASCII (integer) value of character 'E'
            #we then subtract it from 'A' to give array index
            #This way 'A' gets index 0 and 'Z' gets index 25.
            e[ord(char)-ord('A')]=float(prob)
    with open(BASE_DIR / 's.txt',encoding='utf-8') as f:
        for line in f:
            char,prob=line.strip().split(" ")
            s[ord(char)-ord('A')]=float(prob)
    return (e,s)
    
def shred(filename):
    '''
    This function parses a .txt file into a dict of character counts, where
    the input file may contain any printable ASCII characters and can be short 
    (e.g. a single word) or long (e.g. an article). Ignores case, i.e. merges 
    'A' and 'a' counts together, and so on (this is known as case-folding). 
    Only counts characters A to Z (after case-folding), ignoring all other 
    characters such as space, punctuations, etc.

    Sample Input/Output functionality:
    Input: "Hi! I'll go :-)"
    Output: {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0,
             'G': 1, 'H': 1, 'I': 2, 'J': 0, 'K': 0, 'L': 2,
             'M': 0, 'N': 0, 'O': 1, 'P': 0, 'Q': 0, 'R': 0,
             'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0,
             'Y': 0, 'Z': 0}

    Returns: dict of character counts
    '''

    boc=dict()
    with open (filename,encoding='utf-8') as f:
        corpus=f.read()
    #convert all lowercase alphabets to uppercase
    corpus=corpus.upper()
    #initialize X
    for a in string.ascii_uppercase:
        boc[a]=0
    for c in corpus:
        if c in string.ascii_uppercase:
            boc[c]+=1
    return boc


if __name__ == "__main__":
    if len(sys.argv) not in (2, 4):
        print("Usage: python3 probability.py <letter-file> [english-prior spanish-prior]")
        sys.exit(1)

    letterPath = sys.argv[1]
    if len(sys.argv) >= 4:
        eng = float(sys.argv[2])
        spar = float(sys.argv[3])
    else:
        eng = 0.6
        spar = 0.4
    if eng <= 0 or spar <= 0:
        print("Error: priors must be positive.")
        sys.exit(1)

    #step 1
    e, s = get_parameter_vectors()
    boc = shred(letterPath)

    XA = boc.get('A')
    loge1 = XA * math.log(e[0])
    logs1 = XA * math.log(s[0]) 
    print("Compute X1 log e1 and X1 log s1")
    print("{:.4f}".format(loge1))
    print("{:.4f}".format(logs1))

    #step 2
    FE = math.log(eng)
    FS = math.log(spar)
    for i in range(26):
        Xi = boc[chr(ord('A') + i)]
        FE += Xi * math.log(e[i])
        FS += Xi * math.log(s[i])

    print("Compute F (English) and F (Spanish)")
    print(f"{FE:.4f}")
    print(f"{FS:.4f}")

    #step 3
    delta = FS - FE

    if delta >= 100:
        p_eng = 0.0
    elif delta <= -100:
        p_eng = 1.0
    else:
        p_eng = 1.0 / (1.0 + math.exp(delta))

    print("Compute P (Y = English | X)")
    print(f"{p_eng:.4f}")




