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

def solvecase():
    corridor_len, walk_speed, run_speed, run_time, n = readintlist()
    walkways = [tuple(readintlist()) for _ in range(n)]
    walkways.sort()
    prev_end = 0
    slow_walkways = []
    for start, end, _ in walkways:
        if start - prev_end > 0:
            slow_walkways.append((prev_end, start, 0.0))
        prev_end = end
    if corridor_len - prev_end > 0:
        slow_walkways.append((prev_end, corridor_len, 0.0))
    walkways.extend(slow_walkways)
    walkways = [(float(speed), float(end - start)) for start, end, speed in walkways]
    walkways.sort()
    # print walkways
    t = 0.0
    for speed, length in walkways:
        if run_time > 0:
            l = run_time * (speed + run_speed)
            if l <= length:
                t += run_time
                run_time = 0.0
                length -= l
                if length > 0:
                    t += length / (speed + walk_speed)
            else:
                tt = length / (speed + run_speed)
                t += tt
                run_time -= tt
        else:
            t += length / (speed + walk_speed)
    return t
                
                
            
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
