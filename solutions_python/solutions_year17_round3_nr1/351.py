#!/usr/bin/env pypy3
"""Task #1"""
from math import *
from collections import deque, OrderedDict
from heapq import *; from bisect import *
from itertools import *
def ri(): return int(input())
def ris(): return [int(chrs) for chrs in input().split()]
#########################################################


def run():
    ans = -1.0
    num, need = ris()
    items = [] #i, h, s
    for i in range(num):
        r, h = ris()
        items.append([i, 2*pi*r*h, pi*r*r])

    byh = sorted(items, key=lambda x: x[1])
    bys = sorted(items, key=lambda x: x[2])
    #byh_keys = [i[0] for i in byh]
    used = set()

    while num - len(used) >= need:

        large = bys.pop(-1)
        used.add(large[0])
        # bk = bisect_left(byh_keys, large[0])
        # byh_keys.pop(bk)
        # byh.pop(bk)
        # for i, v in enumerate(byh):
        #     if v[0] == large[0]:
        #         byh.pop(i)
        # other = list(reversed(byh))[:need-1]
        # a = large[1] + large[2] + sum(x[1] for x in other)

        a = large[1] + large[2]
        cnt = 1
        # while cnt < need:
        #     cnt += 1
        for x in reversed(byh):
            if cnt >= need: break
            if x[0] in used: continue
            cnt += 1
            a += x[1]

        ans = max(ans, a)

    return ans

for case in range(1, int(input()) + 1):
    print('Case #{}: {}'.format(str(case), str(run())))
