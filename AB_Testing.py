# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 20:39:17 2022

@author: anous
"""


# Import libraries
import codecademylib3
import pandas as pd
import numpy as np

# Read in the `clicks.csv` file as `abdata`
abdata = pd.read_csv('clicks.csv')
#1
abdata.head()
#2
Xtab = pd.crosstab(abdata.group, abdata.is_purchase)
print(Xtab)
#3
from scipy.stats import chi2_contingency
chi2, pval, dof, expected = chi2_contingency(Xtab)
print(pval)
is_significant = True
#4
num_visits = len(abdata)
print("no. of visitors: ", num_visits)
#5
num_sales_needed_099 = np.ceil(1000/0.99)
print(num_sales_needed_099)
#6
p_sales_needed_099 = num_sales_needed_099 / num_visits
print(p_sales_needed_099)
#7
num_sales_needed_199 = 1000/1.99
p_sales_needed_199 = num_sales_needed_199/num_visits
print(p_sales_needed_199)
num_sales_needed_499 = 1000/4.99
p_sales_needed_499 = num_sales_needed_499/num_visits
print(p_sales_needed_499)
#8
samp_size_099 = np.sum(abdata.group == 'A')
sales_099 = np.sum((abdata.group == 'A') & (abdata.is_purchase == 'Yes'))
#9
samp_size_199 = np.sum(abdata.group == 'B')
sales_199 = np.sum((abdata.group == 'B') & (abdata.is_purchase == 'Yes'))
print(samp_size_199)
print(sales_199)
samp_size_499 = np.sum(abdata.group == 'C')
sales_499 = np.sum((abdata.group == 'C') & (abdata.is_purchase == 'Yes'))
print(samp_size_499)
print(sales_499)
#10
from scipy.stats import binom_test
pvalueA = binom_test(sales_099, n=samp_size_099, p=p_sales_needed_099, alternative='greater')
print(pvalueA)
#11
pvalueB = binom_test(sales_199, n=samp_size_199, p=p_sales_needed_199, alternative='greater')
print(pvalueB)
#12
pvalueC = binom_test(sales_499, n=samp_size_499, p=p_sales_needed_499, alternative='greater')
print(pvalueC)