import pandas as pd
import numpy as np
df = pd.read_csv(
    r"C:/Users/prasa/.spyder-py3/Sample - Superstore.csv",
    encoding='latin1'
)
df.head()
df.info()
df.isnull().sum()
df.duplicated().sum()
df.dtypes
df.describe()
df = df.drop_duplicates()
df = df.dropna()
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['Category'] = df['Category'].str.upper()
Q1 = df['Sales'].quantile(0.25)
Q3 = df['Sales'].quantile(0.75)

IQR = Q3 - Q1

outliers = df[
    (df['Sales'] < (Q1 - 1.5 * IQR)) |
    (df['Sales'] > (Q3 + 1.5 * IQR))
]

print(outliers)
df.to_csv("cleaned_superstore.csv", index=False)
