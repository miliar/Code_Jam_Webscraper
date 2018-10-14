#!/usr/bin/env python
def process_file(file):
    fsock = open(file)
    text = fsock.read()
    fsock.close()
    lines = text.split('\n')
    return lines

def process_lines(lines):
    ans = []
    first = True
    numCases = int(lines[0])
    lineIndex = 1
    for caseIndex in range(numCases):
        case = []
        xySplit = lines[lineIndex].split(' ')
        x = int(xySplit[0])
        y = int(xySplit[1])
        lineIndex += 1
        for row in range(x):
            case.append([int(x) for x in lines[lineIndex].split(' ')])
            lineIndex += 1
        ans.append(case)
    return ans

def process_case(case):
    maxHeight = getMaxHeight(case)
    attempt = getAttempt(case, maxHeight)
    curHeight = nextMaxHeight(case, maxHeight)
    if curHeight == 0:
        return 'YES'
    while curHeight > 0 and flatten(case, attempt, curHeight):
        if case == attempt:
            return 'YES'
        else:
            curHeight = nextMaxHeight(case, curHeight)
    return 'NO'

def getMaxHeight(case):
    maxHeight = case[0][0]
    for i in range(len(case)):
        for j in range(len(case[0])):
            if case[i][j] > maxHeight:
                maxHeight = case[i][j]
    return maxHeight

def getAttempt(case, maxHeight):
    attempt = []
    for i in case:
        attempt.append([maxHeight for x in case[0]])
    return attempt

def nextMaxHeight(case, maxHeight):
    next = 0
    for i in range(len(case)):
        for j in range(len(case[0])):
            if case[i][j] > next and case[i][j] < maxHeight:
                next = case[i][j]
    return next

def flatten(case, attempt, curHeight):
    for i in range(len(case)):
        for j in range(len(case[0])):
            if case[i][j] == curHeight:
                if shouldFlattenRow(case, i, curHeight):
                    flattenRow(attempt, i, curHeight)
                elif shouldFlattenColumn(case, j, curHeight):
                    flattenColumn(attempt, j, curHeight)
                else:
                    return False
    return True


def shouldFlattenRow(case, i, curHeight):
    caseRow = case[i]
    for k in caseRow:
        if k > curHeight:
            return False
    return True

def shouldFlattenColumn(case, j, curHeight):
    for caseRow in case:
        if caseRow[j] > curHeight:
            return False
    return True

def flattenRow(attempt, i, curHeight):
    for k in range(len(attempt[0])):
        attempt[i][k] = curHeight

def flattenColumn(attempt, j, curHeight):
    for k in range(len(attempt)):
        attempt[k][j] = curHeight

if __name__ == "__main__":
    import sys
    filename = sys.argv[1]
    lines = process_file(filename)
    cases = process_lines(lines)
    c = 0
    for case in cases:
        c += 1
        print "Case #%d: %s" % (c, process_case(case))