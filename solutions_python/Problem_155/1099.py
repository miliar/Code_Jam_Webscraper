"""A solution to a Google Code Jam problem.

Each problem is parsed into an arbitrary object (which is different for each
problem). Such objects are called "cases".

To use this template:
1) Implement `read_case(lines)` to parse input lines into a case object.
2) Now that you know how cases look like, write some tests at the bottom of
   the file (copying the sample cases at least).
3) implement `solve(case)` (this is the tricky part!) to return a solution.

Usage:
    gcj [--input=<input> [--output=<output>]]

Options:
    --input=<input-file>        the path to the input file
    --output=<output-file>      the path to the output file

"""

import os
import time
import docopt
import unittest
from contextlib import contextmanager


TEST_CASES = {
    (0, 0, 0, 1, 1, 2, 4, 0, 0, 1): 3,
    (6, 3, 1, 5, 4): 0,
    (0, 1, 0, 1, 0, 1, 0, 1): 4,
    (1, 1, 1, 1, 1): 0,
    (0, 9): 1,
    (1, 1, 0, 0, 1, 1): 2,
    (1,): 0,
}


def solve(case):
    """break 'case', solve and return the solution"""
    audience = case
    total, invited = 0, 0
    for i in range(len(audience)):
        if total < i:
            added = i - total
            invited += added
            total += added
        total += audience[i]
    return invited


def read_case(lines):
    """Read input line into a case object.

    This function should `pop` used lines so that `lines` will be ready to
    parse the next case.

    """
    _, string = lines.pop(0).split()
    return tuple(int(val) for val in string)


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
        with timing("Solving case #{}".format(idx + 1)):
            results.append(solve(case))
    write_results(results, outfile)


test_suite = unittest.TestSuite()
for case, result in TEST_CASES.iteritems():
    message = 'Wrong result for case.\nCase: {}\nResult: {}\n' \
              'Expected result: {}'

    class UnitTest(unittest.TestCase):
        def runTest(self, case=case, result=result):
            self.assertEqual(solve(case),
                             result,
                             message.format(case, solve(case), result))

    test_suite.addTest(UnitTest())

if __name__ == '__main__':
    args = docopt.docopt(__doc__)
    assert len(TEST_CASES) > 0, "Don't be an idiot, write some tests!"
    input = args['--input']
    if input:
        output = args['--output'] or input + '.out'
        print input, output
        main(input, output)
    unittest.TextTestRunner().run(test_suite)
