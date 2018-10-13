# GCJ - EX01 #
# by meist3r-ed #
import numpy as py

# DEFINES #
# ---------------------------------------------------------------------------- #
DEBUG = 0
HAPPY_SIDE = '+'
BLANK_SIDE = '-'
# ---------------------------------------------------------------------------- #

# OPERATIONS #
# ---------------------------------------------------------------------------- #
# Check if the problem could be solved ( case is only :) )
def checkSolution(case):
    size = len(case)
    for i in range(0, size):
        if(case[i] == BLANK_SIDE):
            return 0
    return 1

# Flips pancakes ( YAY :3 )
def flipPancakes(case, k, pos):
    size = len(case)
    if(pos + k > size):
        return
    else:
        for i in range(pos, pos + k):
            if(case[i] == HAPPY_SIDE):
                case[i] = BLANK_SIDE
            else:
                case[i] = HAPPY_SIDE

# Algorithm to find solution ( or not )
def solveCase(case, k):
    cnt = 0
    size = len(case)

    if(k > size):
        return -1

    # Runs through the case
    for i in range(0, size):
        # Finds next blank-side pancake
        if(case[i] != HAPPY_SIDE):
            flipPancakes(case, k, i)
            cnt = cnt + 1
            i = i + k

    if(checkSolution(case) == 0):
        return -1
    else:
        return cnt
# ---------------------------------------------------------------------------- #

# MAIN #
# ---------------------------------------------------------------------------- #
cases = input()
cases = int(cases)
if(DEBUG): print(cases)

if(cases >= 1 and cases <= 100):
    for i in range(0, cases):
        buffer = input()
        curCase, curK = buffer.split(" ")

        curCase = list(curCase)
        curK = int(curK)

        if(DEBUG):
            print("Case #" + str(i + 1) + ": " + curCase + ", " + str(curK))
        # Solves current case
        caseRes = solveCase(curCase, curK)
        # If problem is impossible, print impossible
        if(caseRes == -1):
            print("Case #" + str(i + 1) + ": IMPOSSIBLE")
        # Else, print solution
        else:
            print("Case #" + str(i + 1) + ": " + str(caseRes))
# ---------------------------------------------------------------------------- #
