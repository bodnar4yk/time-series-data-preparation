import numpy as np
import pandas as pd

df=pd.read_csv('pay_demo.csv')
df = df.dropna(subset=['Date']) #delete NA in Date 1 row

print(df.describe())

df['Pay_Type_1'] = df['Pay_Type_1'].fillna(0) #filled NA as 0
df['Pay_Type_2'] = df['Pay_Type_2'].fillna(0) #filled NA as 0

print(df.describe())

#create new columns
def add_colunms(df):
    df_copy = df.copy()
    df_copy['Total_Payment']=df_copy['Pay_Type_1']+df_copy['Pay_Type_2']
    return df_copy    

df = add_colunms(df)


#date make index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
df.sort_index(inplace=True)


# Used group_keys=False, that groupby dont dublicate key in index
df_month = df.groupby(['Class', 'Test'], group_keys=False).resample('ME').agg({
    'Pay_Type_1': 'sum',
    'Pay_Type_2': 'sum',
    'Total_Payment':'sum'
}).reset_index()


df_month = df_month.drop(columns=['Date'])

print(df_month.describe())
# print(df_month.median(numeric_only=True))


#convert to log value because too widly data
df_month['Pay_Type_1'] = np.log1p(df_month['Pay_Type_1'])
df_month['Pay_Type_2'] = np.log1p(df_month['Pay_Type_2'])
df_month['Total_Payment'] = np.log1p(df_month['Total_Payment'])

print(df_month.describe())

df_month.to_csv('sample.csv')
