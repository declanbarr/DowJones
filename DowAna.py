# Declan Barr 18 July 2018
# Script to analyse Dow Jones Index Data Set from the UCI Machine Learning Repository

import pandas as pd 

pd.options.display.max_rows = 20000 # Set max rows to 999 to ensure all rows are displayed (from https://pandas.pydata.org/pandas-docs/stable/options.html)
pd.options.display.max_columns = 100 # Set max columns to 100 to ensure all data is shown for describe() function (from https://pandas.pydata.org/pandas-docs/stable/options.html)

df = pd.read_csv('dow_jones_index.data')
print(df)


