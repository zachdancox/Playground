import requests
# import libraries
import urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime

data = []

# specify the url

quote_page = ['https://www.bloomberg.com/quote/INDU:IND', 'http://www.bloomberg.com/quote/CCMP:IND']

for pg in quote_page:
    # query the website and return the html to the variable 'page'
    page = urllib2.urlopen(pg)

    # parse the html using beautiful soap and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')

    # Find the ticker name and print it
    ticker = soup.find('div', attrs={'class': 'ticker'})
    ticker = ticker.text.strip()
    print ticker

    # Find the price of the ticker
    price = soup.find('div', attrs={'class': 'price'})
    price = price.text
    print price

    # save the data in tuple
    data.append((ticker, price))

    # open a csv file with append, so old data will not be erased
    with open('index.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        for ticker, price in data:
            writer.writerow([ticker, price, datetime.now()])

