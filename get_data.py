import yfinance as yf 
import requests
import pandas as pd
from requests_html import HTMLSession
#importing data about coin chosen by user
def get_coin(ticker, per, inter):
    coin = yf.download(
        tickers= ticker,
        period=per,
        interval=inter
    )
    coin.index = pd.to_datetime(coin.index)
    return coin
def get_coins_list():
    session = HTMLSession()
    resp = session.get(f"https://finance.yahoo.com/markets/crypto/all/?start=0&count=100")
    tables = pd.read_html(resp.html.raw_html)               
    df = tables[0].copy()
    symbols_yf = df.Symbol.tolist()
    return symbols_yf

#change yfinance to alphavantage
    