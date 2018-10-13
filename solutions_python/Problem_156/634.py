#!/usr/bin/python

T = int(raw_input())

for caso in range(T):

    D = int(input())    

    P = map(int, raw_input().split())
    
    res = max(P)
    
    baseCase = 2
    
    while baseCase < res:
        res = min(res, sum([(p - 1) // baseCase for p in P]) + baseCase)
        baseCase += 1

    print('Case #%d: %s' % (caso + 1, res))