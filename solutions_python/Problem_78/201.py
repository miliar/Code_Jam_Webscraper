#! /usr/bin/python

import sys
from fractions import Fraction

def getline():
    return sys.stdin.readline().strip()


def out(s):
    if True:
        print s

class Case:
    def __init__(self, casenum):
        self.casenum = casenum
        self.N, self.Pd, self.Pg = [ int(x) for x in getline().split() ]

    def done(self, answer):
        answer = answer and 'Possible' or 'Broken'
        print 'Case #%d: %s' % (self.casenum, answer)

    def solve(self):
        n = self.N
        pd = self.Pd
        pg = self.Pg

        if pd == 0 and pg < 100:
            return self.done(True)

        if pd == 100 and pg > 0:
            return self.done(True)

        if pg == 100 and pd < 100:
            return self.done(False)

        if pg == 0 and pd > 0:
            return self.done(False)

        if n * pd % 100 == 0:
            return self.done(True)
        else:
            d = Fraction(pd, 100).denominator
            return self.done(d <= n)

cases = int(getline())
for case in xrange(cases):
    Case(case + 1).solve()
