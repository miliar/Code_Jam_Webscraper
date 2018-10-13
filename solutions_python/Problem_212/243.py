#!/usr/bin/env python3

import sys

def solve():
    N, P = map(int, input().split())
    groups = list(map(int, input().split()))
    if P == 2:
        even = sum(map(lambda x: x%2 == 0, groups))
        odd = N - even
        return N - odd//2
    if P == 3:
        zero = sum(map(lambda x: x%3 == 0, groups))
        one = sum(map(lambda x: x%3 == 1, groups))
        two = sum(map(lambda x: x%3 == 2, groups))
        sm = min(one, two)
        bad = sm
        one -= sm
        two -= sm
        bad += (one+two)*2//3
        return N - bad
    assert len(groups) == N


T = int(input())
for i in range(1, T+1):
    print("Case #%d: %s" % (i, solve()))
