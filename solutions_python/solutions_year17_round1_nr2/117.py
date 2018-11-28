#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Uses https://github.com/rkistner/contest-algorithms

import sys

from collections import deque
import heapq
import math

def debug(*args):
    print(*args, file=sys.stderr)

def minmax(serving_size, packet_size):

    # serving_size * k * 0.9 <= packet_size <= serving_size * k * 1.1
    # k * 9 <= packet_size * 10 / serving_size <= k * 11
    # k * 9 <= 15 <= k * 11
    # packet_size * 10 / serving_size / 11 <= k <= packet_size * 10 / serving_size / 9
    # k >= packet_size * 10 / serving_size / 9

    # k_min = math.ceil(packet_size * 10 / serving_size / 11)
    k_min = (packet_size * 10 - 1) // serving_size // 11 + 1
    k_max = packet_size * 10 // serving_size // 9
    return k_min, k_max

fin = sys.stdin
T = int(fin.readline())
for case in range(1, T + 1):
    N, P = map(int, fin.readline().split())
    recipe = list(map(int, fin.readline().split()))
    packet_sizes = []
    for i in range(N):
        sizes = sorted(list(map(int, fin.readline().split())))
        packet_sizes.append(deque(sizes))

    count = 0

    for i in range(P):
        stack = [] # smallest_max
        largest_min = 0

        for j in range(N):

            if not packet_sizes[j]:
                break
            packet_size = packet_sizes[j].popleft()

            k_min, k_max = minmax(recipe[j], packet_size)

            largest_min = max(largest_min, k_min)

            heapq.heappush(stack, (k_max, k_min, j))

        if len(stack) != N:
            break

        while stack[0][0] < largest_min:
            item = heapq.heappop(stack)
            j = item[2]

            if not packet_sizes[j]:
                break
            packet_size = packet_sizes[j].popleft()

            k_min, k_max = minmax(recipe[j], packet_size)

            largest_min = max(largest_min, k_min)

            heapq.heappush(stack, (k_max, k_min, j))

        if len(stack) != N:
            break

        count += 1

    print("Case #%d: %s" % (case, count))

