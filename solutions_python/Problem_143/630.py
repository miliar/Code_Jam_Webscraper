#!/usr/bin/env python

import sys
import itertools
import numpy

def solve(A, B, K):
    cnt = 0
    kb = bin(K)[2:]
    for a in range(A):
        for b in range(B):
            ab = bin(a)[2:]
            bb = bin(b)[2:]
            m = max(len(ab), len(bb), len(kb))
            ab = ab.rjust(m, "0")
            bb = bb.rjust(m, "0")
            kb = kb.rjust(m, "0")
            t = True
            for j in range(kb.index("1")):
                if ab[j] == "1" and bb[j] == "1":
                    t = False
                    break
            if t:
                res = 0
                for i, v in enumerate(range(m)):
                    if ab[v] == "1" and ab[v] == bb[v]:
                        res += 2 ** (m-i-1)
                        if res >= K:
                            break
                if res < K:
                    cnt += 1
    return cnt
            

filename = sys.argv[1]

inp = open(filename.strip())
lines = inp.readlines()

i = 1
for line in lines[1:]:
    (A, B, K) = map(lambda i: int(i), line.strip().split(" "))
    print "Case #%d: %s" % (i, solve(A, B, K))
    i += 1

