from django.http import HttpResponse

# importing loading from django template
from django.template import loader

import requests
from bs4 import BeautifulSoup
import re
import datetime

# retrieve the HTML
URL_ve = 'https://weather.com/it-IT/tempo/oggi/l/56ce91b16694095b0274c72cbfcc8af0e76b63753eaaff52e4a56184d0bca51b'
page_ve = requests.get(URL_ve)
URL_pn = 'https://weather.com/it-IT/tempo/oggi/l/2d132c59a3f53d9acb5ea99fbb0cb35c125d24210f6f2cfc9a4c3ddee408c528'
page_pn = requests.get(URL_pn)


# parsing dell' HTML and finding the element
# VE
soup = BeautifulSoup(page_ve.content, 'html.parser')
results_ve = soup.find(id='hero-left-Nowcard-92c6937d-b8c3-4240-b06c-9da9a8b0d22b')
nome_ve = soup.find_all('span', class_='today_nowcard-loc-title-wrqpper')
card_ve = results_ve.find_all('div', class_='today_nowcard-section today_nowcard-condition')
data_elem_ve = soup.find_all('div', class_='today_nowcard-sidecar component panel')
icon_elem_ve = soup.find_all('div', class_='today_nowcard-section today_nowcard-condition')
values_ve = []

for name in nome_ve:
    name_elem_ve = name.find('h1', class_='h4 today_nowcard-location')
    print(name_elem_ve.text.strip())

for degree in card_ve:
    degree_elem_ve = degree.find('span', class_='')
    print(degree_elem_ve.text.strip())

for tr in soup.find('div', class_='today_nowcard-sidecar component panel').find_all('tr'):
    values_ve.append(list(tr.stripped_strings))

for meteo_ve in icon_elem_ve:
    icon_ve = meteo_ve.find('div', class_='today_nowcard-phrase')
    print(icon_ve.text.strip())


    # Change icon when detecting word
    icon_value_ve='sun'
    if 'Nuvoloso' in icon_ve:
        icon_value_ve: str = 'cloud'
    elif 'Molto nuvoloso' in icon_ve:
        icon_value_ve: str = 'cloud'
    elif 'Foschia' in icon_ve:
        icon_value_ve: str = 'fog'
    elif 'Nebbia' in icon_ve:
        icon_value_ve: str = 'fog'
    elif 'Rovesci' in icon_ve:
        icon_value_ve: str = 'rain'
    elif 'Precipitazioni' in icon_ve:
        icon_value_ve: str = 'rain'
    elif 'Temporali' in icon_ve:
        icon_value_ve: str = 'thunder'
    elif 'Neve' in icon_ve:
        icon_value_ve: str = 'snow'
    elif 'Nevicate' in icon_ve:
        icon_value_ve: str = 'snow'



    # Change icon when detecting time
    hour = int(datetime.datetime.now().strftime('%H'))
    if hour < 6 or hour > 20:
        if icon_ve == 'Sereno':
            icon_value_ve = 'moon'


    # Getting the degree number to set image
    gradi_ve = degree_elem_ve.text.strip()
    grado_ve = re.findall('\d+', gradi_ve)

    temp_icon_ve = 'warm'
    if int(grado_ve[0]) < 10:
        temp_icon_ve = 'cold'
    elif 10 < int(grado_ve[0]) < 21:
        temp_icon_ve = 'warm'
    elif int(grado_ve[0]) > 20:
        temp_icon_ve = 'hot'

# PN
soup = BeautifulSoup(page_pn.content, 'html.parser')
results_pn = soup.find(id='hero-left-Nowcard-92c6937d-b8c3-4240-b06c-9da9a8b0d22b')
nome_pn = soup.find_all('span', class_='today_nowcard-loc-title-wrqpper')
card_pn = results_pn.find_all('div', class_='today_nowcard-section today_nowcard-condition')
data_elem_pn = soup.find_all('div', class_='today_nowcard-sidecar component panel')
icon_elem_pn = soup.find_all('div', class_='today_nowcard-section today_nowcard-condition')
values_pn = []

for name in nome_pn:
    name_elem_pn = name.find('h1', class_='h4 today_nowcard-location')
    print(name_elem_pn.text.strip())

for degree in card_pn:
    degree_elem_pn = degree.find('span', class_='')
    print(degree_elem_pn.text.strip())

for tr in soup.find('div', class_='today_nowcard-sidecar component panel').find_all('tr'):
    values_pn.append(list(tr.stripped_strings))

for meteo_pn in icon_elem_pn:
    icon_pn = meteo_pn.find('div', class_='today_nowcard-phrase')
    print(icon_pn.text.strip())

    icon_value_pn ='sun'
    if 'Nuvoloso' in icon_pn:
        icon_value_pn: str = 'cloud'
    elif 'Molto nuvoloso' in icon_pn:
        icon_value_pn: str = 'cloud'
    elif 'Foschia' in icon_pn:
        icon_value_pn: str = 'fog'
    elif 'Nebbia' in icon_pn:
        icon_value_pn: str = 'fog'

    # Change icon when detecting time
    hour = int(datetime.datetime.now().strftime('%H'))
    if hour < 6 or hour > 20:
        if icon_pn == 'Sereno':
            icon_value_pn = 'moon'

    # Getting the degree number to set image
    gradi_pn = degree_elem_pn.text.strip()
    grado_pn = re.findall('\d+', gradi_pn)

    temp_icon_pn = 'warm'
    if int(grado_pn[0]) < 10:
        temp_icon_pn = 'cold'
    elif 10 < int(grado_pn[0]) < 21:
        temp_icon_pn = 'warm'
    elif int(grado_pn[0]) > 20:
        temp_icon_pn = 'hot'

# Formatting values for display activity
#VE
wind_ve = values_ve[0]
humidity_ve = values_ve[1]
pressure_ve = values_ve[3]
print('wind: '+wind_ve[1])
print('humidity: '+humidity_ve[1])
print('pressure: '+pressure_ve[1])

# PN
wind_pn = values_pn[0]
humidity_pn = values_pn[1]
pressure_pn = values_pn[3]
print('wind: '+wind_pn[1])
print('humidity: '+humidity_pn[1])
print('pressure: '+pressure_pn[1])

# ----------------------------------------------------------------------------------------------------------------------
# our view which is a function named index
def index(request):
    # getting our template
    template = loader.get_template('index.html')

    # creating the values to pass
    context = {
        'name_ve': name_elem_ve.text.strip(),
        'degree_ve': degree_elem_ve.text.strip(),
        'wind_ve': wind_ve[1],
        'humidity_ve': humidity_ve[1],
        'pressure_ve':pressure_ve[1],
        'name_pn': name_elem_pn.text.strip(),
        'degree_pn': degree_elem_pn.text.strip(),
        'wind_pn': wind_pn[1],
        'humidity_pn': humidity_pn[1],
        'pressure_pn': pressure_pn[1],
        'icon_ve': icon_value_ve,
        'icon_pn': icon_value_pn,
        'temp_ve': temp_icon_ve,
        'temp_pn': temp_icon_pn
    }

    # rendering the template in HttpResponse
    # but this time passing the context and request
    return HttpResponse(template.render(context, request))
# ----------------------------------------------------------------------------------------------------------------------