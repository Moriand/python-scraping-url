import requests
import re
from bs4 import BeautifulSoup as bs

#r = requests.get("https://mrlpythongui.blogspot.com/")
print("ingrese url de el solucionario ")
url = input("> ")
r = requests.get(url)
html = r.content
soup = bs(html, 'html.parser')
posts = soup.find_all('div',{"class":"panel-body"})
post = posts[0]
libro = post.find('div',{"class":"table-block dwl"})
#---------------
otro = post.find_all('div',{"class" : "table-download"})
#---------------
url = post.find('a',{"class": "download"})["href"]
formato = post.find('div',{"class": "table-item"}).text
tipo = post.find('div', {"class": "table-item"}).text
idioma = post.find('div', {"class": "table-item"}).text
print(url)
print("-----=====================================")
tipo = otro[0].find("div", {"class" : "table-block"})
idioma = otro[0].find("div", {"class" : "table-block hidden-mobile"})
text_tipo = tipo.find("div", {"class" : "table-item"}).text
text_formato = idioma.find("div", {"class" : "table-item"}).text
print(text_tipo)
print(text_formato)
salir = input("presione una tecla para salir")
