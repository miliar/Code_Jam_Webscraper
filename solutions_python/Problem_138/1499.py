#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: d555_
# @Date:   2014-04-12 15:50:19
# @Last Modified by:   d555_
# @Last Modified time: 2014-04-12 19:51:19

import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


T = int(raw_input())
for t in range(1, T + 1):
    N = int(raw_input())
    A = [0] + map(float, raw_input().split())
    A.sort()
    B = [0] + map(float, raw_input().split())
    B.sort()
    i = 1
    iB = [0] * N
    j = 1
    while i <= N:
        while j <= N:
            if iB[j - 1] == 0 and A[i] < B[j]:
                iB[j - 1] = 1
                break
            j += 1
        if j > N:
            break
        i += 1
    pWar = iB.count(0)

    i = 1
    j = 1
    endB = N - 1
    iB = [0] * N
    dWar = 0
    while i <= N:
        if not iB[endB] == 1:
            if A[i] < B[j]:
                iB[endB] = 1
                endB = endB - 1
            else:
                dWar = dWar + 1
                j = j + 1
        i = i + 1
    print "Case #{0}: {1} {2}".format(t, dWar, pWar)
