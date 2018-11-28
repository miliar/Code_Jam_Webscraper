import os
from itertools import product
from collections import defaultdict

PROB_NAME = 'lawnmower'
INPUT_TYPE = 'large'


class Cell(object):
    def __init__(self, h, max_left=None, max_right=None, max_up=None,
                 max_down=None):
        self.h = h
        self.max_left = max_left
        self.max_right = max_right
        self.max_up = max_up
        self.max_down = max_down


class Grid(defaultdict):
    def __init__(self):
        super(Grid, self).__init__(lambda: Cell(0))

    def get_max_left(self, i, j):
        cell = self[i, j]
        left = self[i, j - 1]
        if left.h == 0:
            return 0
        if left.max_left is not None:
            max_left = left.max_left
        else:
            max_left = self.get_max_left(i, j - 1)
        cell.max_left = max(max_left, left.h)
        return cell.max_left

    def get_max_right(self, i, j):
        cell = self[i, j]
        right = self[i, j + 1]
        if right.h == 0:
            return 0
        if right.max_right is not None:
            max_right = right.max_right
        else:
            max_right = self.get_max_right(i, j + 1)
        cell.max_right = max(max_right, right.h)
        return cell.max_right

    def get_max_up(self, i, j):
        cell = self[i, j]
        up = self[i - 1, j]
        if up.h == 0:
            return 0
        if up.max_up is not None:
            max_up = up.max_up
        else:
            max_up = self.get_max_up(i - 1, j)
        cell.max_up = max(max_up, up.h)
        return cell.max_up

    def get_max_down(self, i, j):
        cell = self[i, j]
        down = self[i + 1, j]
        if down.h == 0:
            return 0
        if down.max_down is not None:
            max_down = down.max_down
        else:
            max_down = self.get_max_down(i + 1, j)
        cell.max_down = max(max_down, down.h)
        return cell.max_down


def solve(case):
    """break 'case', solve and return the solution"""
    grid, n, m = case
    for i, j in product(range(n), range(m)):
        cell = grid[(i, j)]
        horizontal = grid.get_max_left(i, j) > cell.h or \
                     grid.get_max_right(i, j) > cell.h
        vertical = grid.get_max_up(i, j) > cell.h or \
                   grid.get_max_down(i, j) > cell.h
        if vertical and horizontal:
#            print i, j, 'is to blame'
#            print grid.get_max_left(i, j), grid.get_max_right(i, j)
#            print grid.get_max_up(i, j), grid.get_max_down(i, j)
            return 'NO'
    return 'YES'


def print_debug(cases, results):
    for idx, case in enumerate(cases):
        print 'Case #{}: {}'.format(idx + 1, results[idx])
        grid, n, m = case
        for i in range(n):
            for j in range(m):
                print grid[i, j].h,
            print
        print '\n'


def read_file(filepath):
    """Read the input file and return a list of cases in a tuple format."""
    cases = []
    with open(filepath, 'rt') as fobj:
        lines = fobj.readlines()
        num_cases = int(lines.pop(0))
        for case in range(num_cases):
            grid = Grid()
            n, m = (int(i) for i in lines.pop(0).split())
            for i in range(n):
                line = lines.pop(0)
                for j, h in enumerate(line.split()):
                    grid[(i, int(j))] = Cell(int(h))
            cases.append((grid, n, m))
    return cases


def write_results(results, outfile):
    with open(outfile, 'wt') as f:
        for idx, result in enumerate(results):
            f.write('Case #{}: {}\n'.format(idx + 1, result))


def main(infile, outfile):
    cases = read_file(infile)
    results = [solve(case) for case in cases]
    print_debug(cases, results)
    write_results(results, outfile)

main(os.path.join('io', '{}_{}.in'.format(PROB_NAME, INPUT_TYPE)),
     os.path.join('io', '{}_{}.out'.format(PROB_NAME, INPUT_TYPE)))
