#!/usr/bin/python

from heapq import *

T = int(raw_input())
for c in range(1, T+1):
    N, K = map(int, raw_input().split())
    H = []

    def makeregion(l, r):
        minlr = (r - l - 1)/2
        maxlr = (r - l)/2
        return -minlr, -maxlr, l, r

    heappush(H, makeregion(0, N))
    for j in xrange(K):
        mi, ma, l, r = heappop(H)
        middle = l + (r - l - 1) / 2
        heappush(H, makeregion(l, middle))
        heappush(H, makeregion(middle+1, r))

    print "Case #%d: %d %d" % (c, -ma, -mi)

