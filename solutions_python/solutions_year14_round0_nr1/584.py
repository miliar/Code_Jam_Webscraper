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
        answer1 = int(getline())
        rows1 = [{int(x) for x in getline().split()} for y in range(4)]
        answer2 = int(getline())
        rows2 = [{int(x) for x in getline().split()} for y in range(4)]
        i = rows1[answer1 - 1].intersection(rows2[answer2 - 1])
        if len(i) == 1:
            answer = list(i)[0]
        elif len(i) < 1:
            answer = 'Volunteer cheated!'
        else:
            answer = 'Bad magician!'
        self.done(answer)

cases = int(getline())
for case in xrange(cases):
    Case(case + 1).solve()
