#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys

def solve(case, row_nb_1, grid1, row_nb_2, grid2):
    
    row1 = grid1[row_nb_1-1]
    row2 = grid2[row_nb_2-1]
 
    match = []
    for card in row1:
        if card in row2:
            match.append(card)

    if len(match) == 0:
        output = "Volunteer cheated!"
    elif len(match) == 1:
        output = match[0]
    else:
        output = "Bad magician!"

    print "Case #" + str(case+1) + ": " + output

f = open(sys.argv[1], "r")
try:
    cases_nb = int(f.readline())

    for case in range(cases_nb):

        row1 = int(f.readline())
        grid1 = [f.readline().split() for i in range(4)]

        row2 = int(f.readline())
        grid2 = [f.readline().split() for i in range(4)]

        solve(case, row1, grid1, row2, grid2)

finally:
    f.close()
