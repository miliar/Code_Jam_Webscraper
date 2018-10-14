#!/usr/bin/env python3

import math
import sys

def solve(N, K, pancakes):
    # p[0] radius, p[1] height
    pancakes.sort(key=lambda p: p[0] * p[1], reverse=True)
    sum_best_k = sum(2 * p[0] * p[1] for p in pancakes[:k])
    #print('sum_best_k', sum_best_k, pancakes[:k])

    max_sa = 0
    for i, p in enumerate(pancakes):
        total_sa = p[0] ** 2 + sum_best_k
        if i >= K:
            total_sa -= 2 * pancakes[K-1][0] * pancakes[K-1][1]
            total_sa += 2 * pancakes[i][0] * pancakes[i][1]
        #print('total_sa', p, total_sa)
        max_sa = max(max_sa, total_sa)

    return math.pi * max_sa


T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    pancakes = [tuple(map(int, input().split())) for _ in range(n)]
    #print(n, k, pancakes)

    res = solve(n, k, pancakes)
    print('Case #{}: {}'.format(t+1, res))

