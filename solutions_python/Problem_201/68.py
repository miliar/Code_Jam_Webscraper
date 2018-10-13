#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys

def rl(proc=None):
    if proc is not None:
        return proc(sys.stdin.readline())
    else:
        return sys.stdin.readline().rstrip()

def srl(proc=None):
    if proc is not None:
        return map(proc, rl().split())
    else:
        return rl().split()

def solve(N, K):
    r = [[N, 1]]
    K -= 1
    while K:
        c = r[0]
        if K >= c[1]:
            k = c[1]
            r = r[1:]
        else:
            k = K
            c[1] -= k
        K -= k
        n1 = c[0] / 2
        n2 = (c[0] - 1) / 2
        for t in (n1, n2):
            for v in r:
                if v[0] == t:
                    v[1] += k
                    break
            else:
                r.append([t, k])
    best = r[0][0]
    return best / 2, (best - 1) / 2

def main():
    T = rl(int)
    for t in xrange(1, T+1):
        N, K = srl(int)
        print "Case #%d: %d %d" % ((t, ) + solve(N, K))

if __name__ == '__main__':
    main()
