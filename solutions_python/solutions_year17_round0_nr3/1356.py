#!/usr/bin/env pypy3
"""Task #3"""


import heapq


for case in range(1, int(input()) + 1):
    space, iters = (int(x) for x in input().split())
    heap = [-space]
    for _ in range(iters):
        current = heapq.heappop(heap)
        if current == -1:
            min_d = max_d = 0
        elif current == -2:
            heapq.heappush(heap, -1)
            min_d, max_d = 0, 1
        else:
            max_d = -current // 2
            min_d = max_d if -current % 2 != 0 else max_d - 1
            heapq.heappush(heap, -min_d)
            heapq.heappush(heap, -max_d)


    print('Case #{}: {} {}'.format(str(case), str(max_d), str(min_d)))
