# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Yixuan Zhao <johnsonqrr (at) gmail.com>


T = int(raw_input())
# T = 1


def jisuangailu(probability, work_num):
    # small
    p = 1.0
    for i in probability:
        p *= i
    return p

for t in range(1, T + 1):
    total, work_num = [int(i) for i in raw_input().split(' ')]     # the total number of cores, and the minimum number of cores that must succeed
    U = float(raw_input())
    probability = [float(i) for i in raw_input().split(' ')]
    # Small dataset 1 K= N
    probability.sort()
    res = 0
    if sum(probability) + U >= total * 1.0:
        res = 1.0
    else:
        for index in range(total):
            if index == total -1:
                # probability[index] += U
                # break
                probability[:index + 1] = [probability[index] + U / (index + 1)] * (index + 1)

                break
            if (probability[index + 1] - probability[index]) * (index + 1) <= U:    # 前面全拔高
                U -= (probability[index + 1] - probability[index]) * (index + 1)
                probability[:index + 1] = [probability[index + 1]] * (index + 1)
            else:
                probability[:index + 1] = [probability[index] + U / (index + 1)] * (index + 1)
                break
    if res < 1.0:
        res = jisuangailu(probability, total)
    print "Case #{}: {}".format(t, res)
