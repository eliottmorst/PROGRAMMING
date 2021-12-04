import yfinance as yf
import plotly.graph_objects as go

nasdaq = yf.Ticker('NQZ21.CME')

data  =  nasdaq.history(start='2021-01-01',  end='2021-11-21')
data.head()
data = data.reset_index()
for i in ['Open', 'High', 'Close', 'Low']: 
      data[i]  =  data[i].astype('float64')
      
fig = go.Figure(data=[go.Candlestick(x=data['Date'],
                                   open=data['Open'],
high=data['High'],
low=data['Low'],
close=data['Close'])])
fig.show()      
      

