import requests
from bs4 import BeautifulSoup

# retrieve the HTML
URL = 'https://weather.com/it-IT/tempo/oggi/l/56ce91b16694095b0274c72cbfcc8af0e76b63753eaaff52e4a56184d0bca51b'
page = requests.get(URL)

# parsing dell' HTML and finding the element
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='hero-left-Nowcard-92c6937d-b8c3-4240-b06c-9da9a8b0d22b')
nome = soup.find_all('span', class_='today_nowcard-loc-title-wrqpper')
card = results.find_all('div', class_='today_nowcard-section today_nowcard-condition')
data_elem = soup.find_all('div', class_='today_nowcard-sidecar component panel')
values = []

for name in nome:
    name_elem = name.find('h1', class_='h4 today_nowcard-location')
    print(name_elem.text.strip())

for degree in card:
    degree_elem = degree.find('span', class_='')
    print(degree_elem.text.strip())

for tr in soup.find('div', class_='today_nowcard-sidecar component panel').find_all('tr'):
    values.append(list(tr.stripped_strings))

# Formatting values for display activity
wind = values[0]
humidity = values[1]
pressure = values[3]
print('wind: '+wind[1])
print('humidity: '+humidity[1])
print('pressure: '+pressure[1])


#TEMPLATE


