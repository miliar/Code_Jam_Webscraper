#!/usr/bin/python
# -*- coding: utf-8 -*-
    
# google code jam - c.durr - 2013
# 
# 

    
def readInts(): return [int(i) for i in raw_input().split()]


def realSolve(A,M):
    if len(M)==0 or A>M[-1]:
        return 0
    elif A>M[0]:
        return realSolve(A+M[0], M[1:])
    elif A==1: # A<=M[0]
        return len(M)
    else:
        return min(len(M), 1+realSolve(A+A-1, M))

def solve(A,M):
    M.sort()
    for k in range(len(M)):
        c = M[k]
        if c<A:
            A += c
        else:
            return realSolve(A,M[k:])
    return 0



for test in range(int(raw_input())):
    A,N = readInts()
    M = readInts()
    print 'Case #%d:' % (test+1), solve(A,M)
