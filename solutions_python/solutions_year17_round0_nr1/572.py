#!/usr/bin/env python

from sys import stdin, stderr
from numpy import array

T = int(stdin.readline())

def Solve(S, K):
    count = 0
    d = array([1] * len(S))
    for i in range(len(S)):
        if S[i] == '-': d[i] = -1
        pass
    for i in range(len(S)-K+1):
        if d[i] == -1:
            d[i:i+K] *= -1
            count += 1
        pass
    if sum(d[-K:]) != K: return 'IMPOSSIBLE'
    return count

# for i in range(100):
#     print Solve('A' * 1000)
# exit(0)


for t in range(T):
    S, K = stdin.readline().split()
    K = int(K)

    print "Case #%d:" % (t+1),
    print Solve(S, K)
