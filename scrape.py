import requests
import urllib3
import requests.packages
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


url = "https://www.ansa.it"

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find("meta",  attrs={'name': 'title'} )
description = soup.find("meta",   attrs={'name': 'description'} )
keywords = soup.find("meta",   attrs={'name': 'keywords'} )

url = soup.find("meta",  property="og:url")
site_name = soup.find("meta",  property="og:site_name")

print(title["content"] if title else "No meta title given")
print(description["content"] if description else "No meta description given")
print(keywords["content"] if keywords else "No meta description given")
print(url["content"] if url else "No meta url given")
print(site_name["content"] if site_name else "No meta site_name given")

