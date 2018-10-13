import pdb
import sys
import re
import time
from collections import namedtuple
from itertools import *
from copy import copy, deepcopy
from pprint import pprint
from bisect import bisect_left, bisect_right

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

def append_fair_squares(n, acc):
    if n == 1:
        acc.extend([1, 4, 9])
        return
    half = (n + 1) // 2
    rev_idx = -1 if 2 * half == n else -2
    for s in product(*(['12'] + ['012'] * (half - 1))):
        s = ''.join(s + s[rev_idx::-1])
        root = int(s)
        square = root ** 2
        s = str(square)
        if s == s[::-1]:
            acc.append(square)        

#fair_squares = [] 
#for n in xrange(1, 23):
#    append_fair_squares(n, fair_squares)
#
#print len(fair_squares)
#pprint(fair_squares)
#sys.exit()


def square_without_overflow(digits):
    result = []
    for i in xrange(1, len(digits)):
        s = sum(d1 * d2 for d1, d2 in izip(digits[:i], reversed(digits[:i])))
        if s > 9: return
        result.append(s)
    
    for i in xrange(len(digits)):
        s = sum(d1 * d2 for d1, d2 in izip(digits[i:], reversed(digits[i:])))
        if s > 9: return
        result.append(s)
    return result

def is_palindrome(lst):
    for i in xrange(len(lst) // 2):
        if lst[i] != lst[~i]:
            return False
    return True

def calculate_fair_squares(n):
    result = [1, 4, 9, 121, 484]
    prefixes = set(map(tuple, [[1], [2], [3]]))
    for i in xrange(n):
        newprefixes = set()
        for x in ((0,), (1,), (2,)):
            for prefix in prefixes:
                interesting = False
                np = prefix + x
                
                square = square_without_overflow(np + np[-2::-1])
                if square: 
                    interesting = True
                    if is_palindrome(square):
                        result.append(int(''.join(map(str, square))))
                        
                square = square_without_overflow(np + np[::-1])
                if square: 
                    interesting = True
                    if is_palindrome(square):
                        result.append(int(''.join(map(str, square))))
                        
                if interesting:
                    newprefixes.add(np)
        prefixes = newprefixes
        print i, len(result), len(prefixes) 
    result.sort()
    return result
#    pprint(result)
#        pprint(prefixes)

#fair_squares = calculate_fair_squares(5)
fair_squares = calculate_fair_squares(24)
print len(str(fair_squares[-1]))

def solvecase():
    a, b = readintlist()
    low = bisect_left(fair_squares, a)
    high = bisect_right(fair_squares, b)
    return high - low

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
    solve('large-2')
