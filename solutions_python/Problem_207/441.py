#!/usr/bin/env python3

"""
Google Code Jam
Round 1A 2017
Problem B.
"""

import argparse

class TestCase:
    def __init__(self, N, R, O, Y, G, B, V):
        self.N = N
        self.R = R
        self.O = O
        self.Y = Y
        self.G = G
        self.B = B
        self.V = V
    def solve(self):
        if self.R + self.B + self.V < self.Y:
            return "IMPOSSIBLE"
        if self.R + self.Y + self.O < self.B:
            return "IMPOSSIBLE"
        if self.B + self.Y + self.G < self.R:
            return "IMPOSSIBLE"
        if self.G > self.R or self.O > self.B or self.V > self.Y:
            return "IMPOSSIBLE"
        gs = []
        os = []
        vs = []
        for _ in range(self.G):
            gs.append("R")
            gs.append("G")
        for _ in range(self.O):
            os.append("B")
            os.append("O")
        for _ in range(self.V):
            vs.append("Y")
            vs.append("V")
        self.R -= self.G
        self.B -= self.O
        self.Y -= self.V
        if self.R > 0:
            if len(gs) > 0:
                gs.append("R")
                self.R -= 1
        if self.B > 0:
            if len(os) > 0:
                os.append("B")
                self.B -= 1
        if self.Y > 0:
            if len(vs) > 0:
                vs.append("Y")
                self.Y -= 1
        ls = gs + os + vs
        rgb = []
        while max(self.R, self.B, self.Y) > 0:
            if self.R >= max(self.B, self.Y) and self.R > 0:
                rgb.append("R")
                self.R -= 1
                if self.B >= self.Y and self.B > 0:
                    rgb.append("B")
                    self.B -= 1
                elif self.Y > 0:
                    rgb.append("Y")
                    self.Y -= 1
            elif self.B >= max(self.R, self.Y) and self.B > 0:
                rgb.append("B")
                self.B -= 1
                if self.R >= self.Y and self.R > 0:
                    rgb.append("R")
                    self.R -= 1
                elif self.Y > 0:
                    rgb.append("Y")
                    self.Y -= 1
            elif self.Y >= max(self.R, self.B) and self.Y > 0:
                rgb.append("Y")
                self.Y -= 1
                if self.R >= self.B and self.R > 0:
                    rgb.append("R")
                    self.R -= 1
                elif self.B > 0:
                    rgb.append("B")
                    self.B -= 1
        ss = ls + rgb
        if ss[0] == ss[-1]:
            temp = ss[-2]
            ss[-2] = ss[-1]
            ss[-1] = temp
        return "".join(ss)


def read_data(filename):
    """Read and parse the input data"""
    with open(filename) as _file:
        test_cases = []
        num_test_cases = int(_file.readline())
        for _ in range(num_test_cases):
            N, R, O, Y, G, B, V = [int(x) for x in _file.readline().split()]
            test_cases.append(TestCase(N, R, O, Y, G, B, V))
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
