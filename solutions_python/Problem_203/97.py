#!/usr/bin/python3

import sys

nRounds = int(sys.stdin.readline().strip())

for _ in range(0, nRounds):
    sys.stdout.write("Case #{}:".format(_+1))
    sys.stdout.write("\n")
    strInput = sys.stdin.readline().strip()
    iRow = int(strInput.split(' ')[0], 10)
    iCol = int(strInput.split(' ')[1], 10)
    cake = []
    for i in range(0, iRow):
        cake.append(list(sys.stdin.readline().strip()))
    cakeTable = []
    for i in range(0, iRow):
        cakeTable.append([])
        for j in range(0, iCol):
            if cake[i][j] != '?':
                cakeTable[i].append((j,cake[i][j]))
    curRow = []
    #find first row
    for i in range(0, iRow):
        if len(cakeTable[i]) != 0:
            curRow = cakeTable[i]
            break
    for i in range(0, iRow):
        if len(cakeTable[i]) != 0:
            # replace curRow
            curRow = cakeTable[i]
        idx = 0
        for j in range(0, iCol):
            if curRow[idx][0] >= j:
                sys.stdout.write(curRow[idx][1])
            elif idx == len(curRow) - 1:
                sys.stdout.write(curRow[idx][1])
            else:
                idx = idx + 1
                sys.stdout.write(curRow[idx][1])
        sys.stdout.write("\n")
    sys.stdout.flush()
