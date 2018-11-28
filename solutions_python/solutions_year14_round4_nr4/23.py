#!/usr/bin/env python

MOD = 1000000007
mem = dict()

def count(S):
    S = frozenset(S)
    if S not in mem:
        if len(S) == 0:
            res = 0
        else:
            nodes = set(s[0] for s in S)
            res = len(nodes)
            for a in nodes:
                res += count(filter(None, (s[1:] for s in S if s[0] == a)))
        mem[S] = res
    return mem[S]

def rec(M, N, S, servers, i):
    if i == M:
        res = 0
        for j in xrange(N):
            T = [S[k] for k in xrange(M) if servers[k] == j]
            if len(T) == 0:
                return 0, 0
            res += count(T) + 1
        return res, 1
    X = 0
    Y = 0
    for j in xrange(N):
        servers[i] = j
        x, y = rec(M, N, S, servers, i + 1)
        if x == X:
            Y += y
        elif x > X:
            X = x
            Y = y
    return X, Y % MOD

def solve(M, N, S):
    return ' '.join(map(str, rec(M, N, S, [0] * M, 0)))

T = int(raw_input())
for x in xrange(1, T + 1):
    M, N = map(int, raw_input().split())
    S = [raw_input() for i in xrange(M)]
    print 'Case #%d: %s' % (x, solve(M, N, S))
