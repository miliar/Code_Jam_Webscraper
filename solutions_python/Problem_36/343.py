#!/usr/bin/env python

import sys

find = 'welcome to code jam'

def recur(s, n):
    if n == len(find):
        return 1
    c = find[n]
    poss = s.split(c)
    opts = 0
    for i in range(1, len(poss)):
        opts += recur(c.join(poss[i:]), n + 1)
    return opts

cases = int(sys.stdin.readline())
for i in range(cases):
    print 'Case #%i: %s' % (i + 1, ('000' + str(recur(sys.stdin.readline().strip(), 0)))[-4:])
