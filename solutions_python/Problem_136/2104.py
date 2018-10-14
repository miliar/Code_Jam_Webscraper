#!/usr/bin/env python

import sys
import os

def solve(t):
    [C, F, X] = map(float, sys.stdin.readline().split())

    wait = 0.0
    curr_cookies = 0.0
    rate = 2.0
    while X - curr_cookies > 1e-6:
        just_wait = (X - curr_cookies) / rate

        to_farm = C- curr_cookies
        farm_wait_1 = to_farm / rate
        rate += F
        farm_wait = farm_wait_1 + X / rate

        if farm_wait < just_wait:
            curr_cookies = 0.0
            wait += farm_wait_1
        else: 
            wait += just_wait
            break

    print 'Case #{0}: {1:.7f}'.format(t, wait)

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for t in range(1, T + 1):
        solve(t)
