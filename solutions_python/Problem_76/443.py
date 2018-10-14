import pdb
import sys
import re
import time
from collections import namedtuple
from itertools import *
from copy import copy, deepcopy
import operator

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
    cnt = readint()
    numbers = readintlist()
    assert cnt == len(numbers)
#    bags = {}
#    def add(bags, xor_sum, true_sum):
#        s = bags.get(xor_sum, -1)
#        if s < true_sum:
#            bags[xor_sum] = true_sum
#    for n in numbers:
#        items = list(bags.iteritems())
#        add(bags, n, n)
#        for xor_sum, true_sum in items:
#            add(bags, xor_sum ^ n, true_sum + n)
    xor_sum = reduce(operator.xor, numbers, 0)
    if xor_sum != 0: return 'NO'
    return sum(numbers) - min(numbers) 

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
