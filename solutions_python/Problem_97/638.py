#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def run(A, B):
    ret = 0
    seen = set()
    for x in xrange(A, B+1):
        if x in seen:
            continue
        word = str(x)
        s = set()
        for i in xrange(len(word)):
            newx = int(word[i:] + word[:i])
            if A <= newx <= B:
                s.add(newx)
        N = len(s)
        if N > 1:
            ret += (N-1)*N/2
            seen.update(s)
    return ret
    
if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) > 1:
        fname = sys.argv[1]
        if fname != "-":
            f = open(fname)
    N = int(f.readline())
    for _num in xrange(N):
        A, B = map(int, f.readline().split())
        ret = run(A, B)
        print "Case #%d: %d" % (_num+1, ret)
