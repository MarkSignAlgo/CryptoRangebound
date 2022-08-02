#function that gets the crypto data from the API
import requests
import json
import datetime
import pandas as pd

def apiCoin(crypto):
    tday=datetime.datetime.today()strftime('%Y-%m-%d')
    t=tday+'T00:00:00'
    root='https://rest.coinapi.io/v1/ohlcv/{}/USD/history?period_id=1DAY&time_start=2021-05-01T00:00:00&time_end='
    link=root+t+'&limit=4000'
    u=link.format(crypto.upper())
    headers={'X-CoinAPI-Key': 'YOU PRIVATE KEY HERE'}
    r=requests.get(u, headers=headers)
    columns=['date', 'close', 'open', 'low', 'high', 'volume']
    h=['time_period_end', 'price_close', 'price_open', 'price_low', 'price_high', 'trades_count']
    rr=json.loads(r.text)
    dl=list()
    for i in rr:
        el=list()
        for k in h:
            if k=='time_period_end':
                el.append(i[k][:10])
            else:
                el.append(i[k])
        dl.append(el)
    dl=dl[:-1]
    df=pd.DataFrame(dl, columns=columns)
    return df
