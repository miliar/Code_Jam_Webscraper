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
2525 1
2400 5
300 2
120 60
60 90
100 2
80 100
70 10
"""

    def solve(self, case):
        D, horses = case
        slowest = max((D - K) / float(S) for K, S in horses)
        return D / slowest

    def parse_case(self, lines):
        D, N = map(int, lines.next().split())
        horses = []
        for horse in xrange(N):
            horses.append(map(int, lines.next().split()))
        return D, horses


if __name__ == '__main__':
    Solution.main()
