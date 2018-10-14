#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# $File: solve.py
# $Date: Sat Apr 08 22:31:12 2017 +0800
# $Author: jiakai <jia.kai66@gmail.com>

import numpy as np
import collections

def work():
    N, K = map(int, input().split())

    # len => num
    segments = collections.defaultdict(int)
    segments[N] = 1
    remain = K

    while True:
        l = max(segments.keys())
        nr = segments.pop(l)
        if remain <= nr:
            return get_lr(l)

        remain -= nr
        for i in get_lr(l):
            if i:
                segments[i] += nr

def simulate():
    for n in range(2, 100):
        print('============', n)
        segments = [n]
        while segments:
            idx = int(np.argmax(segments))
            b, a = get_lr(segments[idx])
            print(segments, b, a)
            segments[idx:idx+1] = [i for i in [a, b] if i]

def get_lr(x):
    x -= 1
    a = x // 2
    return x - a, a

def main():
    #return simulate()
    for i in range(int(input())):
        print('Case #{}: {} {}'.format(i + 1, *work()))

if __name__ == '__main__':
    main()
