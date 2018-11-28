#!/usr/bin/python

import sys

def inside(a, b):
    for i, x in enumerate(a):
        if (i >= len(b) or x != b[i]):
            return i
    return len(a)

T = int(sys.stdin.readline())
for t in xrange(T):
    N, M = [int(x) for x in sys.stdin.readline().split()]

    already = []
    for i in xrange(N):
        already.append(sys.stdin.readline()[:-1].split("/")[1:])

    s = 0
    for i in xrange(M):
        d = sys.stdin.readline()[:-1].split("/")[1:]
        best = 0;
        for a in already:
            n = inside(d, a)
            best = max(n, best)
#            print d, a, n
#        print len(d) - best
        s += len(d) - best
        already.append(d)

    print "Case #%d: %d" % (t+1, s)
