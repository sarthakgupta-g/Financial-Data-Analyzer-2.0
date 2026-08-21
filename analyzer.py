import pandas as pd

data=pd.read_csv("stock_data.csv")
print(data.tail(5))
print(data.columns)
print(data.info())
print(data.shape)

print(data["Price"].median())
print(data["Price"].max()-data["Price"].min())
first_p=data["Price"].iloc[0]
last_p=data["Price"].iloc[-1]
print(first_p)
print(last_p)
print((last_p-first_p)/first_p * 100)

low_v=data["Volume"].min()
print(data[data["Volume"]==low_v]["Date"].iloc[0])
high_v=data["Volume"].max()
print(high_v - low_v)
