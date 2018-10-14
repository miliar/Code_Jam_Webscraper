#!/usr/bin/env python3
def solve(N, K):
    """Counter.  ON if lower N bits are 1."""
    return (K + 1) % 2**N == 0

T = int(input())
for case in range(1, T + 1):
    N, K = (int(w) for w in input().split())
    print("Case #{0}: {1}".format(case,
                                  ("OFF", "ON")[solve(N, K)]))
