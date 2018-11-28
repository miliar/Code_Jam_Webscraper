#!/usr/bin/env python
# encoding: utf-8

'''
bathroom_stalls.py
Created by Shuailong on 2017-04-08.
https://code.google.com/codejam/contest/3264486/dashboard#s=p2
'''

from heapq_max import *

def split(number):
    if number % 2 == 0:
        return number / 2, number / 2 - 1
    else:
        return number / 2, number / 2

def solver(N, K):
    q = []
    heappush_max(q, N)
    count = 0
    while len(q) > 0:
        head = heappop_max(q)
        count += 1
        lchild, rchild = split(head)
        if count == K:
            return lchild, rchild
        else:
            heappush_max(q, lchild)
            heappush_max(q, rchild)


T = int(raw_input())
for case in xrange(1, T + 1):
    N, K = [int(i) for i in raw_input().split(' ')]
    y, z = solver(N, K)
    print "Case #{}: {} {}".format(case, y, z)
