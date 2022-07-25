import requests
from bs4 import BeautifulSoup

iphone11_ProMax= 'https://www.konga.com/product/apple-iphone-11-pro-max-6-5-256gb-rom-4gb-ram-ios-13-3969mah-gold-5699852'
iphone11='https://www.konga.com/product/apple-iphone-11-128gb-rom-4gb-ram-red-4719450'
iphone6='https://www.konga.com/product/apple-iphone-6-4-7-16gb-grey-4623548'
iphone7_plus='https://www.konga.com/product/iphone-7-plus-5-5-32gb-rom-3gb-ram-nano-sim-black-5226700'
iphone8_plus='https://www.konga.com/product/apple-iphone-8-plus-5-5-64gb-rom-3gb-ram-ios-11-12mp-5630055'
iphoneX='https://www.konga.com/product/apple-iphone-x-256gb-pouch-screen-guide-selfie-stick-grey-4678237'
iphoneXS_Max='https://www.konga.com/product/apple-iphone-xs-max-6-5-oy-4gb-ram-64gb-rom-gold-5511576'
iphone13_ProMax='https://www.konga.com/product/apple-iphone-13-pro-128gb-5g-sierra-blue-5501066'
iphone12_ProMax='https://www.konga.com/product/apple-iphone-12-pro-max-256gb-6gb-ram-6-7-pacific-blue-5187171'



#Just add the product link here and fetch the price

def konga(product_link):
    konga_url = product_link
    page = requests.get(url=konga_url)
    soup=BeautifulSoup(page.content,'lxml')
    name =soup.find('h4', class_='_24849_2Ymhg').text
    price =soup.find('div', class_='_678e4_e6nqh').text
    phone={
        'name':name,
        'price':price
    }
    return phone


print(konga(iphoneX))
print(konga(iphone11_ProMax))
print(konga(iphone11))
print(konga(iphone13_ProMax))
print(konga(iphone12_ProMax))
print(konga(iphoneXS_Max))
print(konga(iphone8_plus))
print(konga(iphone7_plus))
print(konga(iphone6))
