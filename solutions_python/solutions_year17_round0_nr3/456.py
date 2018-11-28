#!/usr/bin/env python3

"""
Google Code Jam
Qualification Round 2017
Problem C.
"""

import argparse

class TestCase:
    def __init__(self, N, K):
        self.N = N
        self.K = K
    def rs(self, r, stall):
        return r - stall - 1
    def solve(self):
        segment = (self.N, 1)
        bits = str(bin(self.K))[3:][::-1]
        for bit in bits:
            chosen = (segment[0] - 1) // 2 + segment[1]
            if bit == "0":
                segment = (segment[0] // 2, chosen + 1)
            else:
                segment = ((segment[0] - 1) // 2, chosen - (segment[0] - 1) // 2)
        chosen = (segment[0] - 1) // 2 + segment[1]
        ls = chosen - segment[1]
        rs = segment[1] + segment[0] - chosen - 1
        return "{} {}".format(max(ls, rs), min(ls, rs))

def read_data(filename):
    """Read and parse the input data"""
    with open(filename) as _file:
        test_cases = []
        num_test_cases = int(_file.readline())
        for _ in range(num_test_cases):
            N, K = [int(x) for x in _file.readline().split()]
            test_cases.append(TestCase(N, K))
    return num_test_cases, test_cases

if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("problem", help="problem to solve")
    PARSER.add_argument("--out", help="output result to file", action="store_true")
    ARGS = PARSER.parse_args()
    NUM_TEST_CASES, TEST_CASES = read_data(ARGS.problem + ".in")
    if ARGS.out:
        OUTPUT_FILE = open(ARGS.problem + ".out", 'w')
    for it in range(NUM_TEST_CASES):
        test_case = TEST_CASES[it]
        result = "Case #{}: {}".format(it + 1, test_case.solve())
        if ARGS.out:
            print(result, file=OUTPUT_FILE)
        else:
            print(result)
    if ARGS.out:
        OUTPUT_FILE.close()
