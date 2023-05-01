import requests 
import bs4
url= "https://www.mlb.com/stats/team/batting-average/2022"
response= requests.get (url) 

soup = bs4.BeautifulSoup(response.text) 

pretty_html_string = soup.prettify ()

with open ("think_python_chapter1.html","w") as f:
    f.write (pretty_html_string)