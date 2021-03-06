#The script scrapes data as present on https://coinranking.com

from urllib2 import urlopen as opn
from bs4 import BeautifulSoup as soup

url = 'https://coinranking.com'

client = opn(url)
page = client.read()

fhand = open('data_crypto.csv','w')

page = soup(page,'html.parser')

container = page.find_all('a', {"class":"coin-list__body__row"})

for item in container:
    name = item.find('span',{"class":"coin-name"}).text
    cur_price = item.find('span',{'class':"coin-list__body__row__price__value"}).text
    market_cap = item.find('span',{'class':'coin-list__body__row__market-cap__value'}).text
    percent_change = item.find('span',{'class':'coin-list__body__row__change'}).text.strip()

    print "Name:\t\t" + name
    print "Current Price:\t" + cur_price
    print "Market Cap:\t" + market_cap
    print "24 Hr change:\t" + percent_change + '\n'

    fhand.write(name + ',' +  cur_price.replace(',',' ') + ',' + market_cap.replace(',',' ') + ',' + percent_change + '\n')


fhand.close()

