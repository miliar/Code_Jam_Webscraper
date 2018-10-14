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

#def solve_dyn(n):
#    arr = [None] * (n + 1)
#    arr[1] = (1, None)
#    def set(new_idx, new_cnt, old_idx):
#        if new_idx >= len(arr):
#            return
#        if arr[new_idx] is None or arr[new_idx][0] > new_cnt:
#            arr[new_idx] = (new_cnt, old_idx)
#    for idx in xrange(1, len(arr)):
#        steps = arr[idx][0]
#        set(idx + 1, steps + 1, idx)
#        set(int(str(idx)[::-1], 10), steps + 1, idx)
#    return arr
#
#def solve_greedy(n):
#    arr = [None] * (n + 1)
#    arr[1] = (1, None)
#    for idx in xrange(2, len(arr)):
#        steps1 = arr[idx - 1][0] + 1
#        steps2 = steps1 + 1
#        idx2 = str(idx)[::-1]
#        if idx2[0] != '0':
#            idx2 = int(idx2) 
#            if idx2 < idx:
#                steps2 = arr[idx2][0] + 1
#        if steps1 <= steps2:
#            arr[idx] = (steps1, idx - 1)
#        else:
#            arr[idx] = (steps2, idx2)
#    return arr
#
#def solve_greedy2(n):
#    cnt = 1
#    while n > 1:
#        cnt += 1
#        idx2 = str(n)[::-1]
#        if idx2[0] != '0':
#            idx2 = int(idx2) 
#            if idx2 < n:
#                n = idx2
#                continue
#        n -= 1
#    return cnt


def solve_rec(n):
    sn = str(n)
    if len(sn) < 2:
        return n
    half_len = len(sn) // 2 
    if half_len * 2 == len(sn):
        new_s = sn[0:half_len] + '0' * (half_len - 1) + '1'
    else:
        new_s = sn[0:half_len] + '0' * half_len + '1'
    new_n = int(new_s)
    if new_n > n:
        return 1 + solve_rec(n - 1)
    actual_new_n = int(new_s[::-1])
    if actual_new_n == new_n:
        return (n - new_n) + 1 + solve_rec(actual_new_n - 1)
    return (n - new_n) + 1 + solve_rec(actual_new_n)
 

#arr = solve_greedy(300)
#for idx in xrange(1, len(arr)):
#    steps, prev = arr[idx]
#    print '{:<3} {:<3} {} {}'.format(idx, steps, prev, 
#            '*' if prev is not None and prev + 1 != idx else '')
#
#sys.exit()

#arr = solve_greedy(200000)
#for idx in xrange(1, len(arr)):
#    steps, prev = arr[idx]
#    if prev is not None and prev + 1 != idx:
#        print '{:<3} {:<3} {}'.format(idx, steps, prev)
#
#sys.exit()

#arr1 = solve_dyn(200000)
#arr2 = solve_greedy(200000)
#
#for idx in xrange(1, len(arr1)):
#    (s1, prev1), (s2, prev2) = arr1[idx], arr2[idx]
#    if s1 != s2: #or prev1 != prev2:
#        print 'Greedy1 wrong', idx, s1, prev1, s2, prev2
#        break
#    print
#    s3 = solve_rec(idx)
#    if s1 != s3:
#        print 'Rec wrong', idx, s1, prev1, s3
#        break
#else:
#    print 'All is well'
#
#sys.exit()
    
        

def solvecase():
    n = readint()
    return solve_rec(n)

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
