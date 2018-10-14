#!/usr/bin/python

import sys

def readints(f):
    return [int(s) for s in f.readline().split()]

def readint(f):
    return int(f.readline())

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

def surroundings(p, r, c):
    y, x = p
    a = []
    for i in xrange(-1, 2):
        for j in xrange(-1, 2):
            if (i == 0 and j == 0) or y+i < 0 or y+i >= r or x+j < 0 or x+j >= c:
                continue
            a += [(y+i, x+j)]
    return set(a)

def reveal(p, field, n, fringe):
    field = [row[:] for row in field]
    r, c = len(field), len(field[0])
    cnt = 0
    fr = []

    yy, xx = p
    if field[yy][xx] != 'c':
        field[yy][xx] = '.'
    for nei in surroundings(p, r, c):
        y, x = nei
        if field[y][x] == '*':
            field[y][x] = '.'
            cnt += 1
            fr += [(y, x)]

    if cnt == 0:
        return None
    return field, n+cnt, fringe.union(set(fr))

def display(field):
    for row in field:
        print "".join(row)

def sweep(f):
    r, c, m = readints(f)
    target = r*c - m

    mines = [['*']*c for i in xrange(r)]

    mines[0][0] = 'c'
    stack = [(mines, 1, set())]
    someState = reveal((0,0), mines, 1, surroundings((0,0), r, c))
    if someState is not None:
        stack += [someState]

    while len(stack) > 0:
        state = stack.pop()
        field, n, fringe = state
        # display(field)
        if n == target:
            display(field)
            return
        elif n > target:
            continue
        # print "======="
        #display(field)


        for p in fringe:
            newFringe = fringe.copy()
            newFringe.remove(p)
            newState = reveal(p, field, n, newFringe)
            if newState is not None:
                stack += [newState]

    print "Impossible"

if __name__ == "__main__":
    f = open(sys.argv[1], "r")
    numCases = readint(f)
    for i in xrange(numCases):
        print "Case #%d:" % (i + 1)
        sweep(f)
