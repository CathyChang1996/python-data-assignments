import requests

#Read all the .txt files in folder assignment0/
content = []
for i in range(1,6):
    url="https://raw.githubusercontent.com/hupili/python-for-data-and-media-communication-gitbook/master/assets/assignment0/trade-wars-news{}.txt".format(i)
    s=requests.get(url).text
    content.append(s)
    
import string
without_punc = []  #remove all punctuations in the texts
for elements in content:
    table = str.maketrans({key: None for key in string.punctuation})
    new_s = elements.translate(table) 
    without_punc.append(new_s)

import nltk  # To clean the data and remove the stop words, I googled the solution and found NLTK(Natural Language Toolkit) in python 
nltk.download('punkt')
from nltk.corpus import stopwords 
en_stops = set(stopwords.words('english'))

filtered_data = []
lower_data = [] #lower the words in the texts
for w in without_punc: 
    lower = str.lower(w)
    lower_data.append(lower)
    
split_words = []
for elements in lower_data: # split the string
    splited = str.split(elements) 
    split_words.append(splited)

for elements in split_words: # remove stop words
    for w in elements:
        if w not in en_stops:
            filtered_data.append(w)

without_stopwords = []
stop_words = ['also', 'would', 'us', 'said'] #enrich this stop_words list to make the output more meaningful
for w in filtered_data:
    if w not in stop_words:
        without_stopwords.append(w)

dict = {}
for word in without_stopwords:
    dict[word] = without_stopwords.count(word)#For every word extracted above, count how many times each one appears.
    #print(dict)
    frequency = sorted(dict.items(), key=lambda d: d[1], reverse = True) # arrange the words frequency in ascending order
    #print(frequency)
import csv
with open('assignment0.csv','w') as f: #Output the full keyword frequency list into a CSV file
    writer = csv.writer(f)
    header = ['keyword','frequency']
    writer.writerow(header)
    writer.writerows(frequency[:15])  
