#!/usr/bin/env python3
import math

T = int(input())
for i in range(1, T+1):
    C, F, X = [float(x) for x in input().split()]
    n = math.ceil(X/C-2/F-1)
    if n < 0:
        n = 0
    time = 0
    for j in range(n):
        time += C/(2+j*F)
    time += X/(2+n*F)
    print('Case #{0}: {1}'.format(i, time))
