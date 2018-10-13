#!/usr/bin/env
# -*- Encoding: utf-8 -*-

from __future__ import print_function, unicode_literals
from collections import defaultdict, deque


def solve(N, K):
    counts = defaultdict(int)
    counts[N] = 1
    nums = deque([N])
    used = set()
    while len(nums) > 0:
        n = nums.popleft()
        if n in used:
            continue

        used.add(n)

        if n == 1:
            break

        nums.append(n / 2)
        if n % 2 == 1:
            counts[n / 2] += counts[n] * 2
        else:
            nums.append(n / 2 - 1)
            counts[n / 2] += counts[n]
            counts[n / 2 - 1] += counts[n]

    keys = [k for k in counts.keys()]
    keys.sort(reverse=True)

    i = 0
    for k in keys:
        i += counts[k]
        if i >= K:
            break

    if k % 2 == 1:
        return k / 2, k / 2
    else:
        return k / 2, k / 2 - 1

if __name__ == '__main__':
    T = int(raw_input())
    for Ti in range(T):
        N, K = map(int, raw_input().split(" "))
        y, z = solve(N, K)
        print("Case #{}: {} {}".format(Ti + 1, y, z))
