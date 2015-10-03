import os
import sys
from textblob import TextBlob

## Returns a dictonary of polarity values of each document in the directory
def get_polarity(path) :
    dict = {}
    some_path = path      
    os.chdir(some_path)
    text_files = [f for f in os.listdir(some_path) if f.endswith('_NS.txt')]
    for f1 in text_files:
        f = open(f1,'r')
        file_content = f.read()
        file_content = unicode(file_content,'utf-8')
        document = TextBlob(f.read())
        dict[f1] = document.sentiment.polarity
        f.close()
    return dict

if __name__ == '__main__':
    d = get_polarity("C:/VideoTranscript")
    for k,v in d.items():
        print k
        print v
        
        #f = open(fl,'r')
    
    

