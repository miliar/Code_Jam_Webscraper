#!/usr/bin/env python

import sys

memo = {}

def insertion(x,L):
    for i in range(len(L)):
        if x==L[i][0]:
            return L[:i]+[(x,L[i][1]+1)]+L[i+1:]
        elif x>L[i][0]:
            return L[:i]+[(x,1)]+L[i:]
    return L+[(x,1)]

def depop(L):
    if L[0][1]==1:
        return L[1:]
    else:
        return [(L[0][0],L[0][1]-1)]+L[1:]

def calcul(L):
    TL = tuple(L)
    if L[0][0]<=2:
        return L[0][0]
    if TL in memo:
        return memo[TL]
    else:
        x = L[0][0]
        res = x
        for i in range(1,x/2+1):
            LL = depop(L)
            LL = insertion(i,LL)
            LL = insertion(x-i,LL)
            res = min(res,1+calcul(LL))
        memo[TL] = res
        return res

def main():
    T = int(sys.stdin.readline())
    for c in range(1,T+1):
        D = int(sys.stdin.readline())
        L = []
        for x in sys.stdin.readline().split():
            L = insertion(int(x),L)
        print 'Case #%d: %d' % (c,calcul(L))

main()
