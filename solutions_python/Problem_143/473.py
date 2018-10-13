#!/usr/bin/env python3
import itertools

num_cases = int(input())
for case in range(1, num_cases+1):
    A, B, K = [int(x) for x in input().split()]

    result = 0
    combs = itertools.product(range(A), range(B))
    for x, y in combs:
        if x & y < K:
            result += 1



    print("Case #{}: {}".format(case, result))
    
