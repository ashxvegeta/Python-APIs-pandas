
# Mini-Project Task for You

# Pick either Crypto API or Weather API

# Fetch the data

# Convert JSON → pandas DataFrame

# Print top 5 rows
# Sorting by market_cap (largest to smallest):
# top 3 coins by price
import pandas as pd
import requests

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "ids": "bitcoin,ethereum,solana,cardano,ripple,polkadot,litecoin,chainlink,stellar,uniswap",
}

response = requests.get(url, params=params)
data = response.json()
df = pd.DataFrame(data, columns=["id", "symbol", "current_price", "market_cap", "high_24h", "low_24h"])
print(df.head())
# Sorting by market_cap (largest to smallest):
print(df.sort_values(by="market_cap", ascending=False))
# top 3 coins by price
print(df.nlargest(3, "current_price")[['id', 'current_price']])

df["%_change_from_low"] = ((df["current_price"] - df["low_24h"]) / df["low_24h"]) * 100
print(df[["id", "current_price", "low_24h", "%_change_from_low"]])
