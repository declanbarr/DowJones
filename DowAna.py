# Declan Barr 18 July 2018
# Script to analyse Dow Jones Index Data Set from the UCI Machine Learning Repository

import pandas as pd 

pd.options.display.max_rows = 999 # Set max rows to 999 to ensure all rows are displayed (from https://pandas.pydata.org/pandas-docs/stable/options.html)
pd.options.display.max_columns = 100 # Set max columns to 100 to ensure all data is shown for describe() function (from https://pandas.pydata.org/pandas-docs/stable/options.html)

df = pd.read_csv('dow_jones_index.data', converters={'open': lambda s: float(s.replace('$', '')), 'close': lambda s: float(s.replace('$', '')), 'high': lambda s: float(s.replace('$', '')), 'low': lambda s: float(s.replace('$', ''))}) # From https://stackoverflow.com/questions/36320317/pandas-read-csv-ignore-dollar-sign-when-parsing-numbers
#print(df.head(10))
for x in range(3,7):
    print(df.iloc[:, [x]].describe())
