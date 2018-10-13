#!/usr/bin/env python -u

from collections import Counter
import sys
import logging
from logging import debug, info
from itertools import *


def parse_problems(f):
    total = int(sys.stdin.readline())
    for num in count(start=1):
        line = f.readline().strip()
        if line:
            info("%d of %d ----------", num, total)
            ns, ks = line.split(maxsplit=1)
            yield num, [int(ns), int(ks)]
        else:
            return


def solve_problem(n, k):
    info(f"n=%s, k=%s", n, k)
    state = Counter([n])
    remaining = k
    while remaining > 0:
        size = max(state.keys())
        count = state[size]
        debug('Filling %19d blocks of %19d', count, size)
        to_remove = min([count, remaining])

        pick = size // 2
        l, r = pick, size - pick - 1
        if l > 0:
            state.update({l: to_remove})
        if r > 0:
            state.update({r: to_remove})
        state.update({size: -to_remove})
        if state[size] == 0:
            del state[size]
        remaining -= to_remove

    return max([l, r]), min([l, r])


def format_solution(i, solution):
    return f'Case #{i}: {" ".join(str(b) for b in solution)}'


def main():
    logging.basicConfig(
        level=logging.WARNING,
        format='{levelname:>7s}: {message}',
        style='{',
    )
    for i, problem in parse_problems(sys.stdin):
        print(format_solution(i, solve_problem(*problem)))


if __name__ == '__main__':
    main()
