import sys
import numpy as np
import math

from collections import defaultdict

f = sys.stdin

if 'DEBUG' in sys.argv:
    f = open('in.txt', 'r')


def gi():
    return int(f.readline())


def gil():
    return map(int, f.readline().strip().split())


def gfl():
    return map(float, f.readline().strip().split())

def goods(gs, P):
    for i in range(len(gs)):
        gs[i] %= P

    types = defaultdict(int)
    for v in gs:
        types[v] += 1

    ans = types[0]
    del types[0]

    possp = [
        [],
        [],
        [{1: 2}],
        [{2: 1, 1: 1}, {1: 3}, {2:3}],
        [{3:1, 1:1}, {2:2}, {2:1, 1:2}, {2:1, 3:2}, {1: 4}, {3:4} ]
    ]

    for d in possp[P]:
        while True:
            possible = True
            for v, cnt in d.iteritems():
                if types[v] < cnt:
                    possible = False
                    break
            if possible:
                ans += 1
                for v, cnt in d.iteritems():
                    types[v] -= cnt
            else:
                break

    for v, cnt in types.iteritems():
        if cnt > 0:
            ans += 1
            break

    return ans


def solve():
    tests = gi()
    for testNr in range(1, tests + 1):
        N, P = gil()
        gs = gil()
        print "Case #%d: %d" % (testNr, goods(gs, P))



solve()
