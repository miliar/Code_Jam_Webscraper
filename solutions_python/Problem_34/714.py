#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
                                
def parseQ(file='test'):
    f = open(file)
    line = f.readline()
    (L, D, N) = line.split(' ')

    words = []
    for i in range(int(D)):
        word = f.readline()
        word = word[:-1]
        words.append(word)

    for i in range(int(N)):
        word = f.readline()
        word = word[:-1]
        string = makeWords(word)
        m =  re.compile(string)
        j = 0
        for text in words:
            if(m.match(text) != None):
                j += 1

        print "Case #%d: %d" % (i + 1, j)

def makeWords(word):
    string = ""
    cnt = 0
    for text in word:
        if text == '(':
            cnt = 1
            string = "%s(" % (string)
            continue
        if text == ')':
            cnt = 0
            string = "%s)" % (string)
            continue
        if cnt == 1:
            string = "%s%s" %(string, text)
            cnt = 2
            continue
        if cnt == 2:
            string = "%s|%s" % (string, text)
            continue
        if cnt == 0:
            string = "%s%s" % (string, text)
    return string

if __name__ == '__main__':
    parseQ(sys.argv[1])
