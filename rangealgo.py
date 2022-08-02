#the autonomous rangebound investment algorithm
import datetime
import pandas as pd

def crypto_pattern(df, length, holding, loss_cut):
    positions=list()
    i=0
    if length+holding+2<len(df):
        while i <(len(df)-length-holding-2):
            dfi=df[i:i+length]
            if dfi['close'].max()/dfi['close'].min()<1.08: #the value 1.08 can be set subject to the stock volatility too
                m=dfi['close'].mean()
                s=dfi['close'].std()
                if s/m<0.03:
                    #check for position innitiation
                    if df['close'].iloc[i+length+1]>dfi['close'].max():
                        #INITIATING POSITION
                        perf=df['close'].iloc[i+length+1+holding]/df['close'].iloc[i+length+1]
                        perf=(perf-1)*100
                        positions.append([i+length+1, i+length+holding+1, df['date'].iloc[i+length+1].strftime('%y-%m-%d'),
                            df['date'].iloc[i+length+holding+1].strftime('%y-%m-%d'), perf, ticker])
                        i=i+length+holding+1
                        #ADD LOSS CUT CONDITION??
                    else:
                        i=i+1
                else:
                    i=i+1
            else:
                i=i+1
    return positions
