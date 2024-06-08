from bs4 import BeautifulSoup

import requests

class Scraper:
  def __init__(self, params={}):
    self.language_code = 'en'
    self.headers = {
      # change as needed
      'User-Agent': 'Random User Agent'
    }
    self.params = params
    
  def make_request(self, url: str):
    response = requests.get(url, headers=self.headers, params=self.params)
    if not response.ok:
      print("Request failed")
    soup = BeautifulSoup(response.content, 'html.parser')
    for links in soup.findAll('a'):
      print(links)
    return response
    
def main():
  url = 'https://en.wikipedia.org/wiki/Lists_of_prepared_foods'
  scraper = Scraper()
  
  
  scraper.make_request(url)

if __name__ == "__main__":
  main()
