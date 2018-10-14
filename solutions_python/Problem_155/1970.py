#! /usr/bin/python

import sys, itertools

def getline():
    return sys.stdin.readline().strip()

DEBUG = False
def out(s):
    if DEBUG:
        sys.stderr.write(str(s) + '\n')

class Case:
    def __init__(self, casenum):
        self.casenum = casenum

    def done(self, answer):
        print 'Case #%d: %s' % (self.casenum, answer)

    def solve(self):
        k, s = getline().split()
        s = [int(i) for i in s]
        y = o = 0
        for i in range(len(s)):
            if o < i:
                y += i - o
                o += i - o
            o += s[i]
        self.done(y)

cases = int(getline())
for case in xrange(cases):
    Case(case + 1).solve()
