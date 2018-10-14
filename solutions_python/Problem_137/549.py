#!/usr/bin/env python
# coding: utf-8

import sys
import copy
import random


class Found(BaseException): pass

class Impossible(BaseException): pass

def explore(field, row, column, path=None, mines=None):
    # if field.rows > 2 and field.cols > 2 and (field.size - mines) < 3:
    #     raise Impossible
    # print(field)
    # print(path, sum(field.field), (field.size - mines))
    # raw_input('...')
    if path is None:
        path = [(row, column)]
    # if field.opened > field.size - mines:
    if sum(field.field) > field.size - mines:
        return False
    # if len(path) > field.size:
    #     return False
    if sum(field.field) == (field.size - mines):
    # if field.opened == (field.size - mines):
        # print(field)
        # print(field.size, mines, field.size - mines)
        exception = Found()
        exception.field = field
        raise exception
    neighbors = field.neighbors(row, column, exclude=path)
    for r, c in neighbors:
        path = path + [(r, c)]
        fieldcopy = copy.deepcopy(field)
        fieldcopy.open(row, column)
        for rr, cc in neighbors:
            fieldcopy.open(rr, cc)
        result = explore(fieldcopy, r, c, path=path, mines=mines)


class Field(object):
    OPEN = 1
    NONE = 0

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.size = self.rows * self.cols
        self.field = [Field.NONE for _ in xrange(self.size)]
        self.opened = 0

    def to_index(self, row=0, column=0):
        return (row * self.cols) + column

    def from_index(self, index):
        row = (index // self.cols)
        column = index - (row * self.cols)
        return row, column

    def open(self, row=0, column=0):
        idx = self.to_index(row=row, column=column)
        if not self.field[idx] == Field.OPEN:
            self.opened += 1
            self.field[self.to_index(row=row, column=column)] = Field.OPEN

    def __str__(self):
        rows = []
        for r in xrange(self.rows):
            rows.append(''.join(str(self.field[self.to_index(row=r, column=c)])
                        for c in xrange(self.cols)))
        return '\n'.join(rows)


    def neighbors(self, row, column, exclude=None):
        if exclude is None:
            exclude = set()
        nodes = [(row - 1, column - 1),
                 (row - 1, column),
                 (row - 1, column + 1),
                 (row, column - 1),
                 (row, column),
                 (row, column + 1),
                 (row + 1, column - 1),
                 (row + 1, column),
                 (row + 1, column + 1)]
        return [(r, c) for r, c in nodes if
                r >= 0 and c >= 0
                and r < self.rows and c < self.cols
                and not (r == row and c == column)
                and (r, c) not in exclude]

    def _print(self, start_row, start_column):
        rows = []
        for r in xrange(self.rows):
            row = []
            for c in xrange(self.cols):
                if r == start_row and c == start_column:
                    row.append('c')
                elif self.field[self.to_index(row=r, column=c)] == 1:
                    row.append('.')
                else:
                    row.append('*')
            rows.append(''.join(row))
        return '\n'.join(rows)


if __name__ == '__main__':
    with open('C-small-attempt1.in') as handle:
        _ = handle.next()
        for case, line in enumerate(handle, start=1):
            rows, cols, mines = map(int, line.strip().split(' '))

            field = Field(rows, cols)
            
            print('Case #%s:' % case)
            if (rows * cols) - 1 == mines:
                print(field._print(0, 0))           
                continue

            start = (None, None)
            try:
                field = Field(rows, cols)
                if field.rows > 3 and field.cols > 3 and (field.size - mines) < 3:
                    raise Impossible
                positions = []
                for i in xrange(rows):
                    for j in xrange(cols):
                        positions.append((i, j))
                for i, j in positions:
                    start = (i, j)
                    try:
                        explore(field, i, j, mines=mines)
                    except Impossible:
                        pass
            except Found as exc:
                # print(field)
                field = exc.field
                r, c = start
                print(field._print(r, c))
            except Impossible:
                print('Impossible')
            else:
                print('Impossible')


