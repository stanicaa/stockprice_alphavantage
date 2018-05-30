import json
from urllib import request
import pandas

#this program gets the stock prices for a US listed company and runs simple statistics on it, using AlphaVantage
code=input('company code: ')

#the function that gets all the info and creates the link that gets the data. Default is the last 100 days.
def daily_prices(code):
    home='https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='
    #if wanting the full (20yrs) frame, add outputsize=full in front of the api_key below
    api_key='INPUT_YOUR_KEY_HERE'
    #d_type='&datatype=csv'if you want the data in csv format. Code below need be changed to deal with csv file type instead of json.
    link=home+code+api_key
    return link

f=request.urlopen(daily_prices(code)).read().decode('utf8')

#creating a pandas out of the input - it makes any statistics realted work very easy.
a=json.loads(f)
b=pandas.DataFrame.from_dict(a['Time Series (Daily)'], orient='index')

print(b)
b1=b[['4. close']]
b1['4. close']=b1['4. close'].astype(float)

print(b1.describe())
print('Kurtosis ', b1.kurtosis())
print('Skewness ', b1.skew())
