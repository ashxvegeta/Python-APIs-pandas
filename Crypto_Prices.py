import pandas as pd
import requests

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "ids": "bitcoin,ethereum,solana",
}
#fetch data from the API 
response = requests.get(url, params=params)
data = response.json()

# convert to DataFrame
df = pd.DataFrame(data,columns=["id", "symbol", "current_price", "market_cap", "high_24h", "low_24h"])
print(df)