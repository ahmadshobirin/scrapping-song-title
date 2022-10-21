import requests
from pprint import pprint
from bs4 import BeautifulSoup

r = requests.get("https://www.gramedia.com/best-seller/lagu-pop-indonesia-terpopuler/")
  
soup = BeautifulSoup(r.content, 'html5lib') 
musics=[]
   
listDivs = soup.find('div', attrs = {'class':'entry-content g1-typography-xl'}) 
   
i = 1
for row in listDivs.findAll('h3'):
    song = {}
    song['Nomor'] = i

    songTitle = row.text
    songTitleWithoutNumber = ''.join([i for i in songTitle if not i.isdigit()])
    song['Title'] = songTitleWithoutNumber.strip('. \xa0.')
    musics.append(song)
    i+=1

pprint(musics)