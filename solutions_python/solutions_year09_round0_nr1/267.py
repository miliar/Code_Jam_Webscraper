#!/usr/bin/env python

import sys
import re

l, d, n = (int(i) for i in sys.stdin.readline().strip().split())

wordtree = {}

for wn in xrange(d):
    word = sys.stdin.readline().strip()
    node = wordtree
    for c in word:
        node = node.setdefault(c, {})

#inre = re.compile(r'(?:([^\(\)])|\(([^\)]+)\))+')
inre = re.compile(r'[^\(\)]|\([^\)]+\)')

def calc_n(tokens, wordtree):
    if tokens:
        cnt = 0
        for t in tokens[0]:
            if t in wordtree:
                cnt += calc_n(tokens[1:], wordtree[t])
        return cnt
    else:
        return 1


for i in xrange(n):
    iw = sys.stdin.readline().strip()
    tokens = []
    for m in inre.findall(iw):
        assert len(m) == 1 or len(m) > 3, m
        if len(m) == 1:
            tokens.append(m)
        else:
            tokens.append(m[1:-1])
    print "Case #%d: %d" % (i+1, calc_n(tokens, wordtree))








