# Note - this code must run in Python 3.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib.request
import uuid
import re
import codecs
import sys
import logging
from importlib import reload
import json as dumper
from bs4 import BeautifulSoup
from markupsafe import Markup, escape

# This repository contains the Federal Acquisition Regulation (FAR) language downloaded directly as HTML from https://www.acquisition.gov/browsefar
# FAC Number/Effective Date:    2005-97 / 01-24-2018
#
# Running this file (parser.py) will:
# - Scrape the contents of the downloaded HTML from the FAR website
# - Parse the HTML using BeautifulSoup
# - Create JSON files in the format for SpringCM .sxterm files from the individual regulations
# - Save the .sxterm files into the FAR folder
#
# To run this file,

def readHTMLdoc():
    # url = 'http://0.0.0.0:8080/DFARSHTML/index.html'
    url = 'http://0.0.0.0:8080/FARHTML/Part_52.html'
    logging.warning(url)
    with urllib.request.urlopen(url) as response:
        html = response.read()
    # html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html)

    findLinks(soup)

def remove_html_markup(s):
    tag = False
    quote = False
    out = ""

    for c in s:
        if c == '<' and not quote:
            tag = True
        elif c == '>' and not quote:
            tag = False
        elif (c == '"' or c == "'") and tag:
            quote = not quote
        elif not tag:
            out = out + c

    return out

def findLinks(soup):
    tags = soup('a')
    for tag in tags:
        href = tag.get('href', None)
        # if href != None and "Subpart" in href:
        if href != None:
            # url = 'http://0.0.0.0:8080/DFARSHTML/'+href
            url = 'http://0.0.0.0:8080/FARHTML/'+href
            parseLanguage(url)

def parseLanguage(url):
    print("=====")
    print("=====")
    print(url)
    print("=====")
    print("=====")
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    subpartTitle = soup.title.text
    subpartTitle = re.sub('[. ]', '_', subpartTitle)

    thisName = ''
    thisContent = ''

    thisName = soup.find("h1")
    thisContent = soup.find('div', {'class': 'body'})

    # print(len(thisName))
    print("------")
    # print(len(thisContent))
    # print(thisContent)
    if len(thisName)>0:
        thisName = Markup(thisName.text).striptags()
        thisName = thisName.replace("\"", " ")
        thisName = thisName.replace("\n", " ")

        if thisContent:
            print('HERE')
            thisContent = Markup(thisContent.text).striptags()
            thisContent = thisContent.replace("\"", " ")
            thisContent = thisContent.replace("\n", " ")

            # thisContent = str(thisContent.escape(u'<a>b</a>'))
            # print(thisContent)
            # thisContent = remove_html_markup(thisContent.text.encode("utf-8"))

            # json = '[{"Content": "'+thisContent+'", "Name": "' + thisName + '", "Notes":"", "Uid":"'+str(uuid.uuid4())+'"}]'
            json = '[{"Name": "' + thisName + '", "Content": "' + thisContent + '", "Notes":"", "Uid":"'+str(uuid.uuid4())+'"}]'
            location = 'FAR/'

            filename = location + subpartTitle.strip() + '.sxterm'

            with open(filename, "w", encoding="utf-8") as f:
                f.write(json)

            # fhand = codecs.open(filename,'w', "Cp1252")
            # fhand.write(json)
        else:
            thisContent = ''


    # for tag in elements:
    #     if tag.name == 'h3':
    #         regContent = dumper.dumps(regContent)

    #         regTitle = tag.text.encode("utf-8")
    #         regTitle = str.strip(tag.text)

    #         json = json + '{"Content": '+regContent+', "Name": "' + regTitle + '", "Notes":"", "Uid":"'+str(uuid.uuid4())+'"}'
    #         if counter > 1:
    #             json = json + ','
    #         regContent = ''
    #         counter = counter - 1
    #     else:
    #         # thisContent = tag
    #         # print(tag.content)
    #         # thisContent = tag.prettify(formatter="minimal")

    #         regContent = tag.text.encode("utf-8")
    #         regContent = str.strip(tag.text)
    #         # thisContent = tag.encode(encoding='utf-8', indent_level=None, formatter='html', errors='xmlcharrefreplace')
    #         # print(thisContent)
    #         # regContent = regContent + thisContent




# reload(sys)
# print sys.setdefaultencoding('Cp1252')
readHTMLdoc()


