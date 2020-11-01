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
            category = _.text
            print(category)

    # title
    title = soup_book.find('div', class_='col-sm-6 product_main').h1.text
    #print(title)

    # table
    result = soup_book.find('table', class_='table table-striped')
    # for d in result.find_all('td'):
    #    print(d.text[:])
    for h, d in zip(result.find_all('th'), result.find_all('td')):
        if h.text[0:3] == 'UPC':
            print(d.text)
        else:
            print(d.text[1:])

    # image
    lien_img = soup_book.find('div', class_='item active')
    print('http://books.toscrape.com/'+lien_img.img['src'])


    if i >= 1:
        break


time.sleep(2)