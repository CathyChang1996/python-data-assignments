import os # I found this module on the Internet, and I downloaded all the text files to my local path
myFiles = ['trade-wars-news1.txt', 'trade-wars-news2.txt', 'trade-wars-news3.txt', 'trade-wars-news4.txt', 'trade-wars-news5.txt']
articles = []
for filename in myFiles:
    os.path.join('/Users/cathychang/desktop/friday/assignment0', filename)
    article = os.path.join('/Users/cathychang/desktop/friday/assignment0', filename)
    articles.append(article)
#print(articles)
my_data = []
for i in articles:
    data = open(i).read() #assemble the content of all 5 files and append them in a list
    my_data.append(data)
#print(my_data)
split_words = []
for elements in my_data:
    splited = str.split(elements) 
    split_words.append(splited)
#print(split_words)

import nltk  # To clean the data and remove the stop words, I googled the solution and found NLTK(Natural Language Toolkit) in python 
nltk.download('punkt')
from nltk.corpus import stopwords 
en_stops = set(stopwords.words('english'))

filtered_data = [] #put the filtered words in a list
for elements in split_words:
    for word in elements: 
        lower = str.lower(word)
        if lower not in en_stops:
            #print(word)
            filtered_data.append(lower)

import csv
dict = {}
for w in filtered_data:
    dict[w] = filtered_data.count(w)#For every word extracted above, count how many times each one appears.
    #print(dict)
    frequency = sorted(dict.items(), key=lambda d: d[1], reverse = True) # arrange the words frequency in ascending order
    #print(frequency)
    with open('assignment0.csv','w') as f:
        writer = csv.writer(f)
        header = ['keyword','frequency']
        writer.writerow(header)
        writer.writerows(frequency[:15])           
   