#!/bin/python
#import sys
#sys.stdin = file("sample.in")

from itertools import combinations

def readint(): return int(raw_input())

def readints(): return [ int(x) for x in raw_input().split() ]

def iscross(a,b):
    return (a[0]-b[0])*(a[1]-b[1]) <= 0

def solve(ropes):
    return sum(1 for a,b in combinations(ropes,2) if iscross(a,b))

if __name__ == "__main__":
    nt = readint()
    for i in range(nt):
        N = readint()
        ropes = [ readints() for _ in range(N) ]
        print "Case #%d: %s" % ( i+1, solve(ropes))
