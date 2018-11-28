#!/bin/python
#import sys
#sys.stdin = file("sample.in")

def readint(): return int(raw_input())

def readints(): return [ int(x) for x in raw_input().split() ]

def suprised(avg, n):
    if n == 0:
        if 1 <= avg:
            return 1
        else:
            return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2

def normalmax(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1

def calctype(p, score):
    m = score % 3
    avg = (score-m)/3
    nmax = avg + normalmax(m)
    if p <= nmax:
        return 0
    best = avg + suprised(avg,m)
    if p <= best:
        return 1
    return 2

def solve(n,s,p,scores):
    types = [calctype(p,n) for n in scores]

    avgover = len([x for x in types if x == 0])
    bestover = len([x for x in types if x == 1])
    
    return avgover + min(bestover, s)

if __name__ == "__main__":
    nt = readint()
    for i in range(nt):
        ints = readints()
        n = ints[0]
        s = ints[1]
        p = ints[2]
        scores = ints[3:]
        print "Case #%d: %s" % ( i+1, str(solve(n,s,p,scores)))
