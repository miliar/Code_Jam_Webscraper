#!/usr/bin/env python
from sys import stdin, stdout
from itertools import *

def answer(data):
    data, n, m = data
    
    rmax = [max(r) for r in data]
    cmax = []
    for cn in range(m):
        cmax.append(max(data[rn][cn] for rn in range(n)))

    for rn in range(n):
        for cn in range(m):
            v = data[rn][cn]
            if v < rmax[rn] and v < cmax[cn]:
                return "NO"

    return "YES"

def cases(s):
    while 1:
        n,m = map(int, next(s).rstrip().split())
        data = [ map(int, next(s).rstrip().split()) for x in range(n) ]
        yield (data, n, m)

if __name__ == '__main__':
    stdin.next()
    for n,case in enumerate(cases(stdin)):
        print "Case #%d: %s" % (n+1, answer(case))
