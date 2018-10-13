#!/usr/bin/env python

from __future__ import division, print_function

import fileinput


def min_dining_time(diners):
    min_time = 100000
    for split_threshold in range(1, 1+max(diners)):
        split_time = 0
        for diner in diners:
            while diner > split_threshold:
                diner -= split_threshold
                split_time += 1
        min_time = min(split_time + split_threshold, min_time)
    return min_time


if __name__ == '__main__':
    for i, line in enumerate(fileinput.input()):
        if i == 0 or i % 2 == 1:
            continue
        i = i // 2
        diners = map(int, line.strip().split())
        print("Case #{}: {}".format(i, min_dining_time(diners)))
