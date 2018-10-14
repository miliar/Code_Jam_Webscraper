#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import collections
import copy

fin = sys.stdin
T = int(fin.readline())

for case in range(1, T + 1):
    N = int(fin.readline())
    na = list(map(float,fin.readline().split()))
    ke = list(map(float,fin.readline().split()))

    na.sort()
    ke.sort()

    na1 = copy.deepcopy(na)
    ke1 = copy.deepcopy(ke)

    l = len(na1)

    for i in range(l):
        tmp1 = na1[0]
        del na1[0]
        for j in range(len(ke1)):
            if ke1[j] > tmp1:
                del ke1[j]
                break

    l = len(na)

    i = 0
    while True:
        if i == len(na):
            break

        if na[i] < ke[i]:
            del ke[-1]
            del na[0]
            i = i -1
        i = i + 1

        
    print("Case #%d: %d %d" % (case, len(na), len(ke1)))

