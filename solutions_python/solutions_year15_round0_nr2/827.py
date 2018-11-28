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
import copy

import os
import time
import math
import docopt
import unittest
from contextlib import contextmanager


TEST_CASES = {
    (3,): 3,
    (1, 2, 1, 2): 2,
    (4,): 3,
    (3, 4): 4,
    (9, 9, 9, 9): 9,
    (2, 6, 5, 4): 6,
    (2, 2, 3): 3,
    (9, 9, 9, 9, 9): 9,
    (3, 1, 7): 5,
    (6, 6): 5,
    (7, 7, 4): 6,
    (5, 3, 4, 1): 5,
    (4, 4, 3, 2, 1): 4,
    (6, 6, 6, 6, 9, 9): 8,
    (4, 4, 6, 4): 5,
    (1, 8, 8, 9): 8,
    (5, 8, 8, 6): 8,
    (8, 5, 2): 6,
    (2, 1): 2,
    (4, 8): 5,
    (5, 5): 5,
    (4, 9): 6,
    (2, 4, 1, 3, 1): 4,
    (9, 7): 7,
    (3, 3, 3, 4, 3): 4,
    (6, 1, 7): 6,
    (10, 10, 1): 7,
    (11, 11, 1): 8,
    (9, 8): 7,
    (3, 3, 5, 5, 9, 9): 7,
    (7, 6, 4): 6,
    (8, 8): 6,
    (8, 1, 5): 6,
    (9, 9, 9): 8,
    (8, 8, 8): 7,
    (2, 9, 9, 9, 3, 3): 8,
    (1, 2, 8): 5,
    (7, 9, 8, 5): 8,
    (8, 1, 8): 6,
    (9, ): 5,
    (11, ): 6,
}


def solve(case, level=0):
    """break 'case', solve and return the solution"""
    plates = list(case)
    plates.sort(reverse=True)
    max_plate = plates[0]
    min_time = max_plate
    if len(plates) >= max_plate and plates[max_plate - 1] == max_plate:
        return max_plate
    naive_time = max_plate
    if naive_time < min_time:
        min_time = naive_time
    if max_plate <= 2:
        return min_time
    for i in range(2, int(math.sqrt(max_plate)) + 1):
        new_plates = plates[:]
        new_plates.pop(0)
        for j in range(i - max_plate % i):
            new_plates.append(max_plate / i)
        for j in range(max_plate % i):
            new_plates.append(max_plate / i + 1)
        min_time = min(min_time, solve(new_plates, level + 1) + i - 1)
    """
        if max_plate == 9:
            plates.pop(0)
            plates.extend([3, 3, 3])
            current_time += 1
        else:
            a, b = max_plate / 2, max_plate / 2 + max_plate % 2
            plates.pop(0)
            plates.append(a)
            plates.append(b)
        # plates = [plate - 1 for plate in plates]
        # current_time += 2
        current_time += 1
    """

    return min_time


def read_case(lines):
    """Read input line into a case object.

    This function should `pop` used lines so that `lines` will be ready to
    parse the next case.

    """
    lines.pop(0)
    return (int(val) for val in lines.pop(0).split())


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
        main(input, output)
    unittest.TextTestRunner().run(test_suite)
