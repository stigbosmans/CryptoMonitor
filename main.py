import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def get_ema(current_price, last_ema=-1, number_of_days=26):
    if last_ema == -1:
        return current_price
    N = number_of_days
    k = 2/(N+1)
    ema = ((current_price - last_ema) * k) + (last_ema)
    return ema
def calc_sma(prices, periods):
    prices = np.array(prices)
    sma = []
    for i in range(periods,len(prices)-1):
        sma.append(np.sum(prices[-periods:i]) / periods)
    return sma
def calc_ema(prices, periods):
    sma = calc_sma(prices, periods)
    ema = []
    for i in range(0, len(sma) - 1):
        if i == 0:
            ema.append(sma[0])
        else:
            ema.append(get_ema(sma[i], ema[i - 1], periods))
    return ema
def calc_macd(prices):
    ema_26 = calc_ema(prices, 26)
    ema_12 = calc_ema(prices, 12)
    macd_line = np.array(ema_12) - np.array(ema_26)
    signal_line = calc_ema(macd_line,9)
    return macd_line, signal_line

iota_prices = pd.read_csv('data/iota_price.csv')
iota_prices = iota_prices.iloc[::-1]
close_prices = iota_prices["Close"].tolist()
macd, signal = calc_macd(close_prices)
plt.plot(macd)
plt.plot(signal)
plt.show()
