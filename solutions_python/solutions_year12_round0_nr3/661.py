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
    min_n, max_n = readintlist()
    cnt = 0
    min_n_s = str(min_n)
    shift_bound = len(min_n_s)
    for i in xrange(min_n, max_n + 1):
        s_i = str(i)
        r_pairs = set()
        for shift in xrange(1, shift_bound):
            shifted = s_i[shift:] + s_i[:shift]
            if shifted[0] == '0': continue
            if shifted < s_i and shifted >= min_n_s:
                r_pairs.add(shifted)
        cnt += len(r_pairs)
    return cnt  

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
