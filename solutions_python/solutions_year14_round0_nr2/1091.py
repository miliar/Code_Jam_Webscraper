#!/usr/bin/env python3
# encoding: utf-8


if __name__ == '__main__':
    cases_n = int(input())
    for i in range(cases_n):
        c, f, x = [float(i) for i in input().split()]
        t = 0
        RATE = 2
        prev_wait = x/RATE
        while True:
            t += c/RATE
            RATE += f
            wait = t + x/RATE
            if wait > prev_wait:
                break
            prev_wait = wait
        print('Case #{}: {:.7f}'.format(i + 1, prev_wait))
