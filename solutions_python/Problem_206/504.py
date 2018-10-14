#!/usr/bin/env python3

"""
Google Code Jam
Round 1A 2017
Problem A.
"""

import argparse

class TestCase:
    def __init__(self, D, N, horses):
        self.D = D
        self.N = N
        self.horses = horses
    def remaining_time(self, horse):
        remaining_distance = self.D - horse['K']
        remaining_time = remaining_distance/horse['S']
        return remaining_time
    def solve(self):
        longest_time = 0
        for horse in self.horses:
            if self.remaining_time(horse) > longest_time:
                longest_time = self.remaining_time(horse)
        return self.D/longest_time

def read_data(filename):
    """Read and parse the input data"""
    with open(filename) as _file:
        test_cases = []
        num_test_cases = int(_file.readline())
        for _ in range(num_test_cases):
            D, N = [int(x) for x in _file.readline().split()]
            horses = []
            for _ in range(N):
                K, S = [int(x) for x in _file.readline().split()]
                horse = {'K': K, 'S': S}
                horses.append(horse)
            test_cases.append(TestCase(D, N, horses))
    return num_test_cases, test_cases

if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("problem", help="problem to solve")
    PARSER.add_argument("--check", help="check if computed output is equal to expected output", action="store_true")
    PARSER.add_argument("--out", help="output result to file", action="store_true")
    ARGS = PARSER.parse_args()
    NUM_TEST_CASES, TEST_CASES = read_data(ARGS.problem + ".in")
    if ARGS.check:
        OUTPUT_FILE = open(ARGS.problem + ".out", "r")
    if ARGS.out:
        OUTPUT_FILE = open(ARGS.problem + ".out", "w")
    for it in range(NUM_TEST_CASES):
        test_case = TEST_CASES[it]
        result = "Case #{}: {}".format(it + 1, test_case.solve())
        if ARGS.check:
            assert(OUTPUT_FILE.readline().strip() == result)
        elif ARGS.out:
            print(result, file=OUTPUT_FILE)
        else:
            print(result)
    if ARGS.check or ARGS.out:
        OUTPUT_FILE.close()
