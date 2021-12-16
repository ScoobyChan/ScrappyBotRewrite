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
	return (commit, url)

def get_commit_information(URL):
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, "html.parser")
	results = soup.find("div", class_="js-diff-progressive-container")

	###  Gets Names and Diff ID's  ###
	m = re.findall('.*data-tagsearch-path="(.*)".*', str(results))
	
	files = []
	
	for i in m: 
		m_list = i.split('" id="')
		files.append(m_list)

	# Check the commit
	# for f, d in files:
	# 	print(f, d)
	
	##  Line Additions | Deletions
	results = soup.find("div", class_="toc-diff-stats")
	line_changes = re.findall('.*<strong>(.*) .*', str(results))
	
	###  Amount of files changes
	file_changes = re.findall('''.\n *(.*) changed.*''', str(results))[0]
	
	return (file_changes, line_changes, files)

commit, url = github_commit_latest(URL)
get_commit_information(url)