#!/usr/bin/env python

import pickle

dictionary_file = open("googlerese.dict")
dictionary = pickle.load(dictionary_file)
dictionary_file.close()

dictionary[' '] = ' '

n = int(raw_input())

for i in xrange(n):
    googlerese= raw_input()
    english = []
    for c in googlerese:
        english.append(dictionary[c])

    english = ''.join(english)

    print "Case #%s: %s" % (i + 1, english)
