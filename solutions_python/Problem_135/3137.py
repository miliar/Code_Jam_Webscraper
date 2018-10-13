import pdb
import sys
import re
import time
from collections import namedtuple
from itertools import *
from copy import copy, deepcopy
from pprint import pprint
from glob import glob

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

def solvecase():
    answer1 = readint()
    m1 = [readintlist() for _ in xrange(4)]
    assert all(len(row) == 4 for row in m1)
    answer2 = readint()
    m2 = [readintlist() for _ in xrange(4)]
    assert all(len(row) == 4 for row in m1)
    possibilities1 = set(m1[answer1 - 1])
    possibilities2 = set(m2[answer2 - 1])
#    print possibilities1, possibilities2
    answer = possibilities1.intersection(possibilities2)
#    print answer
    if len(answer) == 1:
        return answer.pop()
    if len(answer) == 0:
        return 'Volunteer cheated!'
    return 'Bad magician!'

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
