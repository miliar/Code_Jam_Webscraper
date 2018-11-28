#!/usr/bin/env python

from sys import stdin
from numpy import array, log2, floor, ceil


T = int(stdin.readline())

for t in range(T):
    print "Case #%d:" % (t+1),

    N, X = array(stdin.readline().split()).astype(int)
    S = array(stdin.readline().split()).astype(int)
    S.sort()

    #print N, X, S

    ret = 0
    start = 0
    end = len(S)-1
    while start < end:
        if S[end] + S[start] <= X:
            end -= 1
            start += 1
            ret += 1
        else:
            end -= 1
            ret += 1
            pass
        pass
    if start == end: ret += 1
    print ret
