#! /usr/bin/env python
import sys

def main():
    t = int(raw_input())
    for i in xrange(t):
        n = int(raw_input())
        arr = map(int, raw_input().split())
        assert len(arr) == n
        print 'Case #%d: %.6f' % (i + 1, solve(arr))

def solve(arr):
    goal = sorted(arr)
    num_diffs = sum(1 for a, b in zip(arr, goal) if a != b)
    return num_diffs


if __name__ == '__main__':
    sys.exit(main())
