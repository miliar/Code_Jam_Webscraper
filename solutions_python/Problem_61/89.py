#!/usr/bin/python

import sys

cases = int(sys.stdin.readline())

def combination(n, r):
    nn = 1
    for i in range(0, r):
        nn *= (n-i)
    for i in range(2, r+1):
        nn /= i
    return nn

def pattern(prevpos, pos, n):
    cnt = 0
    for i in range(pos+(pos-prevpos), n):
        cnt += pattern(pos, i, n) * combination(i-pos-1, pos-prevpos-1)
    cnt += combination(n-pos-1, pos-prevpos-1)
    return cnt

for c in range(1, cases+1):
    n = int(sys.stdin.readline())
    cnt = 0
    for i in range(2, n):
        cnt += pattern(1, i, n)
    cnt += 1
    print "Case #%d: %d" % (c, cnt%100003)
