import pandas as pd
import numpy as np

df = pd.read_csv('data/large_order_data_2024.csv')

# find top 10 spenders of each month

m = pd.to_datetime(df["transaction_datetime"]).dt.month

new_df = pd.DataFrame()

for i in range(1, 13):
    temp = df[m == i]
    result = temp.groupby("customer_no")["amount"].sum().reset_index()
    result = result.sort_values(by="amount", ascending=False).head(10).reset_index(drop=True)
    result.index += 1
    result.index.name = "Top 10"
    result = result.reset_index()
    result.insert(0, "Month", i)
    new_df = pd.concat([new_df, result], axis=0)

new_df.to_csv('result/top_10_spenders.csv', index=False)