#!/usr/bin/env python

import sys
stdin = sys.stdin

def calc(c, f, x):
    rate = 2.0
    t = 0

    if x <= c:
        return (x / rate)

    while 1:
        rate2 = rate + f
        dt_a = x / rate
        dt_b_1 = c / rate
        dt_b_2 = x / rate2
        dt_b = dt_b_1 + dt_b_2

        if dt_a <= dt_b:
            return t + dt_a

        rate = rate2
        t += dt_b_1


n = int(stdin.readline().strip())

for i in range(n):
    x = i + 1
    C, F, X = map(float, stdin.readline().strip().split(' '))
    r = calc(C, F, X)
    print('Case #%i: %s' % (x, r))





