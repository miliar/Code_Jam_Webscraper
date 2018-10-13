#!/usr/bin/env python

from __future__ import division

import collections
import itertools
import sys

class gcj:
    IN = sys.stdin
    number = 0

    @classmethod
    def case(cls):
        cls.number += 1
        return 'Case #%d:' % cls.number

    @classmethod
    def line(cls, type=str):
        line = cls.IN.readline()
        return type(line.strip('\n'))

    @classmethod
    def splitline(cls, type=str):
        line = cls.IN.readline()
        return [type(x) for x in line.split()]



def go():
    x = int(raw_input())
    fix = []
    need = []
    wp = [0] * x
    for i in xrange(x):
        c = str(raw_input())
        # print c
        fix.append(c)
        pos = 0
        tot = 0
        for t in c:
            if t != '.':
                tot+=1
                if t=='1':
                    pos += 1
        need.append((pos,tot))
        wp [i] = float(pos) /float (tot)
    # print wp
    owp = [0] * x
    oowp = [0] * x
    for i in xrange(x):
        for j in xrange (x):
            if fix[i][j]!='.':
                decider = 1 if fix[j][i]=='1' else 0 
                owp[i] += float( (need[j][0] - decider)) / float(need[j][1] - 1) 
        owp[i] = owp[i] / float(need[i][1]) 
    # print owp

    for i in xrange(x):
        for j in xrange (x):
            if fix[i][j]!='.':
                oowp[i] += owp[j] 
        oowp[i] = oowp[i] / float(need[i][1]) 
    # print oowp
    for it in xrange(x):
        print 0.25*wp[it] + 0.5*owp[it] + 0.25*oowp[it]
T = int(raw_input())
for t in xrange(T):
    print gcj.case()
    go()