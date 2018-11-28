#!/usr/bin/python

import sys, math

def readints(f):
    return [int(s) for s in f.readline().split()]

def readint(f):
    return int(f.readline())

def pal(p):
    s = str(p)
    for i in xrange(len(s)/2):
        if s[i] != s[-(i+1)]:
            return False
    return True

def count(a, b):
    start = int(math.floor(pow(a, 0.5)))
    end = int(math.ceil(pow(b, 0.5)))
    count = 0
    for t in xrange(start, end+1):
        if not pal(t):
            continue
        p = t*t
        if p >= a and p <= b and pal(p):
            count += 1
    return count

if __name__ == "__main__":
    f = open(sys.argv[1], "r")
    numCases = readint(f)
    for i in xrange(numCases):
        print "Case #%d:" % (i + 1),
        a, b = readints(f)
        print count(a, b)
