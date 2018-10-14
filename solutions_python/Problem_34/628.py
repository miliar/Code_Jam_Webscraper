#! /usr/bin/env python

import re

a = raw_input().split()
L, D, N = int(a[0]), int(a[1]), int(a[2])
words = []
for i in xrange(D):
    words.append(raw_input())
for p in xrange(N):
    n = 0
    pat = raw_input()
    pat = re.sub('\)', ']', re.sub('\(', '[', pat))
    m = re.compile(pat)
    for word in words:
        if m.match(word):
            n += 1
    print "Case #%d: %d" % (p+1, n)

