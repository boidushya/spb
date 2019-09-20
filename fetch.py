from bs4 import BeautifulSoup as bs
import urllib.request
from pprint import pprint
from random import choice as rc
import sys
import os
def get_lnk(query):
    url = "https://www.shitpostbot.com/gallery/sourceimages?review_state=accepted&query=" + query +"&order=total_rating&direction=DESC"
    response = urllib.request.urlopen(url)
    soup = bs(response,'lxml')
    result = []
    for div in soup.findAll('div', attrs={'class':'img'}):
        result.append(div.find('a')['href'])
    fin = rc(result)
    return 'https://www.shitpostbot.com' + fin

def get_img(cmd):
    url = get_lnk(cmd)
    response = urllib.request.urlopen(url)
    soup = bs(response,'lxml')
    # result = []
    for div in soup.findAll('div', attrs={'style':'padding-top: 15px'}):
        return 'https://www.shitpostbot.com' + (div.find('a')['href'])

def dl(url):
    if not os.path.exists('images'):
        os.mkdir('images')
    urllib.request.urlretrieve(url,'images/' + url.replace('https://www.shitpostbot.com/img/sourceimages/', ''))
    print('Successfully downloaded ' + url.replace('https://www.shitpostbot.com/img/sourceimages/', ''))

# if __name__ == '__main__':
#     url = get_img('nice')
#     dl(url)

if len(sys.argv) <= 2 :
    print("\nUsage:\npython fetch.py -q [query] \n ")
    sys.exit (1)
elif sys.argv[1] == '-q':
    url = get_img(str(sys.argv[2]))
    dl(url)
