# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Yixuan Zhao <johnsonqrr (at) gmail.com>



T = int(raw_input())
# T = 1


# The intervals are closed on the left and open on the right, 
# which ensures that two exactly consecutive intervals have nothing in between but do not overlap.)
for t in range(1, T + 1):
    Ac, Aj = [int(i) for i in raw_input().split(' ')]
    activities_c_begin = []
    activities_c_end   = []
    activities_j_begin = []
    activities_j_end   = []
    for _ in range(Ac):
        begin, end = [int(i) for i in raw_input().split(' ')]
        activities_c_begin.append(begin)
        activities_c_end.append(end)

    for _ in range(Aj):
        begin, end = [int(i) for i in raw_input().split(' ')]
        activities_j_begin.append(begin)
        activities_j_end.append(end)
    half_day = 12 * 60
    if Ac + Aj == 1: # 1 0
        res = 2
    elif Ac == Aj: # 1 1
        res = 2
    elif Ac == 2:           # 2 0
        if max(activities_c_end) - min(activities_c_begin) <= half_day or (min(activities_c_end) + 2 * half_day - max(activities_c_begin) <= half_day):
            res = 2
        else:
            res = 4
    elif Aj == 2:
        if max(activities_j_end) - min(activities_j_begin) <= half_day or (min(activities_j_end) + 2 * half_day - max(activities_j_begin) <= half_day):
            res = 2
        else:
            res = 4
    print "Case #{}: {}".format(t, res)





