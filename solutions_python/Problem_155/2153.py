#!/bin/python

# Runs on Python 2.7

from sys import stdin

def nextLine():
    return stdin.readline().strip()

for i in xrange(int(nextLine())):
    levels = [int(count) for count in list(nextLine().split(' ')[1])]

    extra = 0
    standing = 0

    for j, count in enumerate(levels):
        needed = max(j - standing, 0)
        extra += needed
        standing += needed + count

    print "Case #{}: {}".format(i+1, extra)