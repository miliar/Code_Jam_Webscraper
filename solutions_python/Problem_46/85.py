#!python

import sys

if len(sys.argv) != 2:
    print "Supply a filename."
    exit(-1)

fn = sys.argv[1]

fh = open(fn, 'r')

text = fh.read().split('\n')

t = int(text[0])
text = text[1:]

def finished(d):
    for k in d.keys():
        if d[k] > k:
            return False
    return True

def kendall_dist(p):
    n = len(p)
    d = 0
    for i in xrange(0, n):
        for j in xrange(i, n):
            if p[i] > p[j]:
                d += 1
    return d

import copy
from collections import defaultdict

for i in xrange(0, t):
    n = int(text[0])
    text = text[1:]
    tars = {}
    rev = defaultdict(list)
    for j in xrange(0, n):
        line = text[j]
        index = line.rfind("1")
        index = max(index, 0)
        tars[j] = index
        rev[index].append(j)

    perm = range(0, n)
    adjusts = defaultdict(int)
    for j in xrange(0, n):
        ts = rev[j]
        if len(ts) == 1:
            rem = perm[j:]
            rem.remove(ts[0])
            perm = perm[:j] + ts + rem
        else:
            min_dist = []
            best_v = -1
            for v in ts:
                if abs(perm.index(v) - j) < min_dist:
                    min_dist = abs(perm.index(v) - j)
                    best_v = v
            rem = perm[j:]
            rem.remove(best_v)
            perm = perm[:j] + [best_v] + rem
            for t in ts:
                if t != best_v:
                    rev[j+1].append(t)

    text = text[n:]
    print "Case #%d: %d" % (i+1, kendall_dist(perm))


fh.close()
