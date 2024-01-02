import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest


url = "https://wuzzuf.net/search/jobs/?q=flutter+developer&a=navbl"
request = requests.get(url)
src = request.content

soup = BeautifulSoup(src, "lxml")

jobTitles = soup.find_all("h2", {"class": "css-m604qf"})
companies = soup.find_all("div", {"class": "css-d7j1kk"})
locations = soup.find_all("span", {"class": "css-5wys0k"})

job_titles = []
job_companies = []
job_locations = []
links = []
times = []
for i in range(len(jobTitles)):
    job_titles.append(jobTitles[i].text)
    links.append(jobTitles[i].find("a").attrs["href"])
    job_companies.append(companies[i].text)
    job_locations.append(locations[i].text)

# css-1t5f0fr => job requirments
# css-47jx3m => salary
salaries = []

requirments = []
for link in links:
    print(link)
    request2 = requests.get(link)
    src2 = request.content
    job_soup = BeautifulSoup(src2, "lxml")
    print(job_soup.find("h1", {"class": "css-f9uh36"}))
    # Use a new variable for the job detail page

    salary = job_soup.find("span", {"class": "css-47jx3m"})
    requirment = job_soup.find("div", {"class": "css-1t5f0fr"})
    salaries.append(salary)
    requirments.append(requirment)


my_files = [job_titles, job_companies, job_locations, salaries, requirments]
exported = zip(*my_files)

with open(
    "E:/web scriping/Projects/scraping/jobss.csv", "w", encoding="utf-8", newline=""
) as my_file:
    wr = csv.writer(my_file)
    wr.writerow(["job title", "company", "location"])
    wr.writerows(exported)
