import requests
from bs4 import BeautifulSoup
import smtplib
import time



headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }


def send_email():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('','')
    body = 'Visita el siguiente link de Amazon: https://www.amazon.es/gp/product/B00CUJQ7UG/ref=ox_sc_act_title_1?smid=A1AT7YVPFBWXBL&psc=1 '
    asunto = "El precio a llegado a lo deseado!!"
    message = f"Subject:{asunto}\n\n {body}"

    server.sendmail(
            '',
            '',
            message
    )

    print("Email enviado")

    server.quit()




def get_amazon_price(url):
    response = requests.get(url, headers = headers)
    soup = BeautifulSoup(response.content,'html.parser')
    soup2 = BeautifulSoup(soup.prettify(),'html.parser')
    title = soup2.find(id = "productTitle").get_text()
    price = soup2.find(id = "priceblock_ourprice").get_text()
    print(title.strip())
    print(price.strip())
    
    if price <= '7' :
        send_email()

while(True):
    get_amazon_price('https://www.amazon.es/gp/product/B00CUJQ7UG/ref=ox_sc_act_title_1?smid=A1AT7YVPFBWXBL&psc=1')
    time.sleep(86400)

