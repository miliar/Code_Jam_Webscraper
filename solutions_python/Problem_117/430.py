#!/usr/local/bin/python2.7
from __future__ import print_function
import unittest
import sys

sin = '''5
3 3
2 1 2
1 1 1
2 1 2
5 5
2 2 2 2 2
2 1 1 1 2
2 1 2 1 2
2 1 1 1 2
2 2 2 2 2
1 3
1 2 1
8 4
1 2 1 2
2 2 2 2
2 1 2 1
2 1 1 1
1 2 2 1
1 2 1 2
1 1 2 1
2 1 2 1
8 7
2 2 2 2 2 2 2
2 2 2 2 2 2 2
2 2 1 2 2 2 2
2 2 2 2 2 2 2
2 2 2 2 2 2 2
2 2 2 2 2 2 2
2 2 2 2 2 2 2
2 2 2 2 2 2 2'''

sout = '''Case #1: YES
Case #2: NO
Case #3: YES '''

def err(*msgs, **argv):
    print(*msgs, file=sys.stderr, **argv)

##==============================
##==============================


class Square(object):
    N = M = 1
    def __init__(self, i, j, h):
        self.i = i
        self.j = j
        self.h = h
        N, M = Square.N, Square.M

    def yes(self, lawn):
        h = lawn[self.i]
        v = [lawn[c][self.j] for c in range(self.N)]

        if max([s.h for s in h]) <= self.h or max([s.h for s in v]) <= self.h:
            return True
        return False

    def __eq__(self, other):
        return self.i == other.i and self.j == other.j

    def __repr__(self):
        return repr(self.h)

def solveCase(lawn, N, M):
    for i in range(N):
        for j in range(M):
            if lawn[i][j].yes(lawn):
                continue
            else:
                return 'NO'
    return 'YES'


def solveAll(s):
    it = iter(s.split('\n'))
    T = int(it.next())
    for i in range(T):
        N, M = map(int, it.next().split(' '))
        Square.N, Square.M = N, M
        lawn = []
        for j in range(N):
            heights = map(int, it.next().split(' '))
            lawn.append([Square(j, m, heights[m]) for m in range(M)])
        yield('Case #%s: %s' % (i + 1, solveCase(lawn, N, M)))


def test():
    print('\n'.join(solveAll(sin)))


if __name__ == '__main__':
    if not sys.argv[1:]:
        test()
        sys.exit(0)
    fn = sys.argv[1]
    print('\n'.join(solveAll(open(fn).read())))
