#!/usr/bin/env python2
# -*- coding: utf-8 -*-


def solve(R, C, cake):
    blank_rows = []
    filled_rows = []
    for i in range(R):
        start = 0
        for j in range(C):
            if cake[i][j] == '?':
                continue
            for k in range(start, j):
                cake[i][k] = cake[i][j]
            start = j+1
        if start == 0:
            blank_rows.append(i)
        else:
            # fill the rest of the row
            for k in range(start,C):
                cake[i][k] = cake[i][start-1]
            filled_rows.append(i)
    
    bri = 0
    fri = 0
#    print filled_rows, blank_rows
    for i in range(R):
        if bri < len(blank_rows) and blank_rows[bri] == i:
            for j in range(C):
                cake[i][j] = cake[filled_rows[fri]][j]
            bri += 1
        elif fri < len(filled_rows) and filled_rows[fri] == i:
            fri += 1
            if fri == len(filled_rows):
                fri -= 1
        else:
            print "Error: row {} is neither filled not blank. Filled: {}. Blank {}.".format(i, filled_rows, blank_rows)
        
    return cake

T = int(raw_input())

for test_case in range(1, T+1):
    R,C = [int(s) for s in raw_input().split(" ")]
    cake = []
    for i in range(R):
        cake.append(list(raw_input()))
#    print R, C, cake

    solution = solve(R, C, cake)
    print "Case #{}:".format(test_case)
    for i in range(R):
        print ''.join(solution[i])
