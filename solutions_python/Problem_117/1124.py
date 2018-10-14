#!/usr/bin/env python

import fileinput
import sys

import numpy


def find_in_array(arr, value):
    rows, columns = (arr == value).nonzero()
    return zip(rows, columns)


def solve_cuts(pattern):
    transposed = pattern.transpose()
    heights = list(set(pattern.flat))
    heights.sort()
    for height in heights:
        for row, col in find_in_array(pattern, height):
            if ((height - pattern[row]) < 0).any():
                if ((height - transposed[col]) < 0).any():
                    return False
    return True


if __name__ == '__main__':
    input = fileinput.input()
    test_cases = int(input.next())
    for case in xrange(1, test_cases + 1):
        n, m = map(int, input.next().split())
        pattern = numpy.tile([0], (n, m))
        for i in xrange(n):
            row = map(int, input.next().split())
            for j in xrange(m):
                pattern[i][j] = row[j]
        if solve_cuts(pattern):
            print 'Case #%d: YES' % (case,)
        else:
            print 'Case #%d: NO' % (case,)
        sys.stdout.flush()
