import pandas as pd
import requests
url = "https://api.open-meteo.com/v1/forecast"
param ={
    "latitude": 28.61,    # Delhi
    "longitude": 77.20,
    "hourly": "temperature_2m"
}
response = requests.get(url, params=param)
data = response.json()
df = pd.DataFrame({
    "time": data["hourly"]["time"],
    "temperature": data["hourly"]["temperature_2m"]
})
print(df.head())