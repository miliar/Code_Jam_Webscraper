# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Yixuan Zhao <johnsonqrr (at) gmail.com>



T = int(raw_input())
# T =1
from math import pi
def get_side_area(radius, height):
    return 2 * pi * radius * height


def get_top_area(radius):
    return pi * radius * radius


def get_res_byindex(pos):
    global radius, height, side_area, top_area, n, k
    pool = []
    base_area = top_area[pos]
    for index in range(n):
        if top_area[index] <= base_area and index != pos:
            pool.append(side_area[index])
    pool.sort(reverse=-1)
    return sum(pool[:k-1])

for t in range(1, T + 1):
    n, k = [int(i) for i in raw_input().split(' ')]
    radius = []
    height = []
    for _ in range(n):
        r, h = [int(i) for i in raw_input().split(' ')]
        radius.append(r)
        height.append(h)
    side_area = []
    top_area = []
    sum_area = []
    for index in range(n):
        side_area.append(get_side_area(radius[index], height[index]))
        top_area.append(get_top_area(radius[index]))
        sum_area.append(side_area[-1] + top_area[-1])
    if k == 1:
        print "Case #{}:".format(t), '%f'%(max(sum_area))
        continue

    max_sum_index = sum_area.index(max(sum_area))
    max_top_index = top_area.index(max(top_area))
    max_res = 0
    for i in range(n):
        if sum_area[i] >= sum_area[max_top_index]:
            res = get_res_byindex(i) + sum_area[i]
            if res > max_res:
                max_res = res
    # res1 = get_res_byindex(max_sum_index) + sum_area[max_sum_index]
    # res2 = get_res_byindex(max_top_index) + sum_area[max_top_index]
    # res = max(res1, res2)
    print "Case #{}:".format(t), '%f'%max_res





