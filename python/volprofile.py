import pandas as pd
import numpy as np
from scipy import stats, signal
import plotly.express as px
import plotly.graph_objects as go

# Fetch OHLCV data
data = some_data_load_function('EURUSD')
volume = data['volume']
close = data['close']