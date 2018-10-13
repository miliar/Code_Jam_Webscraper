#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

import sys

def debug(a): sys.stderr.write(str(a) + '\n')
def readarray(foo): return [foo(e) for e in raw_input().split()]
def readint(): return int(raw_input().strip())

debug = lambda x: x

def calc(X, S, R, t, N, W):
    """W = (length, w)"""
    no_walk_way = X - sum(elem[0] for elem in W)
    debug(no_walk_way)
    W.sort(key=lambda x: x[1])
    W.insert(0, (no_walk_way, 0))
    debug(W)

    result = 0
    for elem in W:
        full_run_time = elem[0] / (elem[1] + R)
        if t == 0:
            result += elem[0] / (elem[1] + S)
        elif t >= full_run_time:
            result += full_run_time
            t -= full_run_time
        else:
            result += t
            result += (elem[0] - (elem[1] + R) * t) / (elem[1] + S)
            t = 0
    return result

T = readint()
for i in xrange(1, T+1):
    X, S, R, t, N = readarray(int)
    W = []
    for j in xrange(N):
        B, E, w = readarray(float)
        W.append((E-B, w))
    print('Case #{0}: {1}'.format(i, calc(X, S, R, t, N, W)))
