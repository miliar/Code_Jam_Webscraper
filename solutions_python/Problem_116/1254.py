#!/usr/bin/python

import sys

def isWiningLine (line):
    if line.find('.') != -1:
        return None

    Xs = line.count('X')
    if Xs == 4:
        return 'X won'

    Os = line.count('O')
    if Os == 4:
        return 'O won'

    Ts = line.count('T')
    if Ts == 0:
        return None

    if Xs == 3:
        return 'X won'

    if Os == 3:
        return 'O won'

    return None


def solveCase (case):
    dots = 0 # Number of dots in the play
    for line in case:
        d = line.count('.')
        if d > 0:
            dots += d
            continue

        ret = isWiningLine(line)
        if ret != None:
            return ret

    i = 0
    while i < 4:
        line = case[0][i] + case[1][i] + case[2][i] + case[3][i]
        ret = isWiningLine(line)
        if ret != None:
            return ret
        i += 1

    diag1 = case[0][0] + case[1][1] + case[2][2] + case[3][3]
    ret = isWiningLine(diag1)
    if ret != None:
        return ret

    diag2 = case[0][3] + case[1][2] + case[2][1] + case[3][0]
    ret = isWiningLine(diag2)
    if ret != None:
        return ret

    if dots == 0:
        return "Draw"
    return "Game has not completed"


def solve_input (fname):
    f = open(fname, 'r')
    f.readline()
    i = 1
    caseNum = 1
    case = []
    for line in f:
        if line == "\n" and len(case) > 0:
            solution = solveCase(case)
            print "Case #" + str(caseNum) + ": " + solution
            caseNum += 1
            case = []
        else:
            case.append(line[:-1])
    f.close()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        fname = sys.argv[1]
    else:
        fname = 'Asample'

    solve_input(fname)
