#!/usr/bin/env python3
import sys
import heapq

T = int(input())

# each item: (-size, index)
def solve_small(casei):
    line = input().split(" ")
    N = int(line[0])
    K = int(line[1])
    h = []
    heapq.heappush(h, (- N, 0))
    y = 0
    z = 0
    for i in range(0, K):
        segment = heapq.heappop(h)
        size = - segment[0]
        index = segment[1]
        z = (size - 1) // 2
        y = (size - 1) - z
        heapq.heappush(h, (- z, index))
        heapq.heappush(h, (- y, index + z + 1))
    print("Case #{}: {} {}".format(casei, y, z))

# dict: {size: number_same_size}
def solve(casei):
    line = input().split(" ")
    N = int(line[0])
    K = int(line[1])
    d = {N: 1}
    y = 0
    z = 0
    i = 0
    while i < K:
        size = max(k for k, v in d.items() if v != 0)
        number = d[size]
        z = (size - 1) // 2
        y = (size - 1) - z
        # update
        d[size] = 0
        i = i + number
        d[z] = d.get(z, 0) + number
        d[y] = d.get(y, 0) + number
    print("Case #{}: {} {}".format(casei, y, z))

for i in range(1, T+1):
    solve(i)
