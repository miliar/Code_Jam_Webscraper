#!/bin/python

import sys

table = {}

def count(item, text):
    if table.has_key((item, text)):
        return table[(item, text)]
    
    if len(item) == 1:
        c = text.count(item)
        table[(item, text)] = c
        return c
    elif len(text) == 0:
        table[(item, text)] = 0
        return 0

    currentSum = 0
    for index in xrange(0, len(text)):
        if text[index] == item[0]:
            currentSum += count(item[1:], text[index+1:])

    table[(item, text)] = currentSum
    return currentSum

fin = open(sys.argv[1], "r")
n = int(fin.readline())
for i in xrange(0, n):
    print "Case #%d: %s" % (i+1, str(count("welcome to code jam", fin.readline()))[-4:].zfill(4))
