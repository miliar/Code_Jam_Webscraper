#!/usr/bin/env python

def solve():
    n, m = map(int,raw_input().split())
    l = [map(int,raw_input().split()) for i in xrange(n)]
    t = [[100 for i in xrange(m)] for i in xrange(n)]
    for k in range(1,100)[::-1]:
        for i in xrange(m):
            if k >= max([l[j][i] for j in xrange(n)]):
                for j in xrange(n):
                    t[j][i] = k
        for i in xrange(n):
            if k >= max(l[i]):
                for j in xrange(m):
                    t[i][j] = k
    for i in xrange(n):
        for j in xrange(m):
            if t[i][j] != l[i][j]:
                print 'NO'
                return
    print 'YES'

z = int(raw_input())
for case in xrange(1,z+1):
    print "Case #" + str(case) + ":",
    solve()