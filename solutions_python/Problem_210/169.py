#!/usr/bin/env python2
# -*- coding: utf-8 -*-

total_minutes = 24*60
half_minutes = 12*60

def solve(Ac, Aj, Cs, Js):
    pass


def solve_single(num, apts):
    frees = [apts[0][0] + total_minutes - apts[-1][1]]
    for i in range(num-1):
        frees.append(apts[i+1][0] - apts[i][1])
    frees = sorted(frees, reverse = True)
    if frees[0] >= half_minutes:
        return 2
    else:
        return 4
    
    
    
def solve_small(Ac, Aj, Cs, Js):
    if Ac == 0:
        return solve_single(Aj, Js)
    elif Aj == 0:
        return solve_single(Ac, Cs)
    #Ac = Aj = 1
    return 2
    
    

T = int(raw_input())

for test_case in range(1, T+1):
    Ac, Aj = [int(s) for s in raw_input().split(" ")]
    Cs = sorted([[int(s) for s in raw_input().split(" ")] for i in range(Ac)], key = lambda cs: cs[0])
    Js = sorted([[int(s) for s in raw_input().split(" ")] for i in range(Aj)], key = lambda cj: cj[0])

#    print Ac, Aj, Cs, Js
    solution = solve_small(Ac, Aj, Cs, Js)
    print "Case #{}: {}".format(test_case, solution)
