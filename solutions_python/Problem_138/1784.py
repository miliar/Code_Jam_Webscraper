import os
import unittest
from decimal import Decimal
from copy import deepcopy

PROB_NAME = 'war'
INPUT_TYPE = 'small0'


def solve_war(case):
    naomi_blocks, ken_blocks = deepcopy(case)
    naomi_score = 0

    while naomi_blocks:
        naomi_block = min(naomi_blocks)
        naomi_blocks.remove(naomi_block)
        winning_blocks = [block for block in ken_blocks if block > naomi_block]
        if winning_blocks:
            ken_block = min(winning_blocks)
        else:
            ken_block = min(ken_blocks)
        ken_blocks.remove(ken_block)
        if naomi_block > ken_block:
                naomi_score += 1

    return naomi_score


def solve_dwar(case):
    naomi_blocks, ken_blocks = deepcopy(case)
    naomi_score = 0

    while naomi_blocks:
        if max(naomi_blocks) > max(ken_blocks):
            naomi_blocks.remove(max(naomi_blocks))
            ken_blocks.remove(max(ken_blocks))
            naomi_score += 1
        else:
            naomi_blocks.remove(min(naomi_blocks))
            ken_blocks.remove(max(ken_blocks))

    return naomi_score


def solve(case):
    """break 'case', solve and return the solution"""
    return "{} {}".format(solve_dwar(case), solve_war(case))


def read_case(lines):
    lines.pop(0)
    naomi = [Decimal(num) for num in lines.pop(0).split()]
    ken = [Decimal(num) for num in lines.pop(0).split()]
    return (naomi, ken)


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


def main(infile, outfile):
    cases = read_file(infile)
    results = [solve(case) for case in cases]
    write_results(results, outfile)


if INPUT_TYPE:
    main(os.path.join('io', '{}_{}.in'.format(PROB_NAME, INPUT_TYPE)),
         os.path.join('io', '{}_{}.out'.format(PROB_NAME, INPUT_TYPE)))


class UnitTest(unittest.TestCase):
    CASES = {}

    def runTest(self):
        message = 'Wrong result for case.\nCase: {}\nResult: {}\n'\
                  'Expected result: {}'
        for case, result in self.CASES.iteritems():
            self.assertEqual(solve(case), result, message.format(case,
                                                                 solve(case),
                                                                 result))
