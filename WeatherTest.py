import requests
import pandas as pd
url = "https://www.metaweather.com/api/"
params="location/44418"
r=requests.get(url+params)

rsp=r.json()

df=pd.DataFrame(rsp["consolidated_weather"])
