#!/usr/bin/env python

import sys

import time

input = sys.argv[1]

num_cases = 0
cases = []

print 'input filename ', input

with open(input) as f:
    num_cases = int(f.readline())
    #print 'cases: ', cases 
    for ii in range(0, num_cases):
        cases.append(f.readline())

def baseconvert(n, base):
    """convert positive decimal integer n to equivalent in another base (2-36)"""

    digits = "0123456789abcdefghijklmnopqrstuvwxyz"

    try:
        n = int(n)
        base = int(base)
    except:
        return ""

    if n < 0 or base < 2 or base > 36:
        return ""

    s = ""
    while 1:
        r = n % base
        s = digits[r] + s
        n = n / base
        if n == 0:
            break

    return s

def find_happy(case): 
    bases = case.split() 
    test_int = 2 
    while True: 
        #print 'testing ', test_int
        if is_num_happy(test_int, bases[0]):
            others_happy = True 
            #print 'other bases ', bases[1:]
            for other_base in bases[1:]:
                if not is_num_happy(test_int, other_base): 
                    others_happy = False
                    break
            if others_happy:
                return test_int
        test_int += 1

def _is_num_happy(num, base, prev_sols=[]):
    total = 0
    num = baseconvert(num, base)
    for char in str(num):
        total += int(char) * int(char)
    #print total
    if total == 1:
        return True 
    elif total in prev_sols:
        return False
    else:
        prev_sols.append(total)
        return _is_num_happy(total, base, prev_sols) 

def is_num_happy(num, base):
    return _is_num_happy(num, base, [])

if __name__ == '__main__':
    #print find_happy('2 3')
    case_num = 1
    for case in cases:
        #print 'case: ', case
        print 'Case #%d: %d' % (case_num,find_happy(case))
        case_num += 1
