#!/usr/bin/python

TEMPLATE = "Case #%d: %s"
f = file("A-large.in")
T = int(f.readline())

case = 0
for i in range(T):
    (N, K) = map(int, f.readline().split())

    blue_flag = False
    red_flag = False

    rows = []
    blues = "B" * K
    reds = "R" * K

    case = case + 1
    for i in range(N):

        row = f.readline()
        row = row[:len(row)-1].replace(".", "")
        row = "." * (N - len(row)) + row
        rows.append(row)

    for row in rows:
        if blues in row:
            blue_flag = True
            break

    for row in rows:
        if reds in row:
            red_flag = True
            break

    if blue_flag and red_flag:
        print TEMPLATE % (case, "Both")
        continue

    cols = [""] * N
    for row in rows:
        for j, char in enumerate(row):
            cols[j] = cols[j] + char

    if not blue_flag:
        for col in cols:
            if blues in col:
                blue_flag = True
                break

    if not red_flag:
        for col in cols:
            if reds in col:
                red_flag = True
                break

    if blue_flag and red_flag:
        print TEMPLATE % (case, "Both")
        continue

    diagonals = []
    for j in range(len(rows) - K + 1):
        diagonal_1 = ""
        diagonal_2 = ""
        diagonal_3 = ""
        diagonal_4 = ""
        for k in range(len(rows) - j):
            diagonal_1 = diagonal_1 + rows[k][j + k]
            diagonal_2 = diagonal_2 + rows[j + k][k]
            diagonal_3 = diagonal_3 + rows[k][len(rows) - j - k - 1]
            diagonal_4 = diagonal_4 + rows[j + k][len(rows) - 1 - k]

        diagonals.append(diagonal_1)
        diagonals.append(diagonal_2)
        diagonals.append(diagonal_3)
        diagonals.append(diagonal_4)

    if not blue_flag:
        for diagonal in diagonals:
            if blues in diagonal:
                blue_flag = True
                break

    if not red_flag:
        for diagonal in diagonals:
            if reds in diagonal:
                red_flag = True
                break

    if blue_flag and red_flag:
        print TEMPLATE % (case, "Both")
    elif blue_flag and not red_flag:
        print TEMPLATE % (case, "Blue")
    elif not blue_flag and red_flag:
        print TEMPLATE % (case, "Red")
    else:
        print TEMPLATE % (case, "Neither")



