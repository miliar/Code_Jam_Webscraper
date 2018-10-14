#!/usr/bin/env python3
"""
Mushroom Monster problem
for Google Code Jam 2015
Round 1A

Link to problem description:
https://code.google.com/codejam/contest/4224486/dashboard#s=p0

Author: 
  Chris Nitsas
  (nitsas)

Language:
  Python 3(.4)

Date:
  April, 2015

Usage:
  python3 runme.py input_file
"""


import sys
import argparse
# modules I've written:
from helpful import *


_program_description = \
'''TEMPLATE PROGRAM DESCRIPTION'''


_input_file_description = \
'''TEMPLATE INPUT FILE DESCRIPTION'''


def parse_args():
    """
    Parse the command line arguments and return them in a namespace.
    """
    parser = argparse.ArgumentParser(description=_program_description)
    parser.add_argument('input_file', help=_input_file_description)
    #parser.add_argument('-v', '--verbose', action='store_true', 
    #                    default=False, help='show progress')
    args = parser.parse_args()
    return args


def compute_using_first_method(num_mushrooms_at_intervals):
    min_num_cookies_eaten = 0
    for i in range(1, len(num_mushrooms_at_intervals)):
        diff = num_mushrooms_at_intervals[i-1] - num_mushrooms_at_intervals[i]
        if diff > 0:
            min_num_cookies_eaten += diff
    return min_num_cookies_eaten


def compute_using_second_method(num_mushrooms_at_intervals):
    max_diff = 0
    for i in range(1, len(num_mushrooms_at_intervals)):
        diff = num_mushrooms_at_intervals[i-1] - num_mushrooms_at_intervals[i]
        if diff > max_diff:
            max_diff = diff
    min_num_cookies_eaten = 0
    for i in range(1, len(num_mushrooms_at_intervals)):
        min_num_cookies_eaten += min(num_mushrooms_at_intervals[i-1], 
                                     max_diff)
    return min_num_cookies_eaten


def main(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        T = read_int(f)
        test_cases = list()
        for i in range(T):
            N = read_int(f)
            test_cases.append(read_list_of_int(f))
            assert(N == len(test_cases[-1]))
    for i, tc in enumerate(test_cases, start=1):
        print("Case #{}: {} {}".format(i, compute_using_first_method(tc),
                                          compute_using_second_method(tc)))
    return 0


if __name__ == "__main__":
    status = main(parse_args().input_file)
    sys.exit(status)
