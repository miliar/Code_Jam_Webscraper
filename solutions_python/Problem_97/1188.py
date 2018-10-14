#!/usr/bin/env python

from sys import stdin
from math import log10

T = int(stdin.readline())

def narabi(n, keta):
    mawari = 10 ** (keta-1)
    see = n
    ret = n
    for i in range(keta-1):
        see = see / mawari + see % mawari * 10
        if see < mawari: continue
        if ret > see: ret = see
        pass
    return ret


for t in range(1,1+T):
    wds = stdin.readline().split()
    A = int(wds[0])
    B = int(wds[1])

    keta = int(log10(A)) + 1

    bank = dict([])
    for i in range (A, B+1):
        key = str(narabi(i, keta))
        if key in bank:
            bank[key] += 1
        else:
            bank[key] = 1
            pass
        pass

    ret = 0
    for i in bank:
        if bank[i] == 1: continue
        ret += bank[i] * (bank[i]-1) / 2
        pass


    print "Case #%d: %d" % (t, ret)
