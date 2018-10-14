#!/bin/python
#import sys
#sys.stdin = file("sample.in")

def readint(): return int(raw_input())

def readints(): return [ int(x) for x in raw_input().split() ]

def GetNumRecycled(x,A,B):
    ret = []
    s = str(x)
    lens = len(s)
    for i in range(1,len(s)):
        t = s[i:]+s[:i]
        nt = int(t)
        if A <= x < nt <= B and len(t) == lens:
            ret.append(nt)
    return len(set(ret))

def solve(A,B):
    ret = 0
    for x in xrange(A,B+1):
        ret += GetNumRecycled(x, A, B)
    return ret

if __name__ == "__main__":
    nt = readint()
    for i in range(nt):
        A,B = tuple(readints())
        print "Case #%d: %s" % ( i+1, str(solve(A,B)))
