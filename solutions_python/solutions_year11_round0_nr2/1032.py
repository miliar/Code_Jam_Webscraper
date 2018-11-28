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

try:
    from do import report_working_on
except ImportError:
    report_working_on = lambda a,b: None

if sys.argv:
    fin = file(sys.argv[1], 'r')
    fout = file(splitext(sys.argv[1])[0]+'.out', 'w+')
else:
    fin = sys.stdin
    fout = sys.stdout

def dorun():
    cases = int(fin.next())
    for case in xrange(cases):
        report_working_on(case, cases)
        print>>fout, 'Case #%d: %s' % ( 1+case, solve(fin) )
    else:
        report_working_on(0,0)

#####################################################

def solve(fin):
    line = iter(fin.next().split())

    C = int(line.next())
    CS = islice(line, C)

    combine = {}
    for x,y,z in CS:
        combine[x+y]=z
        combine[y+x]=z

    D = int(line.next())
    DS = islice(line, D)

    delete = {}
    for x,y in DS:
        delete[x] = y
        delete[y] = x

    N = int(line.next())
    NS = line.next()

    elements = []
    for char in NS:
        p = elements[-1] if elements else ''
        if p+char in combine:
            del elements[-1]
            char = combine[p+char]

        opp = delete[char] if char in delete else '-'
        if opp in elements:
            elements = []
        else:
            elements.append( char )

    return '[' + ', '.join(elements) + ']'

#####################################################

if __name__=='__main__': dorun()
