import sys
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_page(url):
  try:
    response = requests.get(url)
    response.raise_for_status()
  except requests.exceptions.RequestException as e:
    print(f"Error fetching {url}: {e}")
    return None
  
  return response.text

def save_page(url, content):
  filename = f"{url.replace('https://', '').replace('http://', '').replace('/', '_')}.html"
  with open(filename, 'w') as file:
    file.write(content)
  print(f"Saved {url} to {filename}")

def print_metadata(url, content):
  soup = BeautifulSoup(content, 'html.parser')
  num_links = len(soup.find_all('a'))
  num_images = len(soup.find_all('img'))
  last_fetch = datetime.now().strftime('%a %b %d %Y %H:%M UTC')

  print(f"site: {url}")
  print(f"num_links: {num_links}")
  print(f"images: {num_images}")
  print(f"last_fetch: {last_fetch}")

def main():

  if len(sys.argv) < 2:
    print("Usage: python fetch.py [URL] [URL]")
    return
  
  for url in sys.argv[1:]:
    content = fetch_page(url)
    if content:
      save_page(url, content)
      print_metadata(url, content)

if __name__ == "__main__":
  main()
  