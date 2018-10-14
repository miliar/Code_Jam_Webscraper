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

def can_lose(my_score, other_scores, bonus):
    for score in other_scores:
        if score > my_score: continue
        bonus -= my_score - score
        if bonus <= 0: return False
    return True

def min_boost(my_score, other_scores):
    total_bonus = my_score + sum(other_scores)
    l, r = 0.0, 1.0
    while r - l > 1e-10:
        m = (l + r) / 2
        if can_lose(my_score + total_bonus * m, other_scores, total_bonus * (1 - m)):
            l = m
        else:
            r = m
    return m   

def min_boost2(my_score, other_scores):
    total_bonus = my_score + sum(other_scores)
    l, r = 0.0, 1.0
    while r - l > 1e-10:
        m = (l + r) / 2
        if can_lose(my_score + total_bonus * m, other_scores, total_bonus * (1 - m)):
            l = m
        else:
            r = m
    return m   

def solvecase():
    numbers = readintlist()
    cnt = numbers.pop(0)
    assert cnt == len(numbers)
    numbers = map(float, numbers)
    boosts = []
    for i in xrange(len(numbers)):
        other_scores = list(numbers)
        my_score = other_scores.pop(i)
        boosts.append(min_boost(my_score, other_scores) * 100)
    return ' '.join(map('{:.6f}'.format, boosts))

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
