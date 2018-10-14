#!/usr/bin/env python

from sys import stdin, stderr
from numpy import array

T = int(stdin.readline())

def equal(A, B):
    return ((A - B) / A)**2 < 1e-12

def Solve(N, V, X, ss):
    if N == 1:
        if not equal(X, ss[0][1]): return "IMPOSSIBLE"
        return V / ss[0][0]
    elif N == 2:
        if equal(ss[0][1], ss[1][1]):
            return Solve(1, V, X, [[ss[0][0]+ss[1][0], ss[0][1]]])
        if equal(ss[0][1], X):
            return V / ss[0][0]
        if equal(ss[1][1], X):
            return V / ss[1][0]
        if (ss[0][1] - X) * (ss[1][1] - X) > 0:
            return "IMPOSSIBLE"
        v0 = (X - ss[1][1]) / (ss[0][1] - ss[1][1]) * V
        v1 = V - v0
        return max(v0 / ss[0][0], v1 / ss[1][0])
    return "IMPOSSIBLE"


for t in range(T):
    N, V, X = [wd for wd in stdin.readline().split()]
    N = int(N)
    V = float(V)
    X = float(X)
    srcs = []
    for n in range(N):
        r, c = [float(wd) for wd in stdin.readline().split()]
        srcs.append(array([r, c]))
        pass

    print "Case #%d:" % (t+1),
    print Solve(N, V, X, srcs)
