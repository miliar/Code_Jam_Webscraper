#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
   
def solve(r, c, w):
    assert r == 1
    def f(x):
        if x == w:
            return w
        elif x < w:
            return 0
        return max(f(x-w)+1, w+1)
    return f(c)

def sp(*a):
    assert solve(*a[:-1]) == a[-1]
def test():
    sp(1, 5, 1, 5)
    sp(1, 2, 2,2)
    sp(1, 3, 2,3)
    sp(1, 4, 2,3)
    sp(1, 5, 2,4)
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
        r, c, w = readInts()
        # print c, w
        print 'Case #%d: %s' % (i+1, solve(r, c, w))
    pass

if __name__ == '__main__':
    main()