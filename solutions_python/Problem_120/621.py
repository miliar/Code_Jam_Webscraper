import os
from math import sqrt

PROB_NAME = 'bullseye'
INPUT_TYPE = 'small'


def solve(case):
    """break 'case', solve and return the solution"""
    r, t = case
    paint = t

    a1 = (r + 1) ** 2 - r ** 2
    return int(0.25 * (sqrt(a1 ** 2 - 4 * a1 + 8 * t + 4) - a1 + 2))


def read_file(filepath):
    """Read the input file and return a list of cases in a tuple format."""
    cases = []
    with open(filepath, 'rt') as fobj:
        lines = fobj.readlines()
        num_cases = int(lines.pop(0))
        for case in range(num_cases):
            # read each case here
            r, t = [int(num) for num in lines.pop(0).split()]
            cases.append((r, t))
    return cases


def write_results(results, outfile):
    with open(outfile, 'wt') as f:
        for idx, result in enumerate(results):
            f.write('Case #{}: {}\n'.format(idx + 1, result))


def main(infile, outfile):
    cases = read_file(infile)
    results = [solve(case) for case in cases]
    write_results(results, outfile)

main(os.path.join('io', '{}_{}.in'.format(PROB_NAME, INPUT_TYPE)),
     os.path.join('io', '{}_{}.out'.format(PROB_NAME, INPUT_TYPE)))
