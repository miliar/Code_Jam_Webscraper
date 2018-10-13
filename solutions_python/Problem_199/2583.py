#!/usr/bin/env python3
"""
Oversized Pancake Flipper problem
for Google Code Jam 2017
Qualification Round

Link to problem description:
https://code.google.com/codejam/contest/3264486/dashboard#s=p0

Author:
  Chris Nitsas
  (nitsas)

Language:
  Python 3(.5)

Date:
  April, 2017

Usage:
  python3 runme.py input_file
"""


import sys, argparse, collections


TestCase = collections.namedtuple('TestCase', ['pancakes', 'flipper_width'])


def parse_args():
    """
    Parse the command line arguments and return them in a namespace.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()
    return args


def read_testcase(file_):
    pancakes_str, flipper_width_str = file_.readline().split()
    return TestCase([p == '+' for p in pancakes_str], int(flipper_width_str))


def solve_testcase(tc):
    num_flips = 0
    for i in range(len(tc.pancakes) - tc.flipper_width + 1):
        if not tc.pancakes[i]:
            # flip
            for j in range(tc.flipper_width):
                tc.pancakes[i + j] = not tc.pancakes[i + j]
            num_flips += 1
    if False in tc.pancakes[::-1][:tc.flipper_width]:
        return 'IMPOSSIBLE'
    else:
        return num_flips


def main(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        num_testcases = int(f.readline())
        testcases = [read_testcase(f) for i in range(num_testcases)]
    for i, tc in enumerate(testcases, start=1):
        print('Case #{}: {}'.format(i, solve_testcase(tc)))
    return 0


if __name__ == "__main__":
    status = main(parse_args().input_file)
    sys.exit(status)
