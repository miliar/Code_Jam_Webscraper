#!/usr/bin/python

import sys

def matches(word, pattern):
    if len(word) != len(pattern):
        return False
    for index in xrange(0, len(word)):
        if pattern[index].find(word[index]) < 0:
            return False
    return True
        

def countMatches(words, pattern):
    s = 0
    for word in words:
        if matches(word, pattern):
            s += 1
    return s

if __name__ == "__main__":
    fin = open(sys.argv[1], "r")
    l, d, n = map(int, fin.readline().split(" "))

    words = []
    for i in range(0 ,d):
        words += [fin.readline().strip()]

    for i in range(1, n+1):
        pattern = []
        unparsed = fin.readline().strip()
        grouped = False
        group = ""
        for c in unparsed:
            if not grouped and c == "(":
                group = ""
                grouped = True
            elif grouped and c == ")":
                pattern += [group]
                grouped = False
            elif grouped:
                group += c
            else:
                pattern += [c]

        print "Case #%d: %d" % (i, countMatches(words, pattern))
