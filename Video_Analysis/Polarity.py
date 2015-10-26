#!/usr/bin/python
import utils
import sys
from textblob import TextBlob

dictonary_original = {}
dictonary_modified = {}


## Returns a dictonary of polarity values of each document in the directory
def get_polarity_of_original_files(path):    
    reload(sys)
    list_of_files = utils.get_files(path)
    for f1 in list_of_files:
        f = open(f1,'r')
        file_content = f.read()
        original_encoded_file_content = unicode(file_content,'utf-8')
        document = TextBlob(original_encoded_file_content)
        dictonary_original[f1] = document.sentiment.polarity
        f.close()
        
def get_polarity_of_modified_files(path):
    reload(sys)
    list_of_files = utils.get_files(path)
    for f1 in list_of_files:
        #print f1
        key = f1
        value = utils.convert_doc(path+"/"+f1)
        dictonary_modified[key] = value

    
if __name__ == '__main__':
    get_polarity_of_original_files("/home/manish/VideoTranscript")
    for k,v in dictonary_original.items():
        print k,v
        
    print "Now the modified one"
    get_polarity_of_modified_files("/home/manish/VideoTranscript")
    for k,v in dictonary_modified.items():
        print k,v
