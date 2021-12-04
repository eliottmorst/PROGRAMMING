import yfinance as yf
import plotly.graph_objects as go
import plotly.express as px


#decllare ticker
nasdaq = yf.Ticker('NQZ21.CME')

#get data from yfinance
old  =  nasdaq.history(start='2021-10-01',  end='2021-11-21')
old = old.reset_index()
for i in ['Open', 'High', 'Close', 'Low']: 
      old[i]  =  old[i].astype('float64')

#visualize candles with plotly
#fig = go.Figure(data=[go.#Candlestick(x=old['Date'],
#open=old['Open'],
#high=old['High'],
#low=old['Low'],
#close=old['Close'])])
#fig.show()

#visualize line with ploty express
fig = px.line(old, x="Date", y="Open", title='Nasdaq Oct 1st to Nov 21st ')
fig.show()

  
    
