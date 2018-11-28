#!/usr/bin/env python

from collections import defaultdict
import sys

ret = 0 # going for speed here, this is ugly

def dd_factory():
    global ret
    ret += 1
    return defaultdict(dd_factory)

def climb(nodes, tree):
    for node in nodes:
        tree = tree[node]

def main():
    global ret
    T = int(sys.stdin.readline())
    t = 0
    while T != t:
        tree = dd_factory()
        N, M = map(int, sys.stdin.readline().split())
        for n in xrange(N):
            climb(sys.stdin.readline().strip().split('/')[1:], tree)
        ret = 0
        for m in xrange(M):
            climb(sys.stdin.readline().strip().split('/')[1:], tree)
        t += 1
        print "Case #%d: %d" % (t, ret, )

if __name__ == '__main__':
    main()
