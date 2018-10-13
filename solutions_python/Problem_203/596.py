#!/usr/bin/env python

import os
import sys
import time
from multiprocessing import Pool

NUM_PROCESSES = 12

class Stopwatch(object):
    def __init__(self):
        self.start_ts = time.time()

    def end_and_print(self):
        print '{0}s'.format(time.time() - self.start_ts)


class Region(object):
    def __init__(self, l, x, y, w, h):
        self.l = l
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def signature(self):
        return self.l, self.x, self.y, self.w, self.h

    def __hash__(self):
        return hash(self.signature())

    def __eq__(self, other):
        return self.signature() == other.signature()


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Cell(object):
    def __init__(self, l, x, y):
        self.l = l if l != '?' else None
        self.x = x
        self.y = y
        self.stack = []

    def push(self):
        self.stack.append(self.l)

    def pop(self):
        self.l = self.stack.pop()

    def letter(self):
        return self.l if self.l else '?'


class Grid(object):
    def __init__(self, r, c, grid_lines):
        self.r = r
        self.c = c
        self.n = r * c
        self.letters = set([letter for line in grid_lines for letter in line if letter != '?'])
        self.grid = []
        for y, row in enumerate(grid_lines):
            self.grid.append([])
            for x, l in enumerate(row):
                self.grid[y].append(Cell(l, x, y))
        self.cells = [c for row in self.grid for c in row]

    def __str__(self):
        lines = []
        for row in self.grid:
            lines.append(''.join([c.letter() for c in row]))
        return '\n'.join(lines)

    def push(self):
        for c in self.cells:
            c.push()

    def pop(self):
        for c in self.cells:
            c.pop()

    def solve(self):
        self.__solve(0)

    def __solve(self, idx):
        if idx >= self.n:
            return True
        if self.cells[idx].l:
            return self.__solve(idx+1)
        for l in self.letters:
            self.push()
            self.cells[idx].l = l
            if self.__fill(idx) and self.__solve(idx+1):
                return True
            self.pop()
        return False

    def __fill(self, idx):
        letter = self.cells[idx].l
        all_cells_of_letter = [c for c in self.cells if c.l == letter]
        xs = [c.x for c in all_cells_of_letter]
        ys = [c.y for c in all_cells_of_letter]
        for x in xrange(min(xs), max(xs)+1):
            for y in xrange(min(ys), max(ys)+1):
                if not self.grid[y][x].l:
                    self.grid[y][x].l = letter
                elif self.grid[y][x].l != letter:
                    return False
        return True

class Spec(object):
    def __init__(self, r, c, grid):
        self.r = r
        self.c = c
        self.grid = grid

def solution(spec):
    grid = Grid(spec.r, spec.c, spec.grid)
    grid.solve()
    return grid

if __name__ == '__main__':
    stopwatch = Stopwatch()
    in_filename = sys.argv[1]
    out_filename = os.path.splitext(in_filename)[0] + '.out'
    with open(in_filename, 'r') as in_f, open(out_filename, 'w') as out_f:
        num_tests = int(in_f.readline())
        specs = []
        for idx in xrange(num_tests):
            first_line = in_f.readline()
            r, c = [int(s) for s in first_line.split()]
            grid = []
            for _ in xrange(r):
                grid.append(in_f.readline().strip())
            specs.append(Spec(r, c, grid))
            print '{0} initialized'.format(idx)
        p = Pool(processes=NUM_PROCESSES)
        results = p.map(solution, specs)
        #results = [solution(s) for s in specs]
        for idx, r in enumerate(results):
            result = 'Case #{0}:\n'.format(idx + 1) + str(r)
            print result
            out_f.write(result + '\n')
    stopwatch.end_and_print()