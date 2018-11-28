#!/usr/bin/env python
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
            print "Case #{0}: {1}".format(index + 1, result)
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


class Solution(Problem):

    SAMPLE = """3
2 0
1 1
o 1 1
3 4
+ 2 3
+ 2 1
x 3 1
+ 2 2"""

    @staticmethod
    def to_internal(models):
        plus = set()
        x = set()

        for mtype, R, C in models:
            if mtype in ('+', 'o'):
                plus.add((R-1, C-1))
            if mtype in ('x', 'o'):
                x.add((R-1, C-1))

        return plus, x

    @staticmethod
    def from_internal(plus, x):
        models = []

        for R, C in plus:
            if (R, C) in x:
                models.append(('o', R+1, C+1))
                x.remove((R, C))
            else:
                models.append(('+', R+1, C+1))

        for R, C in x:
            models.append(('x', R+1, C+1))

        return models

    def solve(self, case):
        N, models = case
        initial = models
        plus, x = self.to_internal(models)

        N_range = set(xrange(N))
        free_rows = N_range.difference(R for R, C in x)
        free_columns = N_range.difference(C for R, C in x)
        for R in free_rows:
            x.add((R, free_columns.pop()))

        forbids = {}
        for R in xrange(N):
            for C in xrange(N):
                adjacent = set()
                for delta in xrange(-N+1, N):
                    r = R + delta
                    c = C + delta
                    if 0 <= r < N and 0 <= c < N:
                        adjacent.add((r, c))
                    c = C - delta
                    if 0 <= r < N and 0 <= c < N:
                        adjacent.add((r, c))
                forbids[(R, C)] = adjacent

        for RC in plus:
            forbidden = forbids[RC]
            for rc in forbidden:
                forbids.pop(rc, None)

        while forbids:
            RC, optimal = min(forbids.iteritems(),
                              key=lambda it: (len(it[1]), it[0]))
            plus.add(RC)
            for rc in optimal:
                forbids.pop(rc, None)

        score = len(plus) + len(x)
        models = frozenset(self.from_internal(plus, x))
        added = models.difference(initial)

        report = ["{} {}".format(score, len(added))]
        report.extend(' '.join(str(item) for item in model)
                      for model in added)
        return '\n'.join(report)

    def parse_case(self, lines):
        N, M = map(int, lines.next().split())
        models = []

        for i in range(M):
            mtype, R, C = lines.next().split()
            models.append((mtype, int(R), int(C)))

        return N, models


if __name__ == '__main__':
    Solution.main()
