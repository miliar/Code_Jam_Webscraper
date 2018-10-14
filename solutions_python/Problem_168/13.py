# Python 3.2

from common import *

def main(casenum):
    r, c = readints()
    x = [None] * r
    for i in range(r):
        x[i] = readline()

    numcol = [0] * c
    numrow = [0] * r
    for i in range(r):
        for j in range(c):
            if x[i][j] != '.':
                numcol[j] += 1
                numrow[i] += 1
    for i in range(r):
        for j in range(c):
            if numrow[i] == 1 and numcol[j] == 1 and x[i][j] != '.':
                writecase(casenum, "IMPOSSIBLE")
                return

    count = 0
    for i in range(r):
        for j in range(c):
            if x[i][j] == '.':
                continue
            if x[i][j] == '^':
                for i2 in range(i):
                    if x[i2][j] != '.':
                        break
                else:
                    count += 1
            if x[i][j] == 'v':
                for i2 in range(i + 1, r):
                    if x[i2][j] != '.':
                        break
                else:
                    count += 1
            if x[i][j] == '<':
                for j2 in range(j):
                    if x[i][j2] != '.':
                        break
                else:
                    count += 1
            if x[i][j] == '>':
                for j2 in range(j + 1, c):
                    if x[i][j2] != '.':
                        break
                else:
                    count += 1

    writecase(casenum, count)

run(main)
