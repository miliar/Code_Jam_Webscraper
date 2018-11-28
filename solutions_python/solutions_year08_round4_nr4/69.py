#!/usr/bin/env python

import sys
import itertools

def compress(l):
    return [a for a,b in itertools.groupby(l)]

def perm(p, s):
    news = ''
    for i in p:
        news += s[i]
    return news

def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]

testcases = int(sys.stdin.readline())
for test in range(1, testcases + 1):
    k = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    permut = all_perms(range(0, k))
    minlen = len(compress(s))
    for i in permut:
        news = ''
        for j in range(0,len(s)/k):
            news += perm(i, s[j*k:(j+1)*k])
        minlen = min(minlen, len(compress(news)))
    print 'Case #%d: %d' % (test, minlen)
