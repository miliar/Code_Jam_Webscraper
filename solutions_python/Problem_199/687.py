#!/usr/bin/env python
#coding:utf-8
#py2

def fw_update(f, pos, diff):
    i = pos
    while i > 0: 
        f[i] += diff #in fact, %2 is enough
        i -= i&-i

def fw_sum(f, pos, max_pos):
    res = 0
    i = pos 
    while i <= max_pos: 
        res += f[i]
        i += i&-i
    return res

def idx(x):
    return x + 1

T = int(raw_input()) #1 100

for cas in xrange(1, T + 1):
    S, K = raw_input().strip().split()
    K = int(K) #2 S
    S = list(S)
    n = len(S) #2 1000
    can = True
    cnt = 0
    f = [0 for i in xrange(idx(n - 1) + 1)]
    max_pos = n - 1
    for i in xrange(n):
        c = S[i]
        flips = fw_sum(f, idx(i), n)
        if flips%2:
            if c == '+':
                c = '-'
            else:
                c = '+'
        if c == '-':
            r = i + K - 1
            if r >= n:
                can = False
                break
            fw_update(f, idx(r), 1)
            cnt += 1
    if can:
        print "Case #%s:"%cas, cnt
    else:
        print "Case #%s:"%cas, "IMPOSSIBLE"
