#!/usr/bin/env python
#-*-coding: utf-8 -*-

def readint(): return int(raw_input())
def readarray(f): return map(f, raw_input().split())

T = readint()

def flip(A, i, K):
    for j in range(i, i + K):
        A[j] = - A[j]

for t in range(T):
    S, K = readarray(str)
    S = [1 if s == '+' else -1 for s in S]
    K = int(K)
    n = 0
    for i in range(len(S) - K + 1):
        if S[i] == -1:
            flip(S, i, K)
            n += 1
    if sum(S) == len(S):
        print "Case #%d: %d" % (t + 1, n)
    else:
        print "Case #%d: %s" % (t + 1, 'IMPOSSIBLE')
