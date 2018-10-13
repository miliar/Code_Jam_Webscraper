#! /usr/bin/python

import sys, itertools

def getline():
    return sys.stdin.readline().strip()

DEBUG = False
def out(s):
    if DEBUG:
        sys.stderr.write(str(s))

def avg(s):
    return float(sum(s)) / float(len(s))

class Case:
    def __init__(self, casenum):
        self.casenum = casenum
        self.teamCount = int(getline())
        self.records = []
        self.wp = []
        self.owp = []
        self.oowp = []
        for i in range(self.teamCount):
            self.records.append(getline())

    def done(self):
        print 'Case #%d:' % self.casenum
        for i in range(self.teamCount):
            print self.calcRpi(i)

    def calcRpi(self, team):
        return 0.25 * self.wp[team] + 0.50 * self.owp[team] + 0.25 * self.oowp[team]

    def calcWp(self, record):
        wins = 0.0
        total = 0.0
        for r in record:
            if r == '1':
                wins += 1
            if r != '.':
                total += 1
        return wins / total

    def calcOwp(self, record, team):
        wps = []
        for i in range(self.teamCount):
            if record[i] != '.':
                r = self.records[i]
                r = list(r)
                r[team] = '.'
                r = ''.join(r)
                wps.append(self.calcWp(r))
        return avg(wps)

    def calcOowp(self, record):
        owps = []
        for i in range(self.teamCount):
            if record[i] != '.':
                owps.append(self.owp[i])
        return avg(owps)

    def solve(self):
        for i in range(self.teamCount):
            self.wp.append(self.calcWp(self.records[i]))
        for i in range(self.teamCount):
            self.owp.append(self.calcOwp(self.records[i], i))
        for i in range(self.teamCount):
            self.oowp.append(self.calcOowp(self.records[i]))

        self.done()

cases = int(getline())
for case in xrange(cases):
    Case(case + 1).solve()
