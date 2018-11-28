#!/usr/bin/python
# -*- coding: utf-8 -*-
class Team:
        
    def wp(self, j=-1):
        if j in self.won:
            return 1.0 * (len(self.won)-1) / (len(self.opponents)-1)
        elif j == -1:
            return 1.0 * (len(self.won)) / (len(self.opponents))
        else:
            return 1.0 * (len(self.won)) / (len(self.opponents)-1)
    
    def score(self):
        return 0.25 * self.wp() + 0.50 * self.owp + 0.25 * self.oowp
        
    def __str__(self):
        return "%s: %.2f %.2f %.2f %.6f" % (self.n, self.wp(), self.owp, self.oowp, self.score())

import sys
fin = sys.stdin
T = int(fin.readline())
for case in range(1,T+1):
    N = int(fin.readline())
    played = []
    teams = []
    for i in range(N):
        row = fin.readline().strip()
        t = Team()
        t.n = i
        t.won = set()
        t.opponents = []
        for j, c in enumerate(row):
            if c == '1':
                t.won.add(j)
            if c != '.':
                t.opponents.append(j)
        teams.append(t)
    
    for t in teams:
        total = 0.0
        for i in t.opponents:
            o = teams[i]
            total += o.wp(t.n)
        t.owp = total / len(t.opponents)
    for t in teams:
        total = 0.0
        for i in t.opponents:
            o = teams[i]
            total += o.owp
        t.oowp = total / len(t.opponents)
    
    print "Case #%d:" % (case)
    
    for t in teams:
        print "%.8f" % t.score()
    
