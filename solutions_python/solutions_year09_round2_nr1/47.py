#!/usr/bin/env python

import sys
import re

N = int(sys.stdin.readline().strip())

def parse(dotks, pos):
    assert dtoks[pos] == '('
    w = float(dtoks[pos+1])
    if dtoks[pos+2] == ')':
        attr = None
        return pos+3, (w, attr)
    else:
        attr = dtoks[pos+2]
        pos, ltree = parse(dotks, pos+3)
        pos, rtree = parse(dotks, pos)
        assert dotks[pos] == ')'
        return pos+1, (w, attr, ltree, rtree)

def evalan(dtree, feat):
    p = dtree[0]
    if dtree[1]:
        if dtree[1] in feat:
            p *= evalan(dtree[2], feat)
        else:
            p *= evalan(dtree[3], feat)
    return p

addsp = re.compile(r'([\(\)])')
toks = re.compile(r'\s+')

for n in xrange(N):

    L = int(sys.stdin.readline().strip())

    dtxt = ""
    for l in xrange(L):
        dtxt += sys.stdin.readline()
    dtxt = addsp.sub(r' \1 ', dtxt).strip()
    dtoks = toks.split(dtxt)
    pos, dtree = parse(dtoks, 0)

    A = int(sys.stdin.readline().strip())

    print "Case #%d:" % (n+1)

    for a in xrange(A):
        inp = sys.stdin.readline().strip().split()
        feat = frozenset(inp[2:])
        assert int(inp[1]) == len(feat)

        p = evalan(dtree, feat)
        print "%.7f" % p


