# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 21:58:25 2013

@author: malaa
"""

import numpy as np
import re

d = {'X': 1, 'O': -1, '.': np.Infinity, 'T': 0}

def read_input(file_name):
    input = open(file_name).readlines()
    input = [i.replace("\n", "") for i in input]
    print input

    T = int(input[0])
    index = 1
    cases = list()
    for t in xrange(T):
        case = np.array(np.mat(input[index]))[0]
        index += 1
        cases.append(case)
    return (T, cases)

def check_fair(num):
    num_str = str(num)
    num_str = re.sub('\.0*', '', num_str)
    l = len(num_str)
    if l == 1:
        return True
    if l % 2 == 0 and num_str[:l/2] == num_str[-1:l/2-1:-1]:
        return True
    if l % 2 == 1 and num_str[:l//2] == num_str[-1:l//2:-1]:
        return True
    return False

def check_fair_square(num):
    sqrt = np.sqrt(num)
    if np.floor(sqrt) == sqrt and check_fair(sqrt):
        return True
    return False

def get_fair(low, high):
    fair = list()
    for i in xrange(max(low,0), min(10,high+1)):
        fair.append(i)

    i = 1
    cont = True
    while cont:
        rev = str(i)[::-1]
        cont = False
        for d in ['', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            n = int(str(i) + d + rev)
            if n <= high and n >= low:
                cont = True
                fair.append(n)
        if not cont and n < low:
            cont = True
        i += 1

    fair.sort()
    return fair

def check_case(case):
    low = case[0]
    high = case[1]

    fair = get_fair(low, high)

    num = 0
    for i in xrange(len(fair)):
        if check_fair_square(fair[i]):
            num += 1

    return num


def check_cases(cases):
    out = list()
    for t in xrange(len(cases)):
        case = cases[t]
        s = check_case(case)
        out.append("Case #%d: %d" % (t+1, s))

    return out

infile = 'C-small-attempt3.in' #'C-example.txt' # 'C-small-attempt1.in'

(T, cases) = read_input(infile)
out = check_cases(cases)
print out
#
open(infile + ".out", 'w').write("\n".join(out))
