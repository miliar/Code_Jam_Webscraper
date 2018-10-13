import os
import unittest

from itertools import chain

PROB_NAME = 'magic_trick'
INPUT_TYPE = 'small'


def solve(case):
    """break 'case', solve and return the solution"""
    row1, deal1, row2, deal2 = case
    possible_cards = set(deal1[row1 - 1]) & set(deal2[row2 - 1])
    if len(possible_cards) > 1:
        return "Bad magician!"
    elif len(possible_cards) == 1:
        return possible_cards.pop()
    else:
        return "Volunteer cheated!"


def read_case(lines):
    case = []
    for _ in range(2):
        case.append(int(lines.pop(0)))
        deal = []
        for _ in range(4):
            deal.append([int(card) for card in lines.pop(0).split()])
        case.append(deal)
    return case


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
