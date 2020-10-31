# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import time

req = requests.get('http://books.toscrape.com/')
soup = BeautifulSoup(req.text, "lxml")
#print(soup.prettify())


books = soup.find('ol', class_='row')

i = 0
for book in books.find_all('li'):
    i += 1
    link = 'http://books.toscrape.com/' + book.a['href']

    # ---------------------------------------------------
    # product details
    # ---------------------------------------------------

    # new requests
    req_book = requests.get(link)
    soup_book = BeautifulSoup(req_book.text, "lxml")

    # category
    head = soup_book.find('ul', class_='breadcrumb')
    j = 0
    for _ in head.find_all('li'):
        j += 1
        if j ==3:
            print(_.text)



    # table
    result = soup_book.find('table', class_='table table-striped')
    #print((result.find('tr').th).text, (result.find('tr').td).text)

    if i >= 1:
        break


time.sleep(2)