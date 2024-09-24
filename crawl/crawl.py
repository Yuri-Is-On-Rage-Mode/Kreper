import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import argparse

def crawl_website(url, depth, current_depth=0, visited=None):
    if visited is None:
        visited = set()
    
    if current_depth > depth:
        return
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")
        return
    
    visited.add(url)
    print(f"Crawling: {url} (Depth: {current_depth})")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.find_all('a', href=True):
        href = link['href']
        # Join relative URLs with base URL
        if not bool(urlparse(href).netloc):
            href = urljoin(url, href)
        
        # Skip links that are not HTTP or HTTPS
        if urlparse(href).scheme not in ['http', 'https']:
            continue
        
        # Skip already visited links
        if href in visited:
            continue
        
        crawl_website(href, depth, current_depth + 1, visited)


def main():
    parser = argparse.ArgumentParser(description='Website Crawler')
    parser.add_argument('url', type=str, help='Website URL to crawl')
    parser.add_argument('--depth', type=int, default=1, help='Crawling depth')
    
    args = parser.parse_args()
    crawl_website(args.url, args.depth)


if __name__ == "__main__":
    main()