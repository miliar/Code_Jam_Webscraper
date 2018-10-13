import pdb
import sys
import re
import time
from collections import namedtuple
from itertools import *
from copy import copy, deepcopy
from pprint import pprint
from glob import glob

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
    farm_cost, farm_production, target_amount = map(float, readstr().split())
    cache = [] # [(farms, time)]
    
    cps = 2.0
    time = 0.0
    best_time = time + target_amount / cps
    saw_best = False
    for farms in xrange(0, 1000000):
        cps = 2.0 + farms * farm_production
        time_to_target = time + target_amount / cps
#        print best_time, time_to_target
        if best_time <= time_to_target and saw_best:
            break
        else:
            best_time = time_to_target
            saw_best = True
        time += farm_cost / cps
    return '{:0.7f}'.format(best_time)

def solve(input_name, output_name):
    global input
    tstart = time.clock()
    input = open(input_name, 'r')
    output = open(output_name, 'w')
    casecount = readint()
    
    for case in range(1, casecount + 1):
        s = solvecase()
        s = "Case #%d: %s" % (case, str(s)) 
        print >>output, s
        print s 
        
    input.close()
    output.close()
    print '%s solved in %.3f' % (input_name, time.clock() - tstart)

def main():
    input_names = glob(taskname + '-*.in')
    assert len(input_names)
    input_names.sort(reverse = True)
    for input_name in input_names:
        solve(input_name, input_name.replace('.in', '.out')) 
                
if __name__ == '__main__':
    main()
