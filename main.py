import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
import chart_studio.plotly as py 
from plotly.offline import init_notebook_mode, iplot 
init_notebook_mode(connected=True)
import plotly.graph_objs as go 

# 轰炸数据，本地实现时请自行更改路径
aerial = pd.read_csv("data/operations.csv")
# 第一个天气数据，气象站的位置
weather_station_location = pd.read_csv("data/Weather Station Locations.csv")
# 第二个天气数据，气象站的测量最低、最高和平均温度
weather = pd.read_csv("data/Summary of Weather.csv")

#检查时间序列平稳度需要调用下面的库函数
#from statsmodels.tsa.stattools import adfuller

#预测时间序列需要调用下列ARIMA模型相关函数
#from statsmodels.tsa.stattools import acf, pacf
#from statsmodels.tsa.arima_model import ARIMA
#from pandas import datetime

#评价预测效果，计算均方误差相关
#from sklearn.metrics import mean_squared_error