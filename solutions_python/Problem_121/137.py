#! /usr/bin/env python3

from functools import lru_cache

@lru_cache(maxsize=None)
def max_gain(E, R, values, actual_e):
    if len(values) == 1:
        return actual_e * values[0]
    return max(spend * values[0] + max_gain(E, R, values[1:],
        min(E, actual_e - spend + R)) for spend in range(actual_e + 1))
    if actual_e <= R:
        return actual_e * values[0] + max_gain(E, R, values[1:], min(E, R))
    # is it better to spend all actual_e or just R or just 0
    test1 = actual_e * values[0] + max_gain(E, R, values[1:], min(E, R))
    test2 = R * values[0] + max_gain(E, R, values[1:], actual_e)
    test3 = max_gain(E, R, values[1:], min(E, actual_e + R))
    return max((test1, test2, test3))

T = int(input())

for case in range(T):
    E, R, N = list(map(int, input().split()))
    values = tuple(map(int, input().split()))
    print("Case #{0}: {1}".format(case + 1, max_gain(E, R, values, E)))
