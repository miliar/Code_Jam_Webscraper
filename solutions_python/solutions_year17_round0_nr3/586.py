#!/usr/bin/env python

from sys import stdin, stderr
from math import log, floor

T = int(stdin.readline())

def Solve(N, K):
    K1 = int(floor(log(K+1)/log(2)))
    K2 = K - 2**K1 + 1
    if K2 == 0:
        K1 -= 1
        K2 = K - 2**K1 + 1
        pass
    #print K1, K2
    part = 2**K1
    part_size = (N+1) / part - 1
    big_part = N+1 - (part_size+1) * part
    if K2 <= big_part: part_size += 1
    return (part_size) / 2, (part_size-1) / 2

# for i in range(100):
#     print Solve('A' * 1000)
# exit(0)


for t in range(T):
    N, K = (int(s) for s in stdin.readline().split())

    print "Case #%d:" % (t+1),
    ret = Solve(N, K)
    print ret[0], ret[1]
