from ast import Return
import numpy as np
import pandas as pd


#variables
dataFile = 'GC1_Price_Data.csv'
short_window = 50
long_window = 250

df = pd.read_csv(f'first-trading-system/data/{dataFile}', parse_dates=True, index_col='Date')

df['MA50'] = df['PX']
print(df)