#!/usr/bin/env pypy3
"""Task #2"""
from math import *
from collections import deque, OrderedDict
from heapq import *; from bisect import *
from itertools import *
def ri(): return int(input())
def ris(): return [int(chrs) for chrs in input().split()]
#########################################################

w, m = 0, 1
def run():
    aw, am = ris()
    aws = sorted([ris() for _ in range(aw)])
    ams = sorted([ris() for _ in range(am)])

    if aw+am == 1:
        return 2

    if aw == am == 1:
        return 2
        a = sorted([aws[0], ams[0]])


        # t = abs(aws[0][0] - ams[0][0])
        # if t <= 720:
        #     return 2
        # return 4

    a = aws if aws else ams
    if a[1][0] - a[0][1] >= 720:
        return 2
    if 1440 - a[1][1] + a[0][0] >= 720:
        return 2
    return 4
    # t = a[1][1] - a[0][0]
    # if t <= 720:
    #     return 2
    # return 4

    #return min(run_i(aws, ams), run_i(ams, aws))


def run_i(ints_1, ints_2):
    ans = 0
    ints = [ints_1, ints_2]
    currt = 0
    currpos = 0
    while True:
        # if currt == 1440:
        #     if currpos == 1:
        #         return ans + 1
        #     return ans
        lastt = currt + 720
        if lastt > 1440: lastt = 1440
        for i in ints[currpos]:
            if currt <= i[0] <= lastt:
                lastt = i[0]
                break
        if lastt == 1440:
            if currpos == 1:
                return ans + 1
            return ans

        currpos = (currpos+1)%2
        currt = lastt
        ans += 1



for case in range(1, int(input()) + 1):
    print('Case #{}: {}'.format(str(case), str(run())))
