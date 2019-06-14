from bs4 import BeautifulSoup
import json
import urllib.request
import os

with urllib.request.urlopen('https://www.giffgaff.com/mobile-phones/apple/apple-iphone-8-refurbished/phone-details') as response:
    contents = response.read()
    soup = BeautifulSoup(contents, 'lxml')
    blob = soup.find(id='frmBuyPhone')['data-color-memory-mapping']
    phones = json.loads(blob)
    stock = phones['space-grey']['64000']['stock']
    print('Debug:')
    print(phones)
    print()
    print("iPhone 8 refurbished 64GB Space Grey stock:")
    print(stock)
    if stock > 0:
      os.system('osascript -e \'display notification "Stock: {}" with title "Giffgaff iPhone notifications"\''.format(stock))
