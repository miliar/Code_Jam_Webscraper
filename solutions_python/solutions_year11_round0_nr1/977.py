#!/usr/bin/python

import sys

def opp(x):
    if x == 'B':
        return 'O'
    else:
        return 'B'

def howmanymoves(p1, p2):
    return abs(p2 - p1) + 1

def process(line):
    content = line.split(" ")
    cnt = int(content[0])
    sequence = []
    for i in xrange(cnt):
        sequence.append([content[2*i+1], int(content[2*i+2])])

    currentPositions = {'B': 1, 'O': 1}
    necessaryMoves = 0
    movesTheOtherIsAhead = {'B': 0, 'O': 0}
    for s in sequence:
        mvs = howmanymoves(currentPositions[s[0]], s[1])
        currentPositions[s[0]] = s[1]
        if movesTheOtherIsAhead[opp(s[0])] > 0: #same robot 2nd move in a row
            necessaryMoves += mvs
            movesTheOtherIsAhead = {s[0]: 0, opp(s[0]): movesTheOtherIsAhead[opp(s[0])] + mvs}
        elif movesTheOtherIsAhead[s[0]] + 1 >= mvs:
            necessaryMoves += 1
            movesTheOtherIsAhead = {s[0]: 0, opp(s[0]): 1}
        else:
            diff = mvs - movesTheOtherIsAhead[s[0]]
            necessaryMoves += diff
            movesTheOtherIsAhead = {s[0]: 0, opp(s[0]): diff}
    return necessaryMoves


if __name__ == '__main__':
    i = 0
    for line in sys.stdin.readlines():
        if i == 0:
            nrOfTestCases = int(line)
        else:
            res = process(line)
            print "Case #%d: %d" % (i, res)
        i += 1
