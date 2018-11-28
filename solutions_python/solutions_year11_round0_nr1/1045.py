#coding: 1251
#####################################################

from __future__ import division

import os
import sys
import operator
import string
import re
import time

from os.path import splitext
from copy import copy

from math import *
from collections import *
from itertools import *
from functools import *

#####################################################

alone = 1

try:
    from do import report_working_on, filein, fileout
except ImportError:
    alone = 1

if alone:
    report_working_on = lambda a,b: None
    filein = lambda: file('A-large.in')#sys.stdin
    fileout = lambda: sys.stdout

def dorun():
    fin, fout = filein(), fileout()
    cases = int(fin.next())
    for case in xrange(cases):
        report_working_on(case, cases)
        print>>fout, 'Case #%d: %s' % ( 1+case, solve(fin) )
    else:
        report_working_on(0,0)

#####################################################

def solve(fin):
    line = iter(fin.next().split())
    N = int(line.next())
    commands = [(i+1, line.next(), int(line.next())) for i in xrange(N)]

    turntime = [0]
    # турн и положение ботов
    botposition = {'B':(0,1), 'O':(0,1)}
    for turn, bot, point in commands:
        prevturn, prevpoint = botposition[bot]
        prevtime = turntime[prevturn]

        # фора, которую имеет робот
        delta = turntime[-1] - prevtime

        # время до достижения
        timeto = max(0, abs(point-prevpoint) - delta)

        # новое положение робота
        botposition[bot] = turn,point

        # время турна
        turntime.append( turntime[-1] + timeto + 1 )

    return turntime[-1]

#####################################################

if __name__=='__main__': dorun()
