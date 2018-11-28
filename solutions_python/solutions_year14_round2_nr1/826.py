#!/usr/bin/env python

import sys

def check_char(s):
    po = 1
    cs = {}
    for c in s[0]:
        cs.setdefault(c, 0)
        cs[c] = po
    for l in s[1:]:
        po += 1
        for c in l:
            if not c in cs.keys():
                return -1
            cs[c] = po
        for k in cs.keys():
            if cs[k] != po:
                return -1
    return 0

def get_data(s):
    r = []
    cnt = 0
    bk = s[0]
    for c in s:
        if bk != c:
            r.append([bk, cnt])
            cnt = 0
        bk = c
        cnt += 1
    r.append([bk, cnt])
    return r

def meter(a, b):
    if len(a) != len(b):
        return -1
    r = 0
    for i in range(len(a)):
        ac = a[i][0]
        an = a[i][1]
        bc = b[i][0]
        bn = b[i][1]
        if ac != bc:
            return -1
        xx = an - bn
        if xx < 0:
            xx *= (-1)
        r += xx
    return r

def solve():
    s = []
    n = int(raw_input())
    for i in range(n):
        s.append(raw_input())
    if check_char(s) == -1:
        return "Fegla Won"
    xx = []
    for l in s:
        xx.append(get_data(l))
    r = 9999999999
    for i in range(len(xx)):
        sum = 0
        for j in range(len(xx)):
            www = meter(xx[i], xx[j])
            if www == -1:
                return "Fegla Won"
            sum += www
        if sum < r:
            r = sum
    return str(r)

N = int(raw_input())
for i in range(N):
    print 'Case #' + str(i+1) + ': ' + solve()
