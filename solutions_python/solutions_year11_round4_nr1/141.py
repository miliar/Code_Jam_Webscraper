#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from time import time

input_file = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
output_file = open(sys.argv[2], 'w') if len(sys.argv) > 2 else sys.stdout

def parse(cast=None):
    line = next(input_file).split()
    return list(map(cast, line)) if cast else line


def solve():
    '''
    '''
    X, S, R, t, N = parse(int)
    walkways = []
    for i in range(N):
        walkways.append(parse(int))

    walkways.sort(key=lambda x:x[2])

    times = []
    for B, E, w in walkways:
        L = E - B
        X -= L
        times.append(L / (S + w))

    # 不在加速器上
    if R * t > X:
        tmpt = t
        t = X / R
        t_left = tmpt - t
        X = 0
        for i in range(N):
            B, E, w = walkways[i]
            L = E - B
            if t_left * (w + R) >= L:
                times[i] = L / (w + R)
                t_left -= times[i]
            else:
                # 只能跑一半的情况

                L_left = L - (w + R) * t_left
                times[i] = t_left + L_left / (w + S)
                t_left = 0

            if t_left <= 0:
                break

    else:
        X -= R * t

    t_left = X / S

    # 能够额外加速的距离


    result = sum(times) + t_left + t
    return result


if __name__ == '__main__':
    total_time = 0
    cases = int(next(input_file))

    for case in range(1, cases + 1):
        result = solve()
        print('Case #{}: {:.6f}'.
              format(case, result),
              file=output_file)
