#!/usr/bin/env python3
"""
Tidy Numbers problem
for Google Code Jam 2017
Qualification Round

Link to problem description:
https://code.google.com/codejam/contest/3264486/dashboard#s=p1

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


import sys, argparse


def parse_args():
    """
    Parse the command line arguments and return them in a namespace.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()
    return args


def index_of_first_digit_that_is_larger_than_its_right_neighbor(numstring):
    for i in range(len(numstring) - 1):
        if numstring[i] > numstring[i + 1]:
            return i
    return None


def last_tidy_number_before(numstring):
    r = index_of_first_digit_that_is_larger_than_its_right_neighbor(numstring)
    if r is None:
        return numstring
    l = numstring.index(numstring[r])
    assert(l <= r)
    last_tidy_numstring = numstring[:l]
    last_tidy_numstring += str(int(numstring[l]) - 1)
    last_tidy_numstring += '9' * (len(numstring) - l - 1)
    assert(len(last_tidy_numstring) == len(numstring))
    return int(last_tidy_numstring)


def main(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        num_testcases = int(f.readline())
        numstrings = [f.readline().strip() for i in range(num_testcases)]
    for i, numstring in enumerate(numstrings, start=1):
        print('Case #{}: {}'.format(i, last_tidy_number_before(numstring)))
    return 0


if __name__ == "__main__":
    status = main(parse_args().input_file)
    sys.exit(status)
