import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import argparse

def extract_tags(url, tags):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    for tag in tags:
        print(f"\nExtracted {tag}s:")
        for i, extracted_tag in enumerate(soup.find_all(tag)):
            print(f"\n{tag} #{i+1}:")
            if tag.lower() == 'table':
                # Print table in a readable format
                table_data = [[cell.text.strip() for cell in row.find_all('td')] for row in extracted_tag.find_all('tr')]
                headers = [cell.text.strip() for cell in extracted_tag.find_all('th')]
                if headers:
                    print(tabulate(table_data, headers, tablefmt='grid'))
                else:
                    print(tabulate(table_data, tablefmt='grid'))
            else:
                # Print other tags
                print(extracted_tag.prettify())
    
def main():
    parser = argparse.ArgumentParser(description='Tag Extractor')
    parser.add_argument('url', type=str, help='Website URL to extract tags from')
    parser.add_argument('--tags', type=str, nargs='+', default=['form', 'table'], help='Tags to extract (space-separated)')
    
    args = parser.parse_args()
    extract_tags(args.url, args.tags)


if __name__ == "__main__":
    main()