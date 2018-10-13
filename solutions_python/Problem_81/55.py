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

def average(values):
    return sum(values, 0.0) / len(values)

def solvecase():
    n_teams = readint()
    data = [readstr() for _ in xrange(n_teams)]
    assert all(len(s) == n_teams for s in data)
    def calc_wp(s):
        cnt = sum(c != '.' for c in s)
        s = sum(int(c) for c in s if c != '.')
        return float(s) / cnt
    def calc_wp_except(s, me):
        return calc_wp(s[:me] + s[me + 1:])
    def calc_owp(s, me):
        return average([calc_wp_except(row, me) 
                        for c, row in zip(s, data) 
                        if c != '.'])
                
    wp = map(calc_wp, data)
    owp = [calc_owp(s, me) for me, s in enumerate(data)]
    oowp = [average([owp[i] for i, c in enumerate(s) if c != '.']) for s in data]
    rpi = [0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i] for i in xrange(n_teams)]
    result = ''.join('\n{}'.format(x) for x in rpi)
    return result

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
