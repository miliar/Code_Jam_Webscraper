#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys

debug = False

def print_debug(line):
    if debug:
        print line
        
def test_solution(solution, N, R, O, Y, G, B, V):
    pass
    

def solve_small(N, R, O, Y, G, B, V):
    colors = 'RYB'
    counts = sorted([[R,0], [Y,1], [B,2]])

    c1, c2, c3 = [c for c,i in counts]
    n_triple = c1+c2-c3
#    print counts, n_triple
    cols = [colors[i] for c,i in counts]
    if n_triple < 0:
        return ["IMPOSSIBLE"]

    solution = [' ' for i in xrange(N)]
    n = 0
    for i in xrange(n_triple):
        solution[n] = cols[2]
        solution[n+1] = cols[1]
        solution[n+2] = cols[0]
        n += 3
    for i in xrange(c2 - n_triple):
        solution[n] = cols[2]
        solution[n+1] = cols[1]
        n += 2
    for i in xrange(c1 - n_triple):
        solution[n] = cols[2]
        solution[n+1] = cols[0]
        n += 2
#    print solution
    
    return solution

def check(N, C, antiC, col1, col2):
    if antiC > C or (C>0 and C == antiC and N > 2*C):
        print_debug('IMPOSSIBLE {}{}'.format(col1, col2))
        return "IMPOSSIBLE"
    if C == antiC and N == 2*C:
        solution = [col1+col2 for i in xrange(C)]
        return ''.join(solution)
    return ''

def replace_color(antiC, col1, col2):
    new_col = []
    for i in range(antiC):
        new_col.append(col1+col2)
    new_col.append(col1)
    return ''.join(new_col)

def solve(N, R, O, Y, G, B, V):
#    if B < 2*O-1 or R < 2*G-1 or Y < 2*V-1:
#        print_debug("IMPOSSIBLE_single")
#        return "IMPOSSIBLE"
#    if B + R + Y < 2*(O + G + V) - 1:
#        print_debug("IMPOSSIBLE_total")
#        return "IMPOSSIBLE"

    if O + G + V == 0:
        return solve_small(N, R, O, Y, G, B, V)

    sol_test = check(N, B, O, 'B', 'O')
    if sol_test <> '':
        return sol_test
    sol_test = check(N, R, G, 'R', 'G')
    if sol_test <> '':
        return sol_test
    sol_test = check(N, Y, V, 'Y', 'V')
    if sol_test <> '':
        return sol_test
    
    B1 = B-O
    R1 = R-G
    Y1 = Y-V
    
    solution = solve_small(N, R1, 0, Y1, 0, B1, 0)
    b_change = False
    r_change = False
    y_change = False
    for i in range(len(solution)):
        if solution[i] == 'B' and not b_change:
            new_letter = replace_color(O, 'B','O')
            solution[i] = new_letter
            b_change = True
            continue
        if solution[i] == 'R' and not r_change:
            new_letter = replace_color(G, 'R','G')
            solution[i] = new_letter
            r_change = True
            continue
        if solution[i] == 'Y' and not y_change:
            new_letter = replace_color(V, 'Y','V')
            solution[i] = new_letter
            y_change = True
            continue
    
    return solution

if '-D' in sys.argv:
    debug = True

T = int(raw_input())

for test_case in range(1, T+1):
    N, R, O, Y, G, B, V = [int(s) for s in raw_input().split(" ")]
#    print N, R, O, Y, G, B, V 
    solution = solve(N, R, O, Y, G, B, V)
    print "Case #{}: {}".format(test_case, ''.join(solution))

