#!/usr/bin/env python
#coding:utf-8
import sys
sys.setrecursionlimit(10000000)
T = int(raw_input())

for cas in xrange(1, T + 1):
    #R C 1 25
    R, C = map(int, raw_input().strip().split())
    a = [list(raw_input().strip()) for i in xrange(R)]
    #expand in row
    for r in xrange(R):
        last = -1
        for c in xrange(C):
            if a[r][c] != '?':
                for i in xrange(last + 1, c):
                    a[r][i] = a[r][c]
                last = c
        if last != -1:
            for c in xrange(last + 1, C):
                a[r][c] = a[r][last]
    #between rows
    last = -1
    for r in xrange(R):
        if a[r][0] != '?':#C >= 1
            for i in xrange(last + 1, r):
                a[i] = a[r][:]
            last = r
    for i in xrange(last + 1, R):
        a[i] = a[last] #last != -1
    print "Case #%s:"%(cas)
    for r in xrange(R):
        print ''.join(a[r])

