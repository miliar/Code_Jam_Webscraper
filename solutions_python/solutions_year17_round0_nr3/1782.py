#!/bin/python3

from math import ceil


T = int(input().strip())
for test in range(T):
    N, K = [int(x) for x in input().split()]
    inserted = 0
    gaps = {N: 1}
    lastgaps = (N, N)
    while inserted < K:
        gap = max(gaps)
        count = gaps[gap]
        del gaps[gap]
        if gap % 2 == 1:
            gaps[(gap // 2)] = gaps.get((gap // 2), 0) + 2 * count
            lastgaps = ((gap // 2), (gap // 2))
        else:
            gaps[(gap / 2)] = gaps.get((gap / 2), 0) + count
            gaps[((gap / 2) - 1)] = gaps.get(((gap / 2) + 1), 0) + count
            lastgaps = ((gap / 2), ((gap / 2) - 1))
        inserted += count
    print('Case #%d: %d %d' % ((test + 1), lastgaps[0], lastgaps[1]))
