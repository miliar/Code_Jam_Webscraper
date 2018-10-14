#!/bin/python
#import sys
#sys.stdin = file("sample.in")

def readint(): return int(raw_input())

def readints(): return [ int(x) for x in raw_input().split() ]

def orop(cs):
    ret = 0
    for c in cs:
        ret = ret ^ c
    return ret

def solve(cs):
    ors = orop(cs)
    if ors != 0:
        return "NO"
    cs.remove(min(cs))
    return sum(cs)

if __name__ == "__main__":
    nt = readint()
    for i in range(nt):
        nc = readint()
        cs = readints()
        print "Case #%d: %s" % ( i+1, str(solve(cs)))
