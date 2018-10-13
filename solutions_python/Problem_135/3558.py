#!/usr/bin/python -tt

import sys


def solve(row1, arr1, row2, arr2):
    candidates1 = arr1[row1 - 1]
    candidates2 = arr2[row2 - 1]

    final_arr = [c for c in candidates1 if c in candidates2]

    if 1 == len(final_arr):
        return str(final_arr[0])
    elif 0 == len(final_arr):
        return 'Volunteer cheated!'
    else:
        return 'Bad magician!'


def main():
    n_cases = int(sys.stdin.readline())

    for case in xrange(n_cases):
        row1 = int(sys.stdin.readline()[:-1])
        arr1 = [map(int, sys.stdin.readline().split())
                for _ in xrange(4)]

        row2 = int(sys.stdin.readline()[:-1])
        arr2 = [map(int, sys.stdin.readline().split())
                for _ in xrange(4)]

        res = solve(row1, arr1, row2, arr2)
        print 'Case #%d: %s' % (case+1, res)


if __name__ == '__main__':
    main()
