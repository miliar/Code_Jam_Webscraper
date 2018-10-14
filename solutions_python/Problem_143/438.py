import os
import time
import unittest
from contextlib import contextmanager


PROB_NAME = 'lottery'
INPUT_TYPE = 'small'


def solve(case):
    """break 'case', solve and return the solution"""
    a, b, k = case
    print "Case: ", a, b, k
    count = 0
    for i in range(a):
        for j in range(b):
            if i & j < k:
                count += 1
            print
    return count


def read_case(lines):
    return [int(num) for num in lines.pop(0).split()]


def read_file(filepath):
    """Read the input file and return a list of cases in a tuple format."""
    cases = []
    with open(filepath, 'rt') as fobj:
        lines = fobj.readlines()
        num_cases = int(lines.pop(0))
        for _ in range(num_cases):
            cases.append(read_case(lines))
    return cases


def write_results(results, outfile):
    with open(outfile, 'wt') as f:
        for idx, result in enumerate(results):
            f.write('Case #{}: {}\n'.format(idx + 1, result))


@contextmanager
def timing(prefix):
    start = time.time()
    yield
    print '{} took {} seconds.'.format(prefix, time.time() - start)


def main(infile, outfile):
    cases = read_file(infile)
    results = []
    for idx, case in enumerate(cases):
        with timing("Solving case #{}".format(idx)):
            results.append(solve(case))
    write_results(results, outfile)


class UnitTest(unittest.TestCase):
    CASES = {(3, 4, 2): 10,
             (4, 5, 2): 16,
             (7, 8, 5): 52,
             (45, 56, 35): 2411,
             (103, 143, 88): 14377}

    def runTest(self):
        message = 'Wrong result for case.\nCase: {}\nResult: {}\n'\
                  'Expected result: {}'
        for case, result in self.CASES.iteritems():
            self.assertEqual(solve(case), result, message.format(case,
                                                                 solve(case),
                                                                 result))

if __name__ == '__main__':
    assert len(UnitTest.CASES) > 0, "Don't be an idiot, write some tests!"
    if INPUT_TYPE:
        main(os.path.join('io', '{}_{}.in'.format(PROB_NAME, INPUT_TYPE)),
             os.path.join('io', '{}_{}.out'.format(PROB_NAME, INPUT_TYPE)))
    unittest.main()
