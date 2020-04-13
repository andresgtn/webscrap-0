import requests
import pprint
from bs4 import BeautifulSoup

# Retrieve the HTML
URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)
# If you wish to view html file then pprint
# pprint.pprint(page.content)

# parse entire html into beautiful soup for manipulation
soup = BeautifulSoup(page.content, 'html.parser')

# retrieve div with job posts as ID
results = soup.find(id='ResultsContainer')

# find all job cards as classes
#job_elems = results.find_all('section', class_='card-content')
python_jobs = results.find_all('h2',
                               string=lambda text: "python" in text.lower())

for p_job in python_jobs:
    link = p_job.find('a')['href']
    print(p_job.text.strip())
    print(f"Apply here: {link}\n")