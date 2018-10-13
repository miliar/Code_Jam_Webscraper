#!/usr/bin/env python
# -*- coding: utf-8 -*-

T=int(raw_input())

def calc(A,B,K):
    res = 0
    for a in xrange(0,A):
        for b in xrange(0,B):
            if a&b < K:
                res+=1
    return res

for case in xrange(T):
    A,B,K = map(int,raw_input().split())
    print 'Case #%d:'%(case+1),
    print calc(A,B,K)
