#!/usr/bin/env python3.1

import sys

def readline():
    return next(sys.stdin).strip()

def readvals(t):
    return map(t, readline().split())

onoff = {True: 'ON', False: 'OFF'}

T = int(readline())
for i in range(T):
    N, K = readvals(int)
    print('Case #{}: {}'.format(i + 1, onoff[(K + 1) % 2 ** N == 0]))
