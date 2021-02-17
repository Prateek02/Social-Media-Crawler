import requests
import pandas as pd
from bs4 import BeautifulSoup
from IPython.display import display

urls = ["http://su.edu.ph/",
"https://uz.edu.ph/",
"https://www.vsu.edu.ph/",
"https://www.msu.edu.ph/"
]

sm_sites = ['facebook.com','twitter.com']
sm_sites_present = []
columns = ['url'] + sm_sites
df = pd.DataFrame(data={'url' : urls}, columns=columns)

def get_sm(row):
    r = requests.get(row['url'])
    output = pd.Series([],dtype=pd.StringDtype())

    soup = BeautifulSoup(r.content, 'lxml')
    all_links = soup.find_all('a', href = True)
    for sm_site in sm_sites:
        for link in all_links:
            if sm_site in link.attrs['href']:
                output[sm_site] = link.attrs['href']
    return output

sm_columns = df.apply(get_sm, axis=1)
df.update(sm_columns)
df.fillna(value='no link')
df.to_csv('file1.csv') 
print(df)
