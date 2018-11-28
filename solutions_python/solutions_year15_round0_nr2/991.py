#!/usr/bin/python2
import sys, re
import copy

fin = open("B-small-attempt4.in", "r")
fout = open("B.real2", "w")
count = int(fin.readline().rstrip())

small_m = 1000000

def rec(m, p):
    global small_m
    # print m, p
    if m > small_m:
        return m
    if len(p) == 0:
        small_m = min(small_m, m)
        # if m == 6:
        #     print act
        return m
    res = 100000
    res = min(res, rec(m + 1, [x - 1 for x in p if x > 1]))
    u = list(set(p))
    for mp in u:
        if mp > 1:
            mp_cnt = len([x for x in p if x == mp])
            np = [x for x in p if x != mp]
            for j in range(1, mp // 2 + 1):
                res = min(res, rec(m + mp_cnt, np + [j, mp - j] * mp_cnt))
        
    return res

for t in xrange(1, count + 1):
    print("Test {0}".format(t))
    d = int(fin.readline().rstrip())
    p = [int(x) for x in fin.readline().rstrip().split()]
    small_m = 1000000
    res = rec(0, p)
    fout.write("Case #{0}: ".format(t))
    fout.write("{0}\n".format(res))
    fout.flush()