import requests
from bs4 import BeautifulSoup

# establish the target URL or URL's
url = "https://www.yelp.com/search?find_desc=&find_loc=San+Francisco%2C+CA&ns=1"

# utilize the request get method to get the target url page
yelp_req = requests.get(url)

# use the beautifulsoup library to clean the html text from target site
yelp_soup = BeautifulSoup(yelp_req.text, 'html.parser')

# use the status_code method to from requests library to check for 200 connection
print(yelp_req.status_code)

# prints out raw HTML text from the target site
print(yelp_req.text)

# The beautifulsoup prettify method allows me to beautify the text extraction from target
print(yelp_soup.prettify())

# use methods to target specific element on a page
print(yelp_soup.title)

# use the find all method to target all iterations of a specific elements
print(yelp_soup.find_all('p'))

# build a loop to iterate through all the links on the target site
for link in yelp_soup.find_all('a'):
    print(link.get('href'))

# I can use the find method instead of find_all
