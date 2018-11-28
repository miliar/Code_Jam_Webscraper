#!/usr/bin/env python3
from itertools import chain
import sys

PROBLEM_LETTER = 'B'
DIFFICULTY = sys.argv[1]
INPUT_FILE = '{0}-{1}.in'.format(PROBLEM_LETTER, DIFFICULTY)
OUTPUT_FILE = '{0}-{1}.out'.format(PROBLEM_LETTER, DIFFICULTY)


def equalSet(l):
    return len(set(l)) == 1

def allEqual(field):
    return len(set(chain(*field))) == 1

def solve(fin):
    rows, cols = tuple(int(s) for s in fin.readline().split())
    field = list(range(rows))
    for r in range(rows): field[r] = list(int(s) for s in fin.readline().split())

    wasRow, wasCol = [False] * rows, [False] * cols
    while True:
        if allEqual(field):
            return 'YES'
        foundEqual, rowNumber, colNumber = False, None, None
        for r in range(rows):
            if wasRow[r]: continue
            if equalSet(field[r]):
                foundEqual, rowNumber = True, r
                break
        if not foundEqual:
            for c in range(cols):
                if wasCol[c]: continue
                if equalSet([field[j][c] for j in range(rows)]):
                    foundEqual, colNumber = True, c
                    break
        if not foundEqual: break
        if rowNumber is not None:
            wasRow[rowNumber] = True
            for c in range(cols):
                maxElem = max(field[j][c] for j in range(rows))
                field[rowNumber][c] = maxElem
        else:
            wasCol[colNumber] = True
            for r in range(rows):
                maxElem = max(field[r])
                field[r][colNumber] = maxElem
    return 'NO'

if __name__ == "__main__":
    fin = open(INPUT_FILE, 'r')
    fout = open(OUTPUT_FILE, 'w')

    testCount = int(fin.readline())
    for i in range(testCount):
        answer = solve(fin)
        fout.write('Case #{0}: {1}\n'.format(i + 1, answer))

    fin.close()
    fout.close()