from bs4 import BeautifulSoup
import requests
import pandas as pd

csv_url = 'https://en.wikipedia.org/wiki/Comma-separated_values'
table_name = 'wikitable'

response = requests.get(csv_url)
soup = BeautifulSoup(response.text, 'html.parser')
wiki_table = soup.find('table', {'class':table_name})
df = pd.read_html(str(wiki_table))

print(pd.concat(df).to_csv('Assignment 2.csv'))