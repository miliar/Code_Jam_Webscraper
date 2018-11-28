#!/usr/local/bin/python

from sys import stdin
import re


def Run():
    L, D, N = stdin.readline().split()
    L, D, N = eval(L), eval(D), eval(N)

    words = []

    for i in range(D):
        words.append(stdin.readline().rstrip())

    #for w in words:
        #print w

    patterns = []

    for i in range(N):
        patterns.append(stdin.readline().rstrip())

    #for p in patterns:
        #print p

    for i in range(N):
        RunTestCase(i, words, patterns[i])


def RunTestCase(index, words, pattern):
    pattern = pattern.replace('(', '[').replace(')', ']')
    m = re.compile(pattern) 

    numMatches = 0

    for word in words:
        if m.search(word):
            numMatches = numMatches + 1

    print "Case #%d: %d" % (index + 1, numMatches)


if __name__ == "__main__":
    Run()
