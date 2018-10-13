#!/usr/bin/python

import sys
import math

c = int(sys.stdin.readline())
def permute(inStr, p ):
    i = list(inStr)
    o = i[:]
    for x in range(0,len(i), len(p)):
        for t in range(len(p)):
            o[x + t] = i[x + p[t]]

    return "".join(o)

def rle(inStr):
    o = False
    r = 0
    for x in inStr:
        if x != o:
            r = r + 1
        o = x

    return r

def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]

for x in range(c):
    k = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    r = 1000000

    for t in all_perms(range(k)):
        r = min(r, rle(permute(s, t)))
    print "Case #%d: %d" %(x + 1, r)
