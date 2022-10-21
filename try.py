import requests
from pprint import pprint
from bs4 import BeautifulSoup
import csv
from pathlib import Path


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
    print(song, "\n")
    musics.append(song)
    i+=1

with open("song_scrapper.csv", 'w', newline='') as f:
    w = csv.DictWriter(f,['Nomor','Title'])
    w.writeheader()
    for music in musics:
        w.writerow(music)