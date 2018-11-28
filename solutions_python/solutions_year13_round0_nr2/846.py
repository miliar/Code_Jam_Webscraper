# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 21:58:25 2013

@author: malaa
"""
import numpy as np

d = {'X': 1, 'O': -1, '.': np.Infinity, 'T': 0}

def read_input(file_name):
    input = open(file_name).readlines()
    input = [i.replace("\n", "") for i in input]
    print input

    T = int(input[0])
    index = 1
    cases = list()
    for t in xrange(T):
        sizes = np.array(np.mat(input[index]))[0]
        case = np.zeros(sizes)
        index += 1
        for n in xrange(sizes[0]):
            line = input[index].split(' ')
            index += 1
            for m in xrange(sizes[1]):
                case[n, m] = int(line[m])
        cases.append(case)
    return (T, cases)

def check_case(case):
    unique = np.unique(case)

    for u in unique:
        (rows, cols) = np.nonzero(case == u)
        for i in xrange(len(rows)):
            row = rows[i]
            col = cols[i]
            if np.any(case[:,col] > u) and np.any(case[row,:] > u):
                return False

    return True

def check_cases(cases):
    out = list()
    for t in xrange(len(cases)):
        case = cases[t]
        if check_case(case):
            out.append("Case #%d: YES" % (t+1))
        else:
            out.append("Case #%d: NO" % (t+1))
    return out

#(T, cases) = read_input('B-example.txt')
(T, cases) = read_input('B-large.in')
out = check_cases(cases)
print out
#
open('B-large.out', 'w').write("\n".join(out))
