import pdb
import sys
import re
import time
from collections import namedtuple
from itertools import *
from copy import copy, deepcopy

taskname = 'B'
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
    lst = readintlist()
    googlers, surprizes, target, scores = lst[0], lst[1], lst[2], lst[3:]
    assert googlers == len(scores)
    
    normal_min_sum_scores = target + 2 * max((target - 1), 0)
    surprizing_min_sum_scores = target + 2 * max((target - 2), 0)
    normal_ok = 0
    surprizing_ok = 0
    failures = 0 
    for sum_score in scores:
        if sum_score >= normal_min_sum_scores:
            normal_ok += 1
        elif sum_score >= surprizing_min_sum_scores:
            surprizing_ok += 1
        else:
            failures += 1
    assert normal_ok + surprizing_ok + failures == googlers
    normal_ok += min(surprizing_ok, surprizes)
    return normal_ok

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
