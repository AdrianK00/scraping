from bs4 import BeautifulSoup
import requests

url = "https://www.coindesk.com"
page = requests.get(url)

soup = BeautifulSoup(page.text, "lxml")

all_cryptos = soup.find("div", class_ = "pricing-container")
cryptos = all_cryptos.find_all("div", class_ = "pricing-col")

for crypto in cryptos:
    crypto_name = crypto.find("div", class_ = "title").text.split()[0]
    crypto_price_with_none = crypto.find("div", class_ = "price val-negative")
    if crypto_price_with_none != None:
        crypto_price = crypto.find("div", class_ = "price val-negative").text
    print(crypto_name)
    print(crypto_price)