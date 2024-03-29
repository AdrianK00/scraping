from bs4 import BeautifulSoup
import requests

url = "https://www.coindesk.com"
page = requests.get(url)

soup = BeautifulSoup(page.text, "lxml")

#Get all cryptos
cryptos = soup.find_all("div", class_ = "pricing-col")

for crypto in cryptos:

    #Get all cryptos names
    crypto_name = crypto.find("div", class_ = "title").text.split()[0]

    #Get all cryptos prices
    crypto_price_with_none = crypto.find("div", class_ = "price val-negative")

    #Filter prices with None value
    if crypto_price_with_none != None:
        crypto_price = crypto.find("div", class_ = "price val-negative").text

    print(crypto_name)
    print(crypto_price)