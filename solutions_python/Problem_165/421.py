#!/usr/bin/python

import sys


def readints(f):
    return [int(s) for s in f.readline().split()]


def readint(f):
    return int(f.readline())


def readmatrix(f, rows):
    matrix = []
    for i in xrange(rows):
        matrix += [readints(f)]
    return matrix


def eachCell(matrix):
    for i in xrange(len(matrix)):
        for j in xrange(len(matrix[i])):
            yield (i, j, matrix[i][j])


class memoized(object):

    """Decorator that caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned, and
    not re-evaluated.
    """

    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        try:
            return self.cache[args]
        except KeyError:
            self.cache[args] = value = self.func(*args)
            return value
        except TypeError:
            # uncachable -- for instance, passing a list as an argument.
            # Better to not cache than to blow up entirely.
            return self.func(*args)

    def __repr__(self):
        """Return the function's docstring."""
        return self.func.__doc__


def solve(r, c, w):
    if w == 1 or w == c:
        return c

    initial = w - 1
    curs = initial
    count = 0
    while curs < c:
        curs += w
        count += 1
    curs -= w

    if curs == c - 1:
        return count + w - 1
    else:
        return count + w

    return

if __name__ == "__main__":
    f = open(sys.argv[1], "r")

    numCases = readint(f)
    for i in xrange(numCases):
        r, c, w = readints(f)
        print "Case #%d: %d" % (i + 1, solve(r, c, w))
