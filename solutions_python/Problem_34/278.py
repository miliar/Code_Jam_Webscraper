#!/usr/bin/python

# google code jam - c.durr - 2009
# Alien Language
# regular expression matching

import sys, re, string

L, D, N = [int(v) for v in sys.stdin.readline().split()]
dict = []
for i in range(D):
    dict.append(sys.stdin.readline().rstrip())

tr = string.maketrans("()","[]")
for i in range(N):
    a = sys.stdin.readline().rstrip().translate(tr)
    res = 0
    for w in dict:
        if re.match(a, w):
            res += 1
    print 'Case #%d:' % (i+1), res
