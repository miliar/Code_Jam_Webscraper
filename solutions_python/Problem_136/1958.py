#!/usr/bin/env python3

import sys

T = int(next(sys.stdin))

for x in range(1, T+1):
    C, F, X = [float(num) for num in next(sys.stdin).split()]
    best = X/2.0
    n = 0
    elapsed = 0
    while True:
        elapsed += C / (2 + (n * F))
        if best < elapsed + (X/(2+ (F * (n+1)))):
            break
        else:
            best = elapsed + (X/(2+ (F * (n+1))))
            n+=1

    print("Case #{}: {}".format(x, best))
