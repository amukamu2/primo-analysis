import pandas as pd
import numpy as np

# 1. take 1M and duplicate it 9 times -> 9M
# 2. randomize 9M
# 3. combine 9M with 1M -> 10M

df = pd.read_csv('data/large_order_data_2024.csv')

dup_df = [df.copy()]*9

nineM_df = pd.concat(dup_df, axis=0)

nineM_df["order_no"] = "ORD" + np.random.randint(100000, 433333, size=len(nineM_df)).astype(str)

nineM_df["amount"] = (nineM_df["amount"] * (np.random.uniform(0.5, 1.5, size=len(nineM_df)))).round().astype(int)   

np1 = pd.Series(np.random.randint(1, 10000, size=len(nineM_df)).astype(str)).str.zfill(4)

nineM_df["customer_no"] = "CUST" + np1

nineM_df["branch"] = np.random.choice(df["branch"].unique(), size=len(nineM_df))

nineM_df["brand"] = np.random.choice(df["brand"].unique(), size=len(nineM_df))

p1 = df["sku"].str.split("-").str[0].unique()
p2 = df["sku"].str.split("-").str[1].unique()
p3 = pd.Series(np.random.randint(1, 51, size=len(nineM_df)).astype(str)).str.zfill(2)

nineM_df["sku"] = np.random.choice(p1, size=len(nineM_df)) + "-" + np.random.choice(p2, size=len(nineM_df)) + "-" + p3

nineM_df["quantity"] = np.random.randint(1, 6, size=len(nineM_df))

random_dates = np.random.choice(pd.date_range(start='2024-01-01', end='2024-12-31'), size=len(nineM_df))
random_times = pd.to_timedelta(np.random.randint(0, 86400, size=len(nineM_df)), unit='s')

nineM_df["transaction_datetime"] = pd.to_datetime(random_dates + random_times)

tenM_df = pd.concat([df, nineM_df], axis=0)

tenM_df.to_csv('result/10m_records.csv', index=False)

