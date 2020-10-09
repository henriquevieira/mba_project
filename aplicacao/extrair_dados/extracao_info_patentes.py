# Extracao de informacoes de patentes
#
# Henrique Cursino Vieira

import requests
from bs4 import BeautifulSoup


# cada pagina lista 50 patentes, alterar a variavel n para obter o numero de
# patentes de interesse

p = 4

link = "https://www.freepatentsonline.com/result.html?p=1&sort=relevance&srch=top&query_txt=agronomy&patents_us=on"

page = requests.get(link)
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.text)

soup.


# for i in range(1, p+1):
