#!/usr/bin/env python
# encoding: utf-8

import sys

def solve(B, N, K):
    D = [N, N+1, N-1, -N, -N-1, -N+1, +1, -1]
    l = len(B)
    R = {'B': False, 'R': False}
    
    for i in xrange(0, l):
        if B[i] and not R[B[i]]:
            for d in D:
                j = 1
                while B[i+j*d] == B[i]: 
                    j += 1
                if j >= K:
                    R[B[i]] = True

    return R['B'], R['R']

def norm(l):
    i = 0
    c = 0
    while i<len(l):
        if l[i] == '.':
            del l[i]
            c += 1
        else:
            i += 1
    return [None] * c + l

M = {
    (False, False): "Neither",
    (True, True): "Both",
    (True, False): "Blue",
    (False, True): "Red"
}
    
T = int(sys.stdin.readline())
for i in xrange(1, T+1):
    N, K = map(int, sys.stdin.readline().split())
    N += 2
    B = [None] * N
    for j in xrange(0, N-2):
        B += [None] + norm(list(sys.stdin.readline().strip())) + [None]
    B += [None] * N
    print "Case #%d: %s" % (i, M.get(solve(B, N, K)))