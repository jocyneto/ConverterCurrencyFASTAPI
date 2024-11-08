import requests
import aiohttp
from os import getenv
from fastapi import HTTPException


APIKEY_ALPHAVANTAGE = getenv("APIKEY_ALPHAVANTAGE")

def sync_converter(from_currency: str, to_currency:str, price:float):
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={APIKEY_ALPHAVANTAGE}"

    try:
        response = requests.get(url)
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)
    # end try

    data = response.json()

    if "Realtime Currency Exchange Rate" not in data:
        raise HTTPException(status_code=400, detail="Realtime Currency Exchange Rate não está contido em data.")
    
    exchage_rate = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])

    return price * exchage_rate

async def async_converter(from_currency: str, to_currency:str, price:float):
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={APIKEY_ALPHAVANTAGE}"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)
    # end try

    if "Realtime Currency Exchange Rate" not in data:
        raise HTTPException(status_code=400, detail=f"Realtime Currency Exchange Rate não está contido em data. {data}")
    
    exchage_rate = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])

    return price * exchage_rate

async def async_converter2(from_currency: str, to_currency:str, price:float):
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={APIKEY_ALPHAVANTAGE}"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)
    # end try

    if "Realtime Currency Exchange Rate" not in data:
        raise HTTPException(status_code=400, detail=f"Realtime Currency Exchange Rate não está contido em data. {data}")
    
    exchage_rate = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])

    return {to_currency: price * exchage_rate}
