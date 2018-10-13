#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
   
def calc(a, word):
    count = 0
    for i in range(0, len(a)-len(word)+1):
        if "".join(a[i:len(word)+i]) == word:
            count += 1
    return count

sum1 = 0
max1 = 0

def solve(keys, word, s):
    global max1, sum1
    a = [None]*s
    sum1 = 0
    max1 = 0

    def go(i):
        global sum1, max1
        if i == s:
            count = calc(a, word)
            # print "a, count", a,count
            sum1 += count
            max1 = max(max1, count)
            return
        for x in keys:
            a[i] = x
            go(i+1)
        pass
    go(0)

    return max1 - (sum1+0.0)/pow(len(keys), s)

def sp(*a):
    assert solve(*a[:-1]) == a[-1]
def test():
    assert calc('AA', 'A') == 2
    assert calc('AA', 'AA') == 1
    assert calc('AAA', 'AA') == 2
    assert calc('GO', 'GO') == 1

    assert solve('GOOGLE', 'GO', 2) == 1
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
        k, l, s = readInts()
        k, = readStrs()
        l, = readStrs()
        print 'Case #%d: %.8f' % (i+1, solve(k, l, s))
    pass

if __name__ == '__main__':
    main()