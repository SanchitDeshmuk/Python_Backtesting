import pandas as pd
import pandas_ta as ta

data = pd.read_csv("data.csv")
data['date'] = pd.to_datetime(data['date'])  
data.set_index('date', inplace=True)
print(data)

data["EMA8"] = ta.ema(data.close, length=8)
data["EMA21"] = ta.ema(data.close, length=21)

print(data)