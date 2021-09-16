# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import uuid
import codecs
import sys
import csv

def parseLanguage():

    rowTitle = ''
    rowContent = ''
    rowNotes = ''
    json = '['

    row_count = len(list(csv.reader(open('sampleCSV.csv'))))


    with open('sampleCSV.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            print(row_count)
            rowContent = row[0]
            rowTitle = row[1]
            rowNotes = row[2]
            json = json + '{"Content": "'+rowContent+'", "Name": "' + rowTitle + '", "Notes": "' + rowNotes + '", "Uid":"'+str(uuid.uuid4())+'"}'
            print(json)
            if row_count > 1:
                json = json + ','
                row_count = row_count - 1   

    json = json + ']'

    location = 'CSV/'

    filename = location + 'sampleCSV.sxterm'

    fhand = codecs.open(filename,'w', "utf-8")
    fhand.write(json)
    
reload(sys)
# print sys.setdefaultencoding('Cp1252')

parseLanguage()


