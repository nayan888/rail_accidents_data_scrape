# Imports the Necessary Pakage
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# Create some useful functions
def get_soup(url):
    """Takes a url and returns a BeautifulSoup object of the contents of url"""
    
    res = urlopen(url)
    return BeautifulSoup(res, 'lxml')


def get_events(bs):
    """Takes a BeautifulSoup object and returns a list of accidents"""
    
    ul_list = bs.select_one('.mw-parser-output').find_all('ul', recursive=False)
    events = []
    for ul in ul_list[:-3]:
        events.extend(ul.find_all('li'))
    return [event.text.split('–', maxsplit=2) for event in events]

# Retrive the wikipedia page and store data in a dataframe
url = 'https://en.wikipedia.org/wiki/List_of_rail_accidents_(1980%E2%80%931989)'
bs = get_soup(url)
accidents = pd.DataFrame(get_events(bs), columns = ['Date', 'Country', 'Description'])

# Save data in a excel file
accidents.to_excel('rail_accidents.xlsx')