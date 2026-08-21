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

data["Daily_Return"]=data["Price"].pct_change() * 100

print(data["Daily_Return"].mean())
print(data["Daily_Return"].min())
print(data["Daily_Return"].max())

avg_p=data["Price"].mean()
avg_p_dates=data[data["Price"]>avg_p]["Date"]
print(avg_p_dates)
print(avg_p_dates.shape[0])
dates_v=data[data["Volume"]>80000000]["Date"]
print(dates_v)
print(dates_v.shape[0])

