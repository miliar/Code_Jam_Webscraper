#!/usr/bin/env python

import sys
import string

filename = sys.argv[-1]

file = open(filename)
ldn = file.readline()
l = int(ldn.split(" ")[0])
d = int(ldn.split(" ")[1])
n = int(ldn.split(" ")[2])

words = []
for i in range(d):
    word = file.readline()[0:l]
    words.append(word)

def word_has_char(word, char):
    for i in word:
        if i == char:
            return True
    return False

def pattern_match(pattern, word):
    groups = []
    while len(pattern) > 0:
        char = pattern[0]
        pattern = pattern[1:]
        if char == '(':
            groups.append([])
            
            char = pattern[0]
            pattern = pattern[1:]
            while char != ')':
                groups[-1].append(char)
                char = pattern[0]
                pattern = pattern[1:]
        else:
            groups.append(char)

    for i in range(len(groups)):
        if not word_has_char(groups[i],word[i]):
            return False
    return True

for i in range(1,n+1):
    pattern = file.readline()[:-1]
    k = 0
    for word in words:
        if pattern_match(pattern, word):
            k += 1
    
    print "Case #%d: %d" % (i, k)
