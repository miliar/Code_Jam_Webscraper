#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
   
def solve(a):
    if not a:
        return 0,0
    n = len(a)
    s = 0 
    maxInterval = 0
    for i in xrange(n-1):
        if a[i] > a[i+1]:
            eat = a[i] - a[i+1]
            s += eat
            maxInterval = max(maxInterval, eat)
    res1 = s
    # print maxInterval
    s = 0
    for i in xrange(n-1):
        s += min(a[i], maxInterval)
    return res1, s

def sp(*a):
    assert solve(*a[:-1]) == a[-1]
def test():
    sp([], (0, 0))
    sp([1], (0, 0))
    pass

def readInt():
    return int(sys.stdin.readline().strip())
    
def readInts():
    return [int(x) for x in sys.stdin.readline().strip().split()]

def readStrs():
    return [x for x in sys.stdin.readline().strip().split()]

def main():
    n = readInt()
    for i in xrange(n):
        _ = readInt()
        a = readInts()
        c, d = solve(a)
        print 'Case #%d: %s %s' % (i+1, c, d)
    pass

if __name__ == '__main__':
    main()