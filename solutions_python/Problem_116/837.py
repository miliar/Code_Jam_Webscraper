#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

SIZE = 4

def solve(case):
    hasBlank = False
    c1 = { "O":[0, 0], "X":[0, 0] }
    for row in range(SIZE):
        c = { "O":[0, 0], "X":[0, 0] }
        for col in range(SIZE):
            for turn in "XO":
                if case[col][row] == turn or case[col][row] == "T":
                    c[turn][0] += 1
                if case[row][col] == turn or case[row][col] == "T":
                    c[turn][1] += 1
                if case[row][col] == ".":
                    hasBlank = True
        for turn in "XO":
            if c[turn].count(SIZE) > 0:
                return "%s won" % turn
        
        for turn in "XO":
            if case[row][row] == turn or case[row][row] == "T":
                c1[turn][0] += 1
            if case[row][SIZE - row - 1] == turn \
                or case[row][SIZE - row - 1] == "T":
                c1[turn][1] += 1  

    for turn in "XO":
        if c1[turn].count(SIZE) > 0:
            return "%s won" % turn

    if hasBlank:
        return "Game has not completed"
    else:
        return "Draw"

# main
#
me = sys.argv[0].split("/")[-1].replace(".py", "")
#file = me + "-sample"
#file = me + "-small-attempt0"
file = me + "-large"
#file = me + "-large-practice"

with open(file + ".in", "r") as fdin:
    with open(file + ".out", "w") as fdout:

        T = int(fdin.readline())
        for ncase in range(T):
            case = []
            for i in range(SIZE):
                case.append(fdin.readline().rstrip())
            if fdin.readline().rstrip() != "":
                print("Fatal error: data format is invalid")
                sys.exit()

            result = solve(case)
    
            line = "Case #%d: %s" % (ncase + 1, result)
            print(line) 
            fdout.write("%s\n" % line)