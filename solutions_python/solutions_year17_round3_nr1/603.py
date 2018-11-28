#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools
import numpy as np

T = int(input())  # number of test cases
for t in range(T):
    N, K = [int(v) for v in input().split()]  # available, to choose
    HR = list()
    TL = list()
    for i in range(N):
        r, h = [int(x) for x in input().split()]  # radius, height
        lat = 2 * np.pi * r * h
        top = np.pi * r * r
        TL.append([top, lat])
        # print(r, h, lat, top)

    # solve
    maxarea = 0
    if K == 1:
        # choose the one with more area
        for i in range(N):
            area = TL[i][0] + TL[i][1]
            if area > maxarea:
                maxarea = area
    else:
        # look at all combinations
        for choosen in itertools.combinations(TL, K):
            choosen = list(choosen)
            choosen.sort(reverse=True)
            # print(choosen)
            area = choosen[0][0]
            for i in range(K):
                area += choosen[i][1]
            if area > maxarea:
                maxarea = area

    print("Case #{:d}: {:.8f}".format(t + 1, maxarea))
