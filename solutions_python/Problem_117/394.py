#! /opt/local/bin/python

import sys, itertools

def getline(file=sys.stdin):
    return file.readline().strip()

def getints():
    return [int(x) for x in getline().split()]

def out(s):
    if False:
        print s

def solve(casenum):
    rowCount, colCount = getints()
    rows = []
    rowMax = []
    colMax = []
    for r in range(rowCount):
        rows.append(getints())
        rowMax.append(max(rows[-1]))
    for c in range(colCount):
        colMax.append(max([row[c] for row in rows]))
    possible = True
    for r in range(rowCount):
        for c in range(colCount):
            if rows[r][c] != min(rowMax[r], colMax[c]):
                possible = False
                break
        if not possible:
            break
    if possible:
        answer = 'YES'
    else:
        answer = 'NO'
    print 'Case #%d: %s' % (casenum, answer)

cases = int(getline())
for case in xrange(cases):
    solve(case + 1)
