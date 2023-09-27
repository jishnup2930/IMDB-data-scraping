# from bs4 import BeautifulSoup
# from urllib import request
# import pandas as pd
# import json
#
# def soupFunction(url):
#     html = request.urlopen(url).read()
#     soup = BeautifulSoup(html, 'html.parser')
#     return soup

from bs4 import BeautifulSoup
from urllib import request
import pandas as pd
import json

def soupFunction(url):
    req = request.Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    html = request.urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

# rest of the code remains unchanged



# def  allLinks():
#     urls = []
#     myMovies = []
#     soup = soupFunction('https://www.imdb.com/chart/top/')
#     for i in soup.findAll('a'):   # anger tag in html code
#         links = i.get('href')
#         urls.append(links)
#     urls=['https://www.imdb.com' + x.strip() for x in urls if x is not None and x.startswith('/title/tt')]
#     for link in urls:
#         if link not in myMovies:
#              myMovies.append(link)
#         return myMovies

def allLinks():
    urls = []
    myMovies = []
    soup = soupFunction('https://www.imdb.com/chart/top/')
    for i in soup.findAll('a'):   # anger tag in html code
        links = i.get('href')
        urls.append(links)
    urls=['https://www.imdb.com' + x.strip() for x in urls if x is not None and x.startswith('/title/tt')]
    for link in urls:
        if link not in myMovies:
             myMovies.append(link)
    return myMovies


def getMovieInfo():
    datalist = []
    myMovies = allLinks()

    for i in myMovies[0:20]:
        soup = soupFunction(i)
        titleClass = soup.find('div',{'class':'sc-dffc6c81-0 iwmAVw'})
        title = titleClass.find('h1').text

        imageClass = soup.find('meta',property='og:image')
        movieimage = imageClass['content']

        genreClass = soup.find('div',{'class':'ipc-chip-list__scroller'})
        genre = genreClass.find('span').text

        directorClass = soup.find('div',{'class':'ipc-metadata-list-item__content-container'})
        director = directorClass.find('a').text

        myData={
            'Movie name': title,
            'Poster': movieimage,
            'Movie genre': genre,
            'Movie director': director
        }
        datalist.append(myData)
    jsonFile = open('finalData.json', 'w')
    json.dump(datalist, jsonFile)


if __name__ == '__main__':
    getMovieInfo()