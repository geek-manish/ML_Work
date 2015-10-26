#!/usr/bin/python
import os
from textblob.blob import Word, TextBlob
import enchant

dictionary = enchant.Dict("en_US")

def get_files(path):
    some_path = path      
    os.chdir(some_path)
    text_files = [f for f in os.listdir(some_path) if not (f.endswith('_NS.txt'))]
    text_files = [f for f in text_files if (f.endswith('txt'))] 
                     
    return text_files

def correct_word_replacer(str):

    length = len(str)
    i = 0
    j = 1
    intermediate_string = ""
    while j<=length:
        if dictionary.check(str[i:j]):
            if len(str[i:j]) == 1:
                j = j+1
                continue
            intermediate_string = intermediate_string+str[i:j]+" "
            i = j
            j = i + 1
        else:
            j = j+1
    #print intermediate_string        
    return intermediate_string

def convert_doc(file_path):
    array = []
    out_string = ""
    with open(file_path, "r") as ins:
        for line in ins:
            array.append(line)
            for word in line.split(" "):
                #print word
                word1 = unicode(word,'utf-8')
                #print word1
                if dictionary.check(word1):
                    out_string = out_string+word1
                    out_string = out_string+" "
                else:
                    returned_word = correct_word_replacer(word1)
                    out_string = out_string+returned_word
                    out_string = out_string+" "
                #out_string = out_string+"."   
        ins.close()
    #print out_string
    #out_string = unicode(out_string,'utf-8')
    new_blob = TextBlob(out_string)
    return new_blob.sentiment.polarity
    
#if __name__ == '__main__':
    #print "in main"
    #f1 = "/home/manish/VideoTranscript/1b4-R6NjZOA.txt"
    #f = open(f1,'r')
    #file_content = f.read()
    #doc_content = unicode(file_content,'utf-8')
    #doc = TextBlob(doc_content)
    #words_in_doc(doc)
    #path = "/home/manish/VideoTranscript"
    #file_name = "Non Linear Systems.txt"
    #x = convert_doc(path+"/"+file_name)
    #print x    
