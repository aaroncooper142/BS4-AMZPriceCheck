from bs4 import BeautifulSoup
import requests
import smtplib

URL = "https://www.amazon.com/Instant-Pot-Electric-Pressure-Stainless/dp/B081Z9FKDB/ref=dp_fod_1?pd_rd_i=B081Z9FKDB&psc=1"
USERAGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
ACCEPTLANGUAGE = "en-US,en;q=0.9"



'''pull price'''

response = requests.get(URL, headers={"User-Agent": USERAGENT,"Accept-Language": ACCEPTLANGUAGE})

soup = BeautifulSoup(response.text,"html.parser")
# print(soup)

# looking for this elemet <span id="priceblock_ourprice" class="a-size-medium a-color-price priceBlockBuyingPriceString">$130.89</span>

price = soup.find(id="priceblock_ourprice", class_="a-size-medium a-color-price priceBlockBuyingPriceString")
price_float = float(price.getText()[1:])
print(price_float)

desired_price = 100.00


'''email if price is =<100'''

def email(price):
    global URL
    # create environment variables if publishing an excecutable version with sensitive email information
    my_email = "example email"
    password = "example password"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # secures connection
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:AMZ Purchase Price Dip\n\nThe price is {price}, buy now @ {URL}."
        )


if price_float <= desired_price:
    email(price_float)
