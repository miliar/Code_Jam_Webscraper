#!/usr/bin/env python

import sys


class Case:
    def __init__(self):
        self.row1 = 0
        self.layout1 = []
        self.row2 = 0
        self.layout2 = []
        self.answer = None

    def __repr__(self):
        return "Case{row1: %d, row2: %d}" % (self.row1, self.row2)

    def solve(self):
        self.answer = [x for x in self.layout1[self.row1-1] if x in self.layout2[self.row2-1]]
        self.answerString = str(self.answer[0]) if len(self.answer) == 1 else "Bad magician!" if len(self.answer) > 1 else "Volunteer cheated!"

def main(filename):
    cases = readCases(filename)
    i = 1

    for c in cases:
        c.solve()
        print "Case #%d: %s" % (i, c.answerString)
        i += 1


def readCases(filename):
    cases = []
    with open(filename) as f:
        nbCases = int(f.readline())
        for n in range(nbCases):
            c = Case()

            c.row1 = int(f.readline())
            for r in range(4):
                row = f.readline()
                c.layout1.append( [int(x) for x in row.split()] )

            c.row2 = int(f.readline())
            for r in range(4):
                row = f.readline()
                c.layout2.append( [int(x) for x in row.split()] )

            cases.append(c)

    assert len(cases) == nbCases
    return cases



if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    main(sys.argv[1])