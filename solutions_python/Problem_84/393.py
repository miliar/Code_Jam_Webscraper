import sys
import copy


class SquareFinder(object):
    def solvable(grid):
        """Return True or False, determining whether this square is solvable."""
        pass
    @staticmethod
    def solve(grid):
        """Recursive solver. Returns modified grid if solvable, None otherwise."""
        if SquareFinder.count_brackets(grid) % 4 != 0:
            # unsolvable.
            return
        if SquareFinder.no_brackets(grid):
            # base case.
            return grid
        for upper_left in SquareFinder.find_upper_corners(grid):
            grid_copy = SquareFinder.replace_colour(upper_left, grid)
            solved = SquareFinder.solve(grid_copy)
            if SquareFinder.no_brackets(solved):
                return solved

    @staticmethod
    def replace_colour(upper_left, original_grid):
        r,c = upper_left
        grid = copy.deepcopy(original_grid)
        try:
            grid[r][c]     = '/'
            grid[r][c+1]   = '\\'
            grid[r+1][c]   = '\\'
            grid[r+1][c+1] = '/'
            return grid
        except IndexError:
            print 'unexpected IndexError.'

    @staticmethod
    def find_upper_corners(grid):
        """Find all upper-left corners of # 2x2 squares."""
        upper_lefts = []
        for r, row in zip(xrange(len(grid)), grid[:-1]):
            for c, cell in zip(xrange(len(row)), row[:-1]):
                try:
                    if cell == '#' and ([grid[r][c+1], grid[r+1][c], grid[r+1][c+1]] == ['#','#','#']):
                        yield (r,c)
                except IndexError:
                    continue

    @staticmethod
    def count_brackets(grid):
        c = 0
        for row in grid:
            for cell in row:
                if cell == '#':
                    c += 1
        return c

    @staticmethod
    def no_brackets(grid):
        if not grid:
            return
        for row in grid:
            if '#' in row:
                return False
        return True



class Runner(object):
    def __init__(self, test_case):
        self.test_case = test_case
    def run(self):
        answer = 0
        solved = SquareFinder.solve(self.test_case.grid)
        print 'Case #%d:' % self.test_case.number
        if not solved:
            print 'Impossible'
        else:
            for row in solved:
                print "".join(row)

class TestCase(object):
    def __init__(self, spec_string, number):
        self.grid = spec_string['grid']
        self.number = number

def read_input():
    def test_cases(lines):
        """Generator, yielding test cases."""
        T = int(lines.pop(0))
        for t in xrange(1, T+1):
            R, C = map(int, lines.pop(0).split())
            spec = {}
            spec['t'] = t
            spec['R'] = R
            spec['C'] = C
            spec['grid'] = []
            for r in xrange(R):
                spec['grid'].append([x for x in lines.pop(0).strip()])
            yield (spec, t)

    lines = sys.stdin.readlines()
    return [TestCase(test_case_spec, test_case_number) for test_case_spec, test_case_number in test_cases(lines)]

if __name__ == '__main__':
    test_cases = read_input()
    for test_case in test_cases:
        Runner(test_case).run()
