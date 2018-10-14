#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

import sys

def debug(a): sys.stderr.write(str(a) + '\n')
def readarray(foo): return [foo(e) for e in raw_input().split()]
def readint(): return int(raw_input().strip())

debug = lambda x: x

def calc(data, D):
    results = []
    for i in xrange(len(data)):
        for j in xrange(i + 1, len(data) + 1):
            some_range = data[i:j]
            expected = (sum(e[1] for e in some_range) - 1) * D
            positions = [e[0] for e in some_range]
            actual = max(positions) - min(positions)
            results.append((expected - actual) / 2.0)
    return max(results)

T = readint()
for i in xrange(T):
    C, D = readarray(int)
    data = []
    for j in xrange(C):
        P, V = readarray(int)
        data.append((P, V))
    data.sort(key=lambda x: x[0])
    debug(data)
    print('Case #{0}: {1}'.format(i + 1, calc(data, D)))
