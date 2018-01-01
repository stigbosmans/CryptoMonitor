import pandas as pd
import matplotlib.pyplot as plt

def get_ema(current_price, last_ema=-1, number_of_days=26):
    if last_ema == -1:
        return current_price
    N = number_of_days
    k = 2/(N+1)
    ema = (current_price * k) + (last_ema * (1-k))
    return ema

iota_prices = pd.read_csv('data/iota_price.csv')
close_prices = iota_prices["Close"].tolist()
print(iota_prices)
ema_26 = []
ema_12 = []
for i in range(0, len(close_prices) - 1):
    last_price = 0
    if i == 0:
        ema_26.append(close_prices[i])
        ema_12.append(close_prices[i])
    else:
        ema_26.append(get_ema(close_prices[i], ema_26[i-1], 26))
        ema_12.append(get_ema(close_prices[i], ema_26[i - 1], 12))

plt.plot(close_prices)
plt.plot(ema_26)
plt.plot(ema_12)
plt.show()
