#!/usr/bin/python

import sys
rl = sys.stdin.readline

def opt(k, v, X, best):
    if best[v][k] != None:
        return best[v][k]
    best[v][k] = optimize(k,v,X,best)
    return best[v][k]

def optimize(k,v,X,best):
    if X[k][1] == 2:
        return v != X[k][0] and 10**9 or 0
    a = opt(k*2,v,X,best)
    b = opt(k*2+1,v,X,best)
    if X[k][0] == v:
        m = a+b
        if X[k][1] == 1:
            o = 1+min(a,b)
            if o < m:
                m = o
        return m
    else:
        m = min(a,b)
        if X[k][1] == 1:
            o = 1+a+b
            if o < m:
                m = o
        return m

for n in xrange(1,int(rl())+1):
    M,V = map(int,rl().split())
    X = [0]
    for i in xrange((M-1)/2):
        X.append(map(int,rl().split()))
    for i in xrange((M+1)/2):
        X.append( (int(rl()),2) )
    best = [[None] * (M+1), [None] * (M+1)]
    ans = opt(1, V, X, best)
    if ans > (M+2):
        print "Case #%d: IMPOSSIBLE" % n
    else:
        print "Case #%d: %d" % (n,ans)
