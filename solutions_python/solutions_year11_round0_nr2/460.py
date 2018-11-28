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
    lst = readstr().split()
    lst.reverse()
    combinations = {}
    oppositions = {}
    for _ in xrange(int(lst.pop())):
        a, b, c = lst.pop()
        combinations[a + b] = c
        combinations[b + a] = c
    for _ in xrange(int(lst.pop())):
        a, b = lst.pop()
        oppositions.setdefault(a, set()).add(b)
        oppositions.setdefault(b, set()).add(a)
    cnt, s = int(lst.pop()), lst.pop()
    assert cnt == len(s)
    assert not len(lst)
    stack = []
    for c in s:
        while len(stack):
            res = combinations.get(c + stack[-1], None)
            if res:
                c = res
                stack.pop()
            else:
                break
        op_set = oppositions.get(c, None)
        if op_set and any(x in op_set for x in stack):
            stack = []
        else:
            stack.append(c)
    return '[' + ', '.join(stack) + ']'

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
