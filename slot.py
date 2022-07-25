from requests_html import HTMLSession
import requests

s = HTMLSession()

iphone12 = 'https://slot.ng/apple-iphone-12-pro-128gb-single-sim-non-act.html'
iphone13 = 'https://kara.com.ng/apple-iphone-13pro-max-1tb-rom'


def get_slot_product_url(product_link):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
    url = product_link
    r = requests.get(url, headers=headers)
    r = s.get(url)
    r.html.render(sleep=1, keep_page=True, scrolldown=1) #gets the page and render all js script
    price = r.html.find('h5.mb-0', first=True).text
    phone={
        'price':price
    }
    return phone['price']

print(get_slot_product_url(iphone12))  
print(get_slot_product_url(iphone13)) 
    