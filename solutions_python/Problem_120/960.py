#!/usr/bin/env python3

T = int(input())

for case in range(T):
    r, t = map(int, input().split())

    rings = 0
    total = 2 * r + 1
    x = total
    while total <= t:
        x += 4
        total += x
        rings += 1

    print('Case #{0}: {1} '.format(case + 1, rings))
