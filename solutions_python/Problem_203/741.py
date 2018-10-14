import argparse
import itertools
import multiprocessing
import sys
import time


def global_solve(index):
    """A dirty way to get around pickling limitations when multiprocessing."""
    return global_solve.instance.solve_single(index)


class Problem(object):
    """
    A simple helper class for parsing Google Code Jam problem inputs and
    formatting solutions.

    It also allows paralellizing tasks by multiprocessing in order to work
    around Python's limited (due to GIL) threading.

    (C) Vytautas Liuolia 2016-2017
    """

    SAMPLE = None

    def __init__(self):
        self.cases = []

    def parse_case(self, lines):
        raise NotImplementedError

    def solve(self, case):
        raise NotImplementedError

    def solve_single(self, index):
        start = time.time()
        result = str(self.solve(self.cases[index]))
        elapsed = time.time() - start
        return result, elapsed

    def read_cases(self, lines=None):
        if lines is None:
            lines = (line.strip() for line in sys.stdin)
        amount = int(lines.next())
        for index in xrange(amount):
            self.cases.append(self.parse_case(lines))

    def solve_all(self, processes=None, verbose=False):

        indices = xrange(len(self.cases))
        processes = processes or multiprocessing.cpu_count()

        if processes > 1:
            global_solve.instance = self
            pool = multiprocessing.Pool(processes=processes)
            results = pool.imap(global_solve, indices)
        else:
            results = itertools.imap(self.solve_single, indices)

        for index, (result, elapsed) in enumerate(results):
            if verbose:
                message = "Solved case #{0} in {1} s\n".format(
                    index + 1, round(elapsed, 6))
                sys.stderr.write(message)
                sys.stderr.flush()
            print "Case #{0}:\n{1}".format(index + 1, result)
            sys.stdout.flush()

    @classmethod
    def main(cls):
        parser = argparse.ArgumentParser(
            description='Reads Code Jam problem input and outputs solutions.')
        parser.add_argument(
            '-s', '--sample', action='store_true',
            help='run the predefined sample instead of input')
        parser.add_argument(
            '-v', '--verbose', action='store_true',
            help='print progress information in stderr')
        parser.add_argument(
            '-p', '--processes', type=int, default=0,
            help='amount of processes to use (default: CPU count)')
        args = parser.parse_args()

        lines = None
        if args.sample:
            if cls.SAMPLE is None:
                raise NotImplementedError
            lines = iter(cls.SAMPLE.splitlines())

        problem = cls()
        problem.read_cases(lines)
        problem.solve_all(processes=args.processes, verbose=args.verbose)


class Rectangle(object):

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def overlaps(self, other):
        if other is self:
            return False
        if (self.x1 > other.x2) or (self.x2 < other.x1):
            return False
        if (self.y1 > other.y2) or (self.y2 < other.y1):
            return False
        return True

    def copy(self):
        return Rectangle(self.x1, self.y1, self.x2, self.y2)

    def include(self, x, y):
        if x < self.x1:
            self.x1 = x
        if y < self.y1:
            self.y1 = y
        if x > self.x2:
            self.x2 = x
        if y > self.y2:
            self.y2 = y

    def __repr__(self):
        return "Rectangle{}".format((self.x1, self.y1, self.x2, self.y2))


class Solution(Problem):

    SAMPLE = """3
3 3
G??
?C?
??J
3 4
CODE
????
?JAM
2 2
CA
KE"""

    def solve(self, case):
        R, C, grid = case

        grid = [list(item) for item in grid]
        rects = {}

        for r in xrange(R):
            for c in xrange(C):
                letter = grid[r][c]
                if letter != '?':
                    if letter in rects:
                        rects[letter].include(r, c)
                    else:
                        rects[letter] = Rectangle(r, c, r, c)

        while True:
            expanded = False

            for letter, rect in rects.items():
                if rect.x1 > 0:
                    current = rect.copy()
                    current.x1 -= 1
                    if not any(r.overlaps(current) for r in rects.itervalues()
                               if r is not rect):
                        expanded = True
                        rects[letter] = current
                        break

                if rect.y1 > 0:
                    current = rect.copy()
                    current.y1 -= 1
                    if not any(r.overlaps(current) for r in rects.itervalues()
                               if r is not rect):
                        expanded = True
                        rects[letter] = current
                        break

                if rect.x2 < R-1:
                    current = rect.copy()
                    current.x2 += 1
                    if not any(r.overlaps(current) for r in rects.itervalues()
                               if r is not rect):
                        expanded = True
                        rects[letter] = current
                        break

                if rect.y2 < C-1:
                    current = rect.copy()
                    current.y2 += 1
                    if not any(r.overlaps(current) for r in rects.itervalues()
                               if r is not rect):
                        expanded = True
                        rects[letter] = current
                        break

            if not expanded:
                break

        for letter, rect in rects.iteritems():
            for r in xrange(rect.x1, rect.x2+1):
                for c in xrange(rect.y1, rect.y2+1):
                    grid[r][c] = letter

        return '\n'.join(''.join(row) for row in grid)

    def parse_case(self, lines):
        R, C = map(int, lines.next().split())
        return (R, C, [lines.next() for row in xrange(R)])


if __name__ == '__main__':
    Solution.main()
