# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 18:11:59 2022

@author: admin
"""


import streamlit as st
import openai

openai.api_key = st.secrets["key"]

USERNAME = 'tradingpro.112233@gmail.com'
PASSWORD = 'Vuatrochoi123'


import pandas as pd
import numpy
from datetime import datetime
import math
import matplotlib.pyplot as plt
from tvDatafeed import TvDatafeed,Interval
import pandas_ta as pandas_ta
import talib
from stockstats import StockDataFrame
import vectorbt as vbt

pd.set_option('expand_frame_repr', False)

tv = TvDatafeed(USERNAME, PASSWORD)
#--------------------------------------------------------------    
def return_time(time):
    try:
       if time == "1h":
           return Interval.in_1_hour
       elif time =="15m":
           return Interval.in_15_minute
       elif time == "30m":
           return Interval.in_30_minute
       elif time == "1m":
           return Interval.in_1_minute
       elif time == "5m":
           return Interval.in_5_minute
       elif time == "4h":
           return Interval.in_4_hour
       elif time == "2h":
           return Interval.in_2_hour
       elif time == "3h":
           return Interval.in_3_hour
       elif time == "3m":
           return Interval.in_3_minute
       elif time == "45m":
           return Interval.in_45_minute
       elif time == "1d":
           return Interval.in_daily
       elif time == "1w":
           return Interval.in_weekly
       elif time == "1M":
           return Interval.in_monthly

    except:
        return "Unknown time format"
#--------------------------------------------------------------    
# Get historical data

symbol = st.text_input("Insert symbol")

exchange = st.text_input("Insert exchange")
input_message = "Interval_time ['1m', '3m', '5m', '15m', '30m', '45m', '1h', '2h', '3h', '4h', '1d', '1w', '1M']"
interval_time = st.text_input(input_message) # Edit to user can change
n_bars = 10000 # No of bars to download, max 5000. Defaults to 10.

if not symbol:
  symbol = 'VNINDEX'
  
if not exchange:
  exchange = 'HOSE'
if not interval_time:
  interval_time = '4h'
interval_time = return_time(interval_time)
### Download from multi sources
print('-------------------')
print(f"Symbol: {symbol} - Exchange: {exchange}")
historical_market_price_df = tv.get_hist(symbol=symbol, exchange=exchange, interval=interval_time, n_bars=n_bars)
