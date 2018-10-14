#!/usr/bin/env python3
import collections
import sys


def main():
    input_file = sys.argv[1]
    solve(input_file)


def solve(input_file):
    with open(input_file) as f_in:
        next(f_in)
        for i, input_line in enumerate(f_in):
            N, K = tuple(int(s) for s in input_line.split())
            ls, rs = solve_instance(N, K)
            print("Case #%d: %d %d" % (i + 1, ls, rs))


def solve_instance(N, K):
    intervals = collections.defaultdict(int)
    intervals[N] = 1
    while K > 0:
        length, count = max(intervals.items())
        if count < K:
            large, small = split(length)
            intervals[small] += count
            intervals[large] += count
            del intervals[length]
            K -= count
        else:
            return split(length)
            

def split(n):
    small = (n - 1) // 2
    large = n - 1 - small
    return large, small


if __name__ == '__main__':
    main()
