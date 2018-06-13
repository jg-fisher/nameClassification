import requests
from bs4 import BeautifulSoup as bs

# top 100 names
nations = ['USA', 'RUS', 'CHN']
url = lambda n: 'http://www.studentsoftheworld.info/penpals/stats.php3?Pays={}'.format(n)

headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': 'jfishersolutions@gmail.com'
        }

with open('data.csv', 'w') as f:

    for nation in nations:
        r = requests.get(url(nation), headers=headers)
        soup = bs(r.content, 'html.parser')
    
        for tag in soup.find_all('nobr'):
            f.write('{0},{1}\n'.format(str(tag.findNext('font').text).lower(), nation))

f.close()
