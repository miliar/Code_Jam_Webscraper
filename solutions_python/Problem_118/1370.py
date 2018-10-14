#!/usr/bin/env python2
# coding: utf-8

from itertools import islice
import sys

def intsqrt(x):
    l = 0
    r = x
    while l < r:
        mid = (l + r + 1) / 2
        if mid ** 2 > x:
            r = mid - 1
        else:
            l = mid
    return l

def count(x):
    x = str(x)
    l = len(x)

    if l == 0 or long(x) == 0:
        return 0
    if l == 1:
        return min(long(x), 3)
    if l == 2:
        if long(x) >= 22:
            return 5
        if long(x) >= 11:
            return 4
        return 3

    x = list(x)

    res = 0

    if l > 1 and x[0] >= '2':
        t = ['2'] + (['0'] * (l - 2)) + ['2']
        if t <= x:
            res += 1
        if l % 2 == 1:
            t[l/2] = '1'
            if t <= x:
                res += 1

    mone = False
    for i in range((l + 1) / 2):
        if x[i] > '1':
            for j in range(i + 1, (l + 1) / 2):
                x[j] = '2'
            break
    else:
        if x[l/2:] < x[(l - 1)/2::-1]:
            mone = True

    y = 0
    for i in range(1, (l + 1) / 2):
        if l % 2 == 1 and (y or (x[i] > '0' and x[l/2] > '1')):
            res += 1
        y *= 2
        y += min(1, int(x[i]))
    res += y + 1 - long(mone)

    return res + count('9' * (l - 1))

T = int(sys.stdin.readline())


for case in range(1,T+1):
    A, B = map(long, sys.stdin.readline().split())

    print 'Case #%d: %s' % (case, count(intsqrt(B)) - count(intsqrt(A - 1)))
