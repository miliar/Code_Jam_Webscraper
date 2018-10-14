#!/usr/bin/env python
# -*- coding: utf-8 -*-

T = int(input())
for case in range(T):
    N = int(input())
    M = list(map(int,input().split()))
    sub = [0]

    prev = M[0]
    for m in M:
        if m < prev:
            sub.append(prev-m)
        prev = m
    rate = max(sub)
    ans2= 0
    for m in M[:N-1]:
        if m < rate:
            ans2 += m
        else:
            ans2 += rate
    print("Case #{0}: {1} {2}".format(case+1,sum(sub),ans2))

