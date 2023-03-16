import math
import requests
from bs4 import BeautifulSoup

amazon_url = "https://www.amazon.com/dp/B08L5T31M6"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                  "104.0.5112.102 Safari/537.36 OPR/90.0.4480.84",
    "Accept-Language": "en-US,en;q=0.9"}

switch = True

while switch:
    response = requests.get(url=amazon_url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")

    price = soup.find(name="span", attrs={"class": "a-price-whole"})

    if price is not None:
        price = int(price.getText())
        if price < 500:
            print(price)
            switch = False
