# Indian Express News Scraper

This Python script scrapes the latest news articles from the Indian Express website and saves the information in a text file. The information includes the news title, description, date, and article URL.

## Features
- Scrapes the latest news articles from Indian Express.
- Extracts the news title, description, date, and article URL.
- Saves the extracted information into a text file (`OutPut.txt`).
- Handles multiple pages of news articles.

## Requirements
- Python 3.x
- `requests` library
- `re` library

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/maruthachalams/Indian-Express-News-Scraper.git
    cd news-scraper
    ```
2. Install the required libraries:
    ```sh
    pip install requests
    ```

## Usage
1. Run the script:
    ```sh
    python scraper.py
    ```
2. The output will be saved in a file named `OutPut.txt`.

## Code Explanation
### `single_regex(pattern, target_string)`
This function uses regular expressions to find matches in a target string and returns the first match found.

### `get_response(url)`
This function makes an HTTP GET request to a given URL, prints the response status code, and writes the content of the response to a file (`Result_page.html`). It also returns the response content.

### Main Script
1. Initializes an output string with headers ("News_Title\tDescription\tDate\tArticle_URL\n") and writes it to the `OutPut.txt` file.
2. Fetches the content of the main URL ("https://indianexpress.com/latest-news/") and stores it in the `content` variable.
3. Uses regular expressions to find the total number of pages (`PN`). If no page number is found, it defaults to 1.
4. Loops through each page (from 1 to `PN`) and fetches the content of each page.
5. Extracts news blocks from the page content and cleans up special characters.
6. Extracts the news title, description, date, and article URL using regular expressions.
7. Appends the extracted information to the `OutPut.txt` file.
8. Prints the current page count and continues to the next page until all pages are processed.
9. Prints "Completed" when all pages have been processed.


