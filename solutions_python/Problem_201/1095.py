#!/usr/bin/env python3

import sys
from collections import defaultdict

IMP = 'IMPOSSIBLE'

def print_res(n, res1, res2):
    print('Case #{}: {} {}'.format(n, res1, res2))


def solve(N, K):
    ranges = defaultdict(int)
    ranges[N] += 1

    for i in range(K):
        ls = N
        rs = N
        min_ls = -1
        min_rs = -1
        min_range = N
        for r in ranges:
            mid = (r + 1) // 2
            new_ls = mid - 1
            new_rs = r - mid
            if (new_ls > min_ls) or (new_ls == min_ls and new_rs > min_rs):
                ls = new_ls
                rs = new_rs
                min_range = r
                min_ls = ls
                min_rs = rs
        ranges[min_range] -= 1
        if ranges[min_range] == 0:
            del ranges[min_range]
        ranges[ls] += 1
        ranges[rs] += 1
    return rs, ls


with open(sys.argv[1], 'r') as f:
    test_cases = int(f.readline())
    for tc in range(test_cases):
        line = f.readline().split()
        res1, res2 = solve(int(line[0]), int(line[1]))
        print_res(tc + 1, res1, res2)
