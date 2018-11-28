import os
import unittest
from collections import defaultdict

PROB_NAME = 'wall'
INPUT_TYPE = 'small'


def drange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step


class Attack(object):
    def __init__(self, day, strength, east, west):
        self.day = day
        self.strength = strength
        self.east = east
        self.west = west


def get_attacks(tribe):
    d, n, w, e, s, dd, dp, ds = tribe
    attacks = []
    for _ in range(n):
        attacks.append(Attack(d, s, e, w))
        d += dd
        s += ds
        e += dp
        w += dp
    return attacks


def solve(case):
    """break 'case', solve and return the solution"""
    wall = defaultdict(lambda: 0)
    attacks = defaultdict(list)
    successful_attacks = 0

    for tribe in case:
        tribe_attacks = get_attacks(tribe)
        for attack in tribe_attacks:
            attacks[attack.day].append(attack)

    for day in sorted(attacks.iterkeys()):
        for attack in attacks[day]:
            for point_on_wall in drange(attack.west, attack.east + 0.5, 0.5):
                if wall[point_on_wall] < attack.strength:
                    successful_attacks += 1
                    break

        for attack in attacks[day]:
            for point_on_wall in drange(attack.west, attack.east + 0.5, 0.5):
                if wall[point_on_wall] < attack.strength:
                    wall[point_on_wall] = attack.strength

    return successful_attacks


def read_case(lines):
    num_of_tribes = int(lines.pop(0))
    case = list()
    for _ in range(num_of_tribes):
        case.append(tuple([int(num) for num in lines.pop(0).split()]))
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
