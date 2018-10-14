#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# vi: set fileencoding=utf-8 :

import math


def solve(N, K, pancake):
    pancake.sort()
    r, h = pancake[K - 1]
    r_times_h = []
    max_r = r
    area = math.pi * r ** 2
    for i in range(K):
        r, h = pancake[i]
        area += 2 * math.pi * r * h
        r_times_h += [r * h]
    r_times_h.sort()
    for i in range(K, N):
        new_r, new_h = pancake[i]
        radi_delta = math.pi * (new_r ** 2 - max_r ** 2)
        h_delta = 2 * math.pi * (new_r * new_h - r_times_h[0])
        if radi_delta + h_delta > 0:
            max_r = new_r
            r_times_h.pop(0)
            r_times_h += [new_r * new_h]
            r_times_h.sort()
            area += radi_delta + h_delta
    return area 


def answer():
    T = int(input())
    for case_number in range(1, T + 1):
        N, K = map(int, input().split())
        pancake = []
        for n in range(N):
            r, h = map(int, input().split())
            pancake += [(r, h)]
        print('Case #{0}: {1:.9f}'.format(case_number, solve(N, K, pancake)))
    return


if __name__=='__main__':
    import sys
    answer()
