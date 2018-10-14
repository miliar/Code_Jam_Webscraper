#!/usr/bin/env python

from sys import stdin, stderr
from numpy import array

T = int(stdin.readline())

def Solve(N):
    ns = []
    while N > 0:
        ns.append(N%10)
        N /= 10
        pass
    for i in range(1, len(ns)):
        if ns[i] <= ns[i-1]: continue
        ns[i] -= 1
        for j in range(i): ns[j] = 9
        pass
    ret = 0
    for i, d in enumerate(ns): ret += 10**i * d
    return ret

# for i in range(100):
#     print Solve('A' * 1000)
# exit(0)


for t in range(T):
    N = int(stdin.readline().strip())

    print "Case #%d:" % (t+1),
    #print N,
    print Solve(N)
