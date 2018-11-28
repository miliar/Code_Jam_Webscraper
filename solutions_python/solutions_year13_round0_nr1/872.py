# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 21:58:25 2013

@author: malaa
"""
import numpy as np

d = {'X': 1, 'O': -1, '.': np.Infinity, 'T': 0}

def read_input(file_name):
    input = open(file_name).readlines()
    input = [i[:-1] for i in input]

    T = int(input[0])
    index = 1
    cases = list()
    for t in xrange(T):
        case = list()
        for r in xrange(index, index + 4):
            case.append(input[r])
        index += 5
        cases.append(case)
    return (T, cases)

def convert_input(cases):
    mat_cases = list()
    for case in cases:
        mat = np.zeros((4,4))
        for r in xrange(4):
            for c in xrange(4):
                mat[r, c] = d[case[r][c]]
        mat_cases.append(mat)
    return mat_cases

def compute_sums(case):
    # compute sums
    sums = np.sum(case, axis=0)
    sums = np.append(sums, np.sum(case, axis=1))
    sums = np.append(sums, np.trace(case))
    sums = np.append(sums, np.trace(np.fliplr(case)))
    return sums

def check_symbol_won(symbol, in_case):
    # convert any T to that symbol
    case = in_case.copy()
    case[case == d['T']] = d[symbol]
    sums = compute_sums(case)

    # check for 4 * d[symbol]
#    print sums
#    print 4. * d[symbol]
#    print sums == 4. * d[symbol]
    if np.any(sums == 4. * d[symbol]):
        return True
    else:
        return False

def check_full(case):
    sums = compute_sums(case)
    if np.all(np.isfinite(sums)):
        return True
    else:
        return False

def check_cases(cases):
    out = list()

    for t in xrange(len(cases)):
        case = cases[t]
        if check_symbol_won('X', case):
            out.append('Case #%d: X won' % (t+1))
        elif check_symbol_won('O', case):
            out.append('Case #%d: O won' % (t+1))
        elif check_full(case):
            out.append('Case #%d: Draw' % (t+1))
        else:
            out.append('Case #%d: Game has not completed' % (t+1))

    return out

#(T, cases) = read_input('tictactoe-example.txt')

(T, cases) = read_input('A-large.in')
cases = convert_input(cases)
out = check_cases(cases)
print out

open('tictactoe-out-large.txt', 'w').write("\n".join(out))
