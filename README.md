# README #

This repository contains the Federal Acquisition Regulation (FAR) language downloaded directly as HTML from https://www.acquisition.gov/browsefar

FAC Number/Effective Date:    2005-97 / 01-24-2018
 
# Running this file (parser.py) will:
- Scrape the contents of the downloaded HTML from the FAR website
- Parse the HTML using BeautifulSoup
- Create JSON files in the format for SpringCM .sxterm files from the individual regulations
- Save the .sxterm files into the FAR folder

# TO CREATE A FAR LIBRARY FROM THE TERMINAL
1. (If it doesn't exist), create a folder called FAR in the same folder as the other files
2. Start a simple server: python -m SimpleHTTPServer 8080
3. Execute the script: python parser.py