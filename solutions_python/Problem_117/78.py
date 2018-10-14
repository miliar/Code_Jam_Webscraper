import pdb
import sys
import re
import time
from collections import namedtuple
from itertools import *
from copy import copy, deepcopy
from pprint import pprint

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
    n, m = readintlist()
    map = [readintlist() for _ in xrange(n)]
    assert all(len(l) == m for l in map)
    result = [[100 for _ in xrange(m)] for _ in xrange(n)]
    for row in xrange(n):
        maxheight = max(map[row][col] for col in xrange(m))
        for col in xrange(m):
            result[row][col] = min(result[row][col], maxheight)
    for col in xrange(m):
        maxheight = max(map[row][col] for row in xrange(n))
        for row in xrange(n):
            result[row][col] = min(result[row][col], maxheight)
    if all(c1 == c2 for r1, r2 in izip(map, result) for c1, c2 in izip(r1, r2)):
        return 'YES' 
    return 'NO'
    
    return 0

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
