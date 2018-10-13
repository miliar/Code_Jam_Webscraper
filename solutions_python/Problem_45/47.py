#!/usr/bin/python
# Python 2.6

import sys
from util import FileReader

#import re
#import itertools
#from collections import defaultdict

def count(prisons, start):
    value = 0

    for i in xrange(start + 1, len(prisons)):
        if prisons[i] == 0:
            break
        value += 1

    for i in xrange(start - 1, -1, -1):
        if prisons[i] == 0:
            break
        value += 1

    return value


def solve(prisons, order):

    if not order:
        return 0

    opts = []

    for i, q in enumerate(order):

        nextorder = order[:]
        del nextorder[i]

        next = prisons[:]
        next[q] = 0

        curr = count(next, q)
        future = solve(next, nextorder)

        opts.append(curr + future)

    return min(opts)


def main():

    if len(sys.argv) < 2:
        print "usage: {0} <input-file>".format(__file__)
        sys.exit(-1)

    with open(sys.argv[1]) as _file:
        file = FileReader(_file)

        T = file.int()
        for t in xrange(T):

            P, Q = file.ints()
            order = [v - 1 for v in file.ints()]

            prisons = [1] * P
            result = solve(prisons, order)

            print "Case #{0}: {1}".format(t+1, result)


if __name__ == "__main__":
    main()

