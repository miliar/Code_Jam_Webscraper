#!/usr/bin/python

from __future__ import print_function
import sys
from collections import defaultdict

def solve(R, C, M):
    F = R*C - M
    if F == 1:
        return field(R, C, '*').clone_set(0, 0, 'c')
    else:
        res = presolve(R, C)
        if F not in res:
            return None
        else:
            return res[F].pop().clone_set(0, 0, 'c')

def presolve(R, C):
    solutions = defaultdict(set)
    seen_fields = set()

    def r(R, C, state, level):
#        print(state.field, "\n", level, state.get_free_cnt(), "\n", state.border)
#        raw_input()
        solutions[ state.get_free_cnt() ].add( state.field )
        if state.field not in seen_fields:
            for cell in state.get_border():
                r(R, C, state.clone_remove_border(cell), level+1)
                r(R, C, state.clone_set_zero(cell), level+1)
            seen_fields.add(state.field)

    state = State.make(R, C)
    state.set_zero((0, 0))
    r(R, C, state, level=0)

    return solutions

class State(object):
    def __init__(self, field, free_cnt, max_row, max_col, border):
        self.field = field
        self.free_cnt = free_cnt
        self.max_row = max_row
        self.max_col = max_col
        self.border = border

    @classmethod
    def make(cls, rows, cols):
        return cls(
            field = field(rows, cols, '*'),
            free_cnt = 0,
            max_row = 0,
            max_col = 0,
            border = set([(0, 0)]),
        )

    def clone(self):
        return State(
            field = self.field.clone(),
            free_cnt = self.free_cnt,
            max_row = self.max_row,
            max_col = self.max_col,
            border = set(self.border),
        )

    def get_free_cnt(self):
        return self.free_cnt

    def get_bounding_box(self):
        return (self.max_row + 1, self.max_col + 1)

    def get_border(self):
        return self.border

    def set_zero(self, cell):
        self.border.remove(cell)
        new_border = []
        for row, col in get_neighbours(cell, self.field.size()):
            if self.field.get(row, col) == '*':
                self.field.set(row, col, '.')
                self.free_cnt += 1
                self.max_row = max(self.max_row, row)
                self.max_col = max(self.max_col, col)
                new_border.append((row, col))

        for cell in new_border:
            if any(self.field.get(row, col) == '*' for row, col in get_neighbours(cell, self.field.size())):
                self.border.add(cell)

    def remove_border(self, cell):
        self.border.remove(cell)

    def clone_set_zero(self, cell):
        s = self.clone()
        s.set_zero(cell)
        return s

    def clone_remove_border(self, cell):
        s = self.clone()
        s.remove_border(cell)
        return s

def get_neighbours((row0, col0), (rows, cols)):
    for row in range(row0-1, row0+2):
        for col in range(col0-1, col0+2):
            if 0 <= row < rows and 0 <= col < cols:
                yield (row, col)

class Field(object):
    def __init__(self, field):
        self.field = field

    def __nonzero__(self):
        return bool(self.field)

    def __iter__(self):
        return iter(self.field)

    def __repr__(self):
        return 'Field({!r})'.format(self.field)

    def __str__(f):
        return "\n".join("".join(row) for row in f)

    def __eq__(self, other):
        return self.field == other.field

    def __hash__(self):
        return hash(str(self))

    def size(self):
        rows = len(self.field)
        if rows:
            cols = len(self.field[0])
        else:
            cols = 0
        return (rows, cols)

    def get(self, row, col):
        return self.field[row][col]

    def set(self, r, c, v):
        self.field[r][c] = v

    def clone(self):
        return Field([list(row) for row in self])

    def clone_set(self, r, c, v):
        f2 = self.clone()
        f2.set(r, c, v)
        return f2

    def clone_replace(self, r, c, v1, v2):
        if self.field[r][c] == v1:
            return self.set(r, c, v2)
        else:
            raise Exception('Failed replace')

    def clone_transpose(self):
        R = len(self.field)
        new = defaultdict(lambda: [None]*R)
        for r, row in enumerate(self.field):
            for c, v in enumerate(row):
                new[c][r] = v
        return Field([row for r, row in sorted(new.items())])

def null():
    return Field([])

def field(r, c, f):
    return Field([[f for x in range(c)] for x in range(r)])

"""
def solve(R, C, M):
    '''
    >>> print(solve(5, 33, 0).replace(0, 0, '.', '-'))
    -...............................c
    .................................
    .................................
    .................................
    .................................
    >>> print(solve(1, 5, 1))
    *...c
    >>> print(solve(1, 5, 3))
    ***.c
    >>> print(solve(1, 5, 4))
    ****c
    >>> print(solve(1, 5, 5))
    <BLANKLINE>
    >>> print(solve(7, 2, 0))
    ..
    ..
    ..
    ..
    ..
    ..
    c.
    >>> print(solve(7, 2, 1))
    <BLANKLINE>
    >>> print(solve(7, 2, 2))
    <BLANKLINE>
    >>> print(solve(7, 2, 3))
    <BLANKLINE>
    >>> print(solve(2, 7, 4))
    **....c
    **.....
    >>> print(solve(2, 7, 5))
    <BLANKLINE>
    >>> print(solve(2, 7, 6))
    ***...c
    ***....
    >>> print(solve(2, 7, 10))
    *****.c
    *****..
    '''
    if R < C:
        return solve(C, R, M).transpose()

    else:
        if M == 0:
            return field(R, C, '.').set(R-1, 0, 'c')

        elif M == R*C:
            return null()

        elif M == R*C - 1:
            return field(R, C, '*').set(R-1, 0, 'c')

        elif C == 1:
            f = field(R, C, '.').set(R-1, 0, 'c')
            for x in range(M):
                f = f.set(x, 0, '*')
            return f

        elif C == 2:
            if M < 4 or M % 2 != 0:
                return null()
            else:
                f = field(R, C, '.').set(R-1, 0, 'c')
                for r in range(M // 2):
                    f = f.set(r, 0, '*').set(r, 1, '*')
                return f

        elif C == 3:
            raise NotImplemented()

        else:
            raise NotImplemented()
"""

def main():
    T = int(next(sys.stdin))
    for x in range(1, T+1):
        R, C, M = (int(x) for x in next(sys.stdin).split())
        res = solve(R, C, M)
#        print("Case #{}:\n{}".format(x, (R, C, M)))
        if not res:
            print("Case #{}:\nImpossible".format(x))
        else:
            print("Case #{}:\n{}".format(x, res))

if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    main()

