#!/usr/bin/env python3

def maxCol(j, lawn):
    maximum = 0
    for row in lawn:
        if row[j] > maximum:
            maximum = row[j]
    return maximum

def checkRow(i, rows, cols, lawn):
    if rows[i]:
        return False
    else:
        maximum = max(lawn[i])
        for j in range(M):
            if lawn[i][j] < maximum:
                if not cols[j]:
                    return False
    rows[i] = True
    return True

def checkCol(j, rows, cols, lawn):
    if cols[j]:
        return False
    else:
        maximum = maxCol(j, lawn)
        for i in range(N):
            if lawn[i][j] < maximum:
                if not rows[i]:
                    return False
    cols[j] = True
    return True

def checkLawn(lawn):
    rows = [False] * N
    cols = [False] * M
    changed = True

    while changed:
        changed = False

        for i in range(N):
            if checkRow(i, rows, cols, lawn):
                changed = True

        for j in range(M):
            if checkCol(j, rows, cols, lawn):
                changed = True

    for i in range(N):
        if not rows[i]:
            return False

    for j in range(M):
        if not cols[j]:
            return False

    return True

fin  = open("B-large.in",  "r")
fout = open("B-large.out", "w")

T = int(fin.readline())

for t in range(1, T + 1):
    N, M = [int(i) for i in fin.readline().split(" ")]
    lawn = []

    for _ in range(N):
        lawn.append([int(i) for i in fin.readline().split(" ")])

    result = "YES" if checkLawn(lawn) else "NO"
    fout.write("Case #{0}: {1}\n".format(t, result))

fin.close()
fout.close()
