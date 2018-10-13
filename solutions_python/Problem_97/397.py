#!/usr/bin/python
import sys

def numPairs(A,B):
    res = 0
    seen = set()
    for x in xrange(A,B+1):
        s = str(x)
        orig = int(s)
        l = len(s)
        for i in xrange(l-1):
            s = s[1:] + s[0]
            if s[0]=='0': continue
            n = int(s)
            if n==orig: continue
            if n<A or n>B: continue
            frz = frozenset([s,orig])
            if frz not in seen:
                res = res+1
                seen.add(frz)
    return res/2



T = int(sys.stdin.readline())
for i in xrange(T):
    params = [int(x) for x in sys.stdin.readline().split()]
    print 'Case #%d: %d' % (i+1,numPairs(params[0],params[1]))



