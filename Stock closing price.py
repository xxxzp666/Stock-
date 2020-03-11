# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 21:51:26 2019

@author: ABC
"""

import pandas as pd
import tushare as ts
import time

#get  period
begin_time='2018-01-01'
end_time=time.strftime('%Y-%m-%d',time.localtime())

#get close price
while True:
    code=input('Please enter a stock code : ')
    if not code.isdigit():
        print('please enter a positive integer!')
        continue 
    codes=int(code)
    if len(code)>5 and len(code)<=6:
        break
    else:
        print('please enter a six-digit code')

close_price=ts.get_hist_data(code,start=begin_time,end=end_time)['close']

#View 10 records from the end of the data frame
close_price.tail(10)

#n days mavg
while True:
    day=input('Please enter a moving average number of days : ')
    if not day.isdigit():
        print('please enter a positive integer!')
        continue 
    days=int(day)
    if days>0 and days<=100:
        break
    else:
        print('please enter a numeber between 0~100')
mavg=close_price.rolling(window=days).mean()


#draw mavg picture
import matplotlib.pyplot as plt
from matplotlib import style 
#adjusting the size of matplotlib
import matplotlib as mpl
mpl.rc('figure',figsize=(10,8))
#adjusting the style of matplotlib
style.use('ggplot')
close_price.plot(label='actual close')
mavg.plot(label=day+' mavg')
plt.legend()
plt.ylabel('price')

#rate of return
re=close_price/close_price.shift(1)-1
re.plot(label='return')
plt.legend()