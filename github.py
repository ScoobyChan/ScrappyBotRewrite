# github
import re
import requests
from bs4 import BeautifulSoup

URL = 'https://github.com/ScoobyChan/ScrappyBotRewrite/commit/main'

def github_commit_latest(URL):	
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, "html.parser")

	results = str(soup.find("div", id="repo-content-pjax-container"))
	start = results.find('href="') + len('href="')
	end = results.find('">', start)
	clean_url = URL[:len(URL)-len(URL.split('/')[len(URL.split('/'))-1])]
	commit = results[start:end].split('/')[len(results[start:end].split('/'))-1]
	url = clean_url+commit

# print(github_commit_latest(URL))

def get_commit_information