#!/usr/bin/env python3

import sys

IMP = 'IMPOSSIBLE'

def print_res(n, res):
    print('Case #{}: {}'.format(n, res))


def flip(pancakes, flip_len):
    if len(pancakes) < flip_len:
        return None

    res = ''
    for i in range(flip_len):
        res += '+' if pancakes[i] == '-' else '-'

    # Nothing to append when length is equal.
    if len(pancakes) > flip_len:
        res += pancakes[flip_len:]
    return res


def solve(pancakes, flip_len):
    pancakes = pancakes.lstrip('+')
    if not pancakes:
        return 0
    if len(pancakes) < flip_len:
        return IMP

    count = 0
    pancakes = flip(pancakes, flip_len)
    while True:
        if pancakes is None:
            return IMP
        count += 1
        pancakes = pancakes.lstrip('+')
        if not pancakes:
            return count
        pancakes = flip(pancakes, flip_len)
    return count


with open(sys.argv[1], 'r') as f:
    test_cases = int(f.readline())
    for tc in range(test_cases):
        line = f.readline().split()
        res = solve(line[0], int(line[1]))
        print_res(tc + 1, res)
