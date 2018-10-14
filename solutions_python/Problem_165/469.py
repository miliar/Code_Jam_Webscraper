#!/usr/bin/python

import sys

data = file(sys.argv[1]).read().splitlines()

T = int(data.pop(0))

def numVbrute(X,numX,W,C):
    V = 0
    for i in xrange(0,C-W+1):
        found = 1
        for j in xrange(0,W):
            # miss
            if X[j] == 2:
                found = 0
                break
        if found:
            V = V + 1
    return V

def minV(CC,W):
    if CC == W:
        return W
    
CACHE={}
def brute(CC,W):
    G = 0
    if W == 1:
        return CC
    if CC in CACHE:
        return CACHE[CC]
    if CC < W:
        assert False
    if CC == W:
        return W
    elif CC <= W*2:
        return W+1
    else:
        b = brute(CC-W,W) + 1
        m = max(W+1,b)
        CACHE[CC] = m
        return m


for CASE in xrange(1,T+1):
    print 'Case #%d:' % (CASE),
    (R, C, W) = [int(x) for x in data.pop(0).split()]
    CACHE = {}
#    print R,C,W,brute(C,W)
    print brute(C,W)



