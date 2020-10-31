from bs4 import BeautifulSoup
import requests
import time

req = requests.get('http://books.toscrape.com/')
soup = BeautifulSoup(req.text, "lxml")
#print(soup.prettify())


books = soup.find('ol', class_='row')

for book in books.find_all('li'):
    #print(book.a['href'])
    link = 'http://books.toscrape.com/' + book.a['href']

    req_book = requests.get(link)
    soup_book = BeautifulSoup(req.text, "lxml")

    
time.sleep(2)