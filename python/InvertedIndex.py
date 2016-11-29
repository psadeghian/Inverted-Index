#! /usr/bin/python3

from sys import stdin
import re, sys


file_path = sys.argv[1].strip()
# note the first argument is the 'file_name.py'
file = open(file_path, "r")

index = {}
for line in file:
    doc_id, content = line.split('\t')

    words = re.findall(r'\w+', content)

    for word in words:
            word = word.lower()
            if index.get(word) is None:
                index.setdefault(word, {})
                index[word].setdefault(doc_id, 1)

            elif index[word].get(doc_id) is None:
                index[word].setdefault(doc_id, 1)

            else:
                count = index[word][doc_id] + 1
                index[word][doc_id] = count
file.close()

file_path = sys.argv[2].strip()
file = open(file_path, "w")
word_list = index.keys()
for word in word_list:
    line = word + ": "
    for doc_id in index[word].keys():
        line = line + doc_id + ":" + str(index[word][doc_id]) + " "
    print(line, file=file)
file.close()
