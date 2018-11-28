#!/usr/bin/env pypy

import collections
import itertools


_Cell = collections.namedtuple('Cell', 'board i j')
class Cell(_Cell):
    def __repr__(self):
        return 'Cell[%d, %d] = %s' % (self.i, self.j, self.value)

    @property
    def value(self):
        return self.board.matrix[self.i][self.j]

    def test_win(self, direction):
        cells = [self]
        while len(cells) < 4:
            next = getattr(cells[-1], direction)()
            if not next:
                return False
            cells.append(next)
        values = set(cell.value for cell in cells)
        if len(values) == 1:
            return cells[0].value
        elif len(values) == 2 and 'T' in values:
            return [v for v in values if v != 'T'][0]
        return False

    def up(self):
        if self.i == 0: return None
        return Cell(self.board, self.i - 1, self.j)

    def down(self):
        if self.i == 3: return None
        return Cell(self.board, self.i + 1, self.j)

    def left(self):
        if self.j == 0: return None
        return Cell(self.board, self.i, self.j - 1)

    def right(self):
        if self.j == 3: return None
        return Cell(self.board, self.i, self.j + 1)

    def movseq(*movements):
        def method(cell):
            for mov in movements:
                cell = getattr(cell, mov)()
                if cell is None:
                    return
            return cell
        return method

    upleft = movseq('up', 'left')
    upright = movseq('up', 'right')
    downleft = movseq('down', 'left')
    downright = movseq('down', 'right')

    del movseq


class Board(object):
    def __init__(self):
        self.matrix = [[None] * 4 for _ in xrange(4)]

    def parse(self, input):
        for row in xrange(4):
            line = input.next()
            for col, value in enumerate(list(line[:4])):
                if value != '.':
                    self.matrix[row][col] = value
        input.next()

    def full(self):
        return all(all(val is not None for val in row) for row in self.matrix)

    def perimeter_coords(self):
        top = itertools.product((0,), range(4))
        right = itertools.product(range(4), (3,))
        right.next()
        bottom = itertools.product((3,), range(4)[::-1])
        bottom.next()
        left = itertools.product(range(1, 4)[::-1], (0,))
        left.next()
        return itertools.chain(top, right, bottom, left)

    def perimeter(self):
        for coords in self.perimeter_coords():
            yield Cell(self, *coords)

    def find_winner(self):
        directions = ['up', 'down', 'left', 'right',
                      'upleft', 'upright', 'downleft', 'downright']
        # Account for situations in which both players might have 'won';
        # we know X goes first so in cases where runs of four exist for both
        # players, X gets priority.
        o_might_have_won = False
        for cell in self.perimeter():
            if not cell.value:
                continue
            for direction in directions:
                attempt = cell.test_win(direction)
                if attempt == 'X':
                    return 'X won'
                elif attempt == 'O':
                    o_might_have_won = True
        if o_might_have_won:
            return 'O won'
        if self.full():
            return 'Draw'
        return 'Game has not completed'

if __name__ == '__main__':
    import fileinput
    input = fileinput.input()
    cases = int(input.next())
    for case in xrange(1, cases + 1):
        b = Board()
        b.parse(input)
        print 'Case #%d:' % case, b.find_winner()
