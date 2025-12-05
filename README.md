# Probability Project

This project implements a Bayesian text classifier that estimates whether a given text is more likely written in English or Spanish, based on character frequency distributions and multinomial probability models.

## Overview

The classifier uses:
- Case-folding (ignoring letter case)
- Bag-of-characters counts (A–Z)
- Log-probability calculations to avoid numerical underflow
- Bayesian inference to compute the posterior probability

## Key Steps

1. Load probability vectors for English and Spanish
2. Count characters in the input file
3. Compute log-likelihoods for both languages
4. Apply Bayes’ rule using a logistic function
5. Output the predicted probability

## How to Run

Run with default priors (0.6 English, 0.4 Spanish):

python3 probability.py letter0.txt

Run with custom priors:

python3 probability.py letter0.txt 0.5 0.5

## Files

- probability.py — main script
- e.txt — English character probability vector
- s.txt — Spanish character probability vector
- letter*.txt — sample input files
- letter*_out.txt — generated output files

## Techniques Used

- Multinomial probability modeling
- Log-sum calculations
- Bag-of-characters feature extraction
- Bayesian classification logic
- Python-based text processing

## Author

Macy Xiang  
GitHub: https://github.com/macyxiangA
