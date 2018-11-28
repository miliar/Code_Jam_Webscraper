#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def run(S, p, t):
    ret = 0
    for x in t:
        if x is 0 or x is 1:
            if x >= p:
                ret += 1
        elif x >= 3 * p - 2:
            ret += 1
        elif x >= 3 * p - 4:
            if S > 0:
                S -= 1
                ret += 1
    return ret
    
if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) > 1:
        fname = sys.argv[1]
        if fname != "-":
            f = open(fname)
    N = int(f.readline())
    for _num in xrange(N):
        temp = map(int, f.readline().split())
        _, S, p = temp[:3]
        t = temp[3:]
        ret = run(S, p, t)
        print "Case #%d: %d" % (_num+1, ret)
