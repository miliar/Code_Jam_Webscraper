#!/usr/bin/env python

import sys


class Case:
    def __init__(self):
        self.Smax = 0
        self.S = []

        self.ans = 0

    def __repr__(self):
        return "Case-> Max: {0}, S: {1}".format(self.Smax, self.S)

    def solve(self):
        total = 0
        moar = 0
        for i, n in enumerate(self.S):
            # assert(i <= self.Smax)
            # print "Rank {0}: {1} person need {2} before'em, {3} so far, {4} more needed".format(
            #     i, n, i, total, i-total
            # )

            if i-total > 0:
                moar += i-total
                total += i-total
            total += n
        self.ans = moar




def main(filename):
    cases = readCases(filename)
    i = 1

    for c in cases:
        c.solve()
        print "Case #%d: %d" % (i, c.ans)
        i += 1


def readCases(filename):
    cases = []
    with open(filename) as f:
        nbCases = int(f.readline())
        for n in range(nbCases):
            c = Case()
            max, S = f.readline().split()
            c.Smax = int(max)
            for l in S:
                c.S.append(int(l))
            cases.append(c)

    # print cases
    assert len(cases) == nbCases
    return cases



if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    main(sys.argv[1])