# Kreper Web Scraper Documentation

## Introduction

`Kreper` is a versatile web scraper designed to extract various elements from web pages, such as HTML tags, images, videos, audio, and metadata. It also includes features for crawling websites, saving extracted data in multiple formats (JSON, CSV, Excel), and downloading media files.

### Features

- Crawl web pages up to a specified depth
- Extract specific HTML tags, images, videos, audio, meta tags, and tables
- Search for specific text within a web page
- Download images and videos from web pages
- Save extracted data in JSON, CSV, or Excel formats
- Store the entire HTML of a page

---

## Installation

1. **Clone the Repository**  
   Download the source code to your local machine.

2. **Install Dependencies**  
   Ensure you have the Python libraries installed

## Usage

To use `Kreper`, run the script with the appropriate arguments.

### Command Line Options

- `-u`, `--url`  
**Description**: Target URL to scrape  
**Example**: `python kreper.py -u https://example.com`

- `--crawl`  
**Description**: Crawl the website  
**Example**: `python kreper.py -u https://example.com --crawl`

- `--depth`  
**Description**: Depth for crawling (default is 0)  
**Example**: `python kreper.py -u https://example.com --crawl --depth 2`

- `--limit`  
**Description**: Limit the number of pages to crawl (default is 100)  
**Example**: `python kreper.py -u https://example.com --crawl --limit 50`

- `--extract`  
**Description**: Extract specific HTML tags  
**Example**: `python kreper.py -u https://example.com --extract p h1 h2`

- `--extract-images`  
**Description**: Extract image URLs  
**Example**: `python kreper.py -u https://example.com --extract-images`

- `--extract-video`  
**Description**: Extract video URLs  
**Example**: `python kreper.py -u https://example.com --extract-video`

- `--extract-audio`  
**Description**: Extract audio URLs  
**Example**: `python kreper.py -u https://example.com --extract-audio`

- `--extract-meta`  
**Description**: Extract meta tags  
**Example**: `python kreper.py -u https://example.com --extract-meta`

- `--extract-table`  
**Description**: Extract tables  
**Example**: `python kreper.py -u https://example.com --extract-table`

- `--search-text`  
**Description**: Search for specific text on the web page  
**Example**: `python kreper.py -u https://example.com --search-text "Kreper"`

- `--output`  
**Description**: Specify the format to save extracted data (json, csv, xlsx)  
**Example**: `python kreper.py -u https://example.com --output json`

## Example Commands

1. **Crawl a website with a depth of 2 and limit of 50 pages**:
```bash
python kreper.py -u https://example.com --extract a span h1 h2 h3 --extract-images --download-images --media-path ./media_downloaded --crawl --limit 100 --depth 3
```
