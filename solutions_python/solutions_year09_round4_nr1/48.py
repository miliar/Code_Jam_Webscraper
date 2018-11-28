import pdb
import sys
import re
import time
import operator
from collections import namedtuple
from itertools import *



taskname = 'A'
input = None
output = None

def readstr():
    return next(input).strip()

def readintlist():
    lst = map(int, readstr().split())
    return lst

def readints():
    lst = readintlist()
    return lst[0] if len(lst) == 1 else lst



def solvecase(case):
    print "Case #%d" % case
    rcnt = readints()
    rows = [reversed(readstr()) for i in range(rcnt)]
    nums = [rcnt - 1 - len(list(takewhile(lambda x: x == '0', row))) for row in rows]
    swaps = 0
    for i in range(rcnt):
        #print nums
        if nums[i] > i:
            for j in range(i + 1, rcnt):
                if nums[j] <= i:
                    r = nums[j]
                    swaps += j - i
                    nums[i + 1:j + 1] = nums[i:j]
                    nums[i] = r
                    break
            else:
                raise "Wtf"
    
    print >>output, "Case #%d: %d" % (case, swaps)

    
    

def solve(suffix):
    global input, output, taskname
    tstart = time.clock()
    input = open(taskname + '-' + suffix + '.in', 'r')
    output = open(taskname + '-' + suffix + '.out', 'w')
    casecount = readints()
    for case in range(1, casecount + 1):
        solvecase(case)
    input.close()
    output.close()
    print '%s solved in %.3f' % (suffix, time.clock() - tstart)
            
if __name__ == '__main__':
    solve('small')
    solve('large')
