#!/usr/bin/env python

for nnn in xrange(1, int(raw_input())+1):
    print "Case #%d:" % (nnn),
    D, N = [int(x) for x in raw_input().split()]
    T = 0
    for i in xrange(N):
        K, S = [int(x) for x in raw_input().split()]
        tmp = (D-K)/float(S)
        T = tmp if tmp > T else T
    print D/float(T)
