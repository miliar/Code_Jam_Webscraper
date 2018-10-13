#! /usr/bin/python2.7
# coding: utf-8

import sys
sys.setrecursionlimit(1000000)
def pretty(lst):
    d = {}
    for n in lst:
        d[n] = d[n]+1 if n in d else 1
    print '   ',
    for n in sorted(d, reverse=True):
        print '%4d: %d, ' % (n,d[n]),
    print


cache={}
def recurs(ps, nsplit=0):
    global cache
    #print ps
    ps = tuple(sorted(ps, reverse=True))
    if ps in cache:
        return cache[ps]+nsplit

    a = max(ps) + nsplit
    #print 'a:',a
    for i in xrange(1, ps[0]//2 + 1):
        b = recurs((i, ps[0] - i) + ps[1:], nsplit + 1)
        a = min(a, b)

    cache[ps] = a
    return a
    
    

for t in xrange(input()):
    d = input()
    ps = map(int, raw_input().split())
    ps = tuple(ps)

    cache = {}
    print 'Case #%d: %d' % (t + 1, recurs(ps))
