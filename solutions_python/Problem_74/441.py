import pdb
import sys
import re
import time
from collections import namedtuple
from itertools import *
from copy import copy, deepcopy

taskname = 'A'
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

def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

def solvecase():
    lst = readstr().split()
    cnt = int(lst[0])
    del lst[0]
    assert len(lst) == cnt * 2
    p1, t1 = 1, 0
    p2, t2 = 1, 0
    t = 0
    def step(current_t, oldpos, oldt, newpos):
        steps = abs(newpos - oldpos)
        return max(current_t, oldt + steps) + 1
    for robot, pos in grouper(2, lst):
        pos = int(pos)
        if robot == 'O':
            t = step(t, p1, t1, pos)
            t1, p1 = t, pos
        elif robot == 'B':
            t = step(t, p2, t2, int(pos))
            t2, p2 = t, pos
        else: 
            assert False, str((robot, pos)) 
    return t 

def solve(suffix):
    global input
    tstart = time.clock()
    input = open(taskname + '-' + suffix + '.in', 'r')
    output = open(taskname + '-' + suffix + '.out', 'w')
    casecount = readint()
    
    for case in range(1, casecount + 1):
        s = solvecase()
        s = "Case #%d: %s" % (case, str(s)) 
        print >>output, s
        print s 
        
    input.close()
    output.close()
    print '%s solved in %.3f' % (suffix, time.clock() - tstart)
            
if __name__ == '__main__':
    solve('small')
    solve('large')
