#!/usr/bin/env python3
"""
Magic Trick problem
for Google Code Jam 2014
Qualification Round

Link to problem description:
https://code.google.com/codejam/contest/2974486/dashboard

author: 
Christos Nitsas
(chrisn654 or nitsas)

language:
Python 3(.3)

date:
May, 2012

usage:
$ python3 runme.py sample.in
or
$ runme.py sample.in
(where sample.in is the input file and $ the prompt)
"""


import sys
import collections
# non-standard modules:
from helpful import read_int, read_list_of_int


TestCase = collections.namedtuple("TestCase", ("answerA", "gridA", "answerB", "gridB"))


def solve_test_case(tc):
    rowA = tc.gridA[tc.answerA-1]
    rowB = tc.gridB[tc.answerB-1]
    possible_cards = set(rowA).intersection(set(rowB))
    if len(possible_cards) > 1:
        return "Bad magician!"
    elif len(possible_cards) == 1:
        return possible_cards.pop()
    else:
        return "Volunteer cheated!"


def main(filename=None):
    if filename is None:
        if len(sys.argv) == 2:
            filename = sys.argv[1]
        else:
            print("Usage: runme.py input_file")
            return 1
    with open(filename, "r") as f:
        T = read_int(f)
#        test_cases = list(TestCase(read_list_of_int(f), list(read_list_of_int(f) for i in range(4)), read_list_of_int(f), list(read_list_of_int(f) for i in range(4))) for i in range(T))
        test_cases = []
        for i in range(T):
            answerA = read_int(f)
            gridA = list(read_list_of_int(f) for i in range(4))
            answerB = read_int(f)
            gridB = list(read_list_of_int(f) for i in range(4))
            tc = TestCase(answerA, gridA, answerB, gridB)
            test_cases.append(tc)
    for i, tc in enumerate(test_cases, start=1):
        print("Case #{}: {}".format(i, solve_test_case(tc)))
    return 0


if __name__ == "__main__":
    status = main()
    sys.exit(status)

