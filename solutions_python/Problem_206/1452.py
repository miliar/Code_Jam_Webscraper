#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys


def cruise(f, d, n):
    times = [0] * n
    lst = []

    for i in range(n):
        lst.append(tuple(map(lambda x: float(x), f.readline().split())))
    lst.sort(_horse_cmp)

    for i in range(n):
        max_speed = _get_max(times)
        if ((d - lst[i][0]) / lst[i][1]) > max_speed:
            times[i] = (d - lst[i][0]) / lst[i][1]
        else:
            times[i] = max_speed
    return d / max(times)

def _get_max(lst):
    max = -1
    for i in lst:
        if i == 0:
            return max
        if i > max:
            max = i
    return max


def _horse_cmp(a, b):
    if a[0] > b[0]:
        return -1
    else:
        return 1


with sys.stdin as f:
    T = int(f.readline())
    for i in range(T):
        d, n = tuple(map(lambda x: int(x), f.readline().split()))
        speed = cruise(f, d, n)

        print("Case #" + str(i+1) + ": " + "{:.6f}".format(speed))
f