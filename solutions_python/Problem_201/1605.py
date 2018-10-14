#!/usr/bin/env python3

from heapq import heappush, heappop

t = int(input())
for i in range(1, t + 1):
    print('Case #{}: '.format(i), end='')
    n, k = map(int, input().split())
    empty_ranges = [(-n, 0)]
    for j in range(k):
        length, first = heappop(empty_ranges)
        length *= -1
        last = first + length - 1
        choice = (first + last) // 2
        l = choice - first
        r = last - choice
        heappush(empty_ranges, (-l, first))
        heappush(empty_ranges, (-r, 1 + choice))
    print('{} {}'.format(r, l))
