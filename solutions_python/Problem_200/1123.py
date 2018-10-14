#!/usr/bin/env python3

import sys

IMP = 'IMPOSSIBLE'

def print_res(n, res):
    print('Case #{}: {}'.format(n, res))


def is_tidy(num):
    num = str(num)
    for i in range(len(num) - 1):
        if num[i] > num[i + 1]:
            leftover = int(num[i + 1:])
            return False, leftover + 1

    return True, 0


def solve(last_num):
    if last_num < 10:
        return last_num
    while last_num > 10:
        found, to_dec = is_tidy(last_num)
        if found:
            return last_num
        last_num -= to_dec
    return 9

with open(sys.argv[1], 'r') as f:
    test_cases = int(f.readline())
    for tc in range(test_cases):
        line = f.readline()
        res = solve(int(line.strip()))
        print_res(tc + 1, res)
