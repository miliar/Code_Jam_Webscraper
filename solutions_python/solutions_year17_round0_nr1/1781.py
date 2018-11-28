#!/usr/bin/env python

import sys


def go(s, k):
    r = 0
    #print 'before', s
    for i in range(len(s) - (k - 1)):
        if not s[i]:
            r += 1
            for j in range(k):
                s[i + j] = not s[i + j]
        #print 'after ', i, s
    return r if all(s[-k - 1:]) or all(not p for p in s[-k - 1:]) else None


for i, l in enumerate(sys.stdin.read().splitlines()[1:]):
    s, k = l.split(' ', 1)
    s = [p == '+' for p in s]
    k = int(k)
    r = go(s, k)
    print (('Case #%d: ' % (i + 1)) +
           (str(r) if r is not None else 'IMPOSSIBLE'))
