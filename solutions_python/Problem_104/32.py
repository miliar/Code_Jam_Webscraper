import pdb
import sys
import re
import time
from collections import namedtuple
from itertools import *
from copy import copy, deepcopy

taskname = 'C'
input = None

def readstr():
    return next(input).strip()

def readintlist():
    lst = map(int, readstr().split())
    return lst

def readint():
    lst = readintlist()
    assert len(lst) == 1
    return lst[0]

def solvecase():
    numbers = readintlist()
    cnt = numbers.pop(0)
    assert cnt == len(numbers)
    d = {}
    for i in xrange(1, cnt):
        for subset in combinations(numbers, i):
            s = sum(subset)
            if s in d:
                return ' '.join(str(n) for n in d[s]) + '\n' + ' '.join(str(n) for n in subset)
            else:
                d[s] = subset
    return 'Impossible'

def solve(suffix):
    global input
    tstart = time.clock()
    input = open(taskname + '-' + suffix + '.in', 'r')
    output = open(taskname + '-' + suffix + '.out', 'w')
    casecount = readint()
    
    for case in range(1, casecount + 1):
        s = solvecase()
        s = "Case #%d:\n%s" % (case, str(s)) 
        print >>output, s
        print s
        
    input.close()
    output.close()
    print '%s solved in %.3f' % (suffix, time.clock() - tstart)
            
if __name__ == '__main__':
    solve('small')
    solve('large')
