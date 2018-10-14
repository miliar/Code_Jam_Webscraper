#!/usr/bin/env python

import sys


class Case:
    def __init__(self):
        self.gain = 2.0
        self.C = 0
        self.F = 0
        self.X = 0
        self.ans = 0

    def __repr__(self):
        return "Case{C: %f, F: %f, X: %f}" % (self.C, self.F, self.X)

    def solve(self):
        current = self.X / self.gain
        self.ans = sys.maxint

        n = 0
        while True:
            current = self.X / (n*self.F + self.gain)  #final cookies

            for m in range(n):  # farms cost
                current += (self.C / (m * self.F + self.gain))

            if current > self.ans:
                break
            else:
                n += 1
                self.ans = current


def main(filename):
    cases = readCases(filename)
    i = 1

    for c in cases:
        c.solve()
        print "Case #%d: %.7f" % (i, c.ans)
        i += 1


def readCases(filename):
    cases = []
    with open(filename) as f:
        nbCases = int(f.readline())
        for n in range(nbCases):
            c = Case()
            c.C, c.F, c.X =  [float(x) for x in f.readline().split()]
            cases.append(c)

    #print cases
    assert len(cases) == nbCases
    return cases



if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    main(sys.argv[1])