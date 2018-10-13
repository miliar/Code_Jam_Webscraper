#!/usr/bin/python

def eq(a, b):
    return abs(a - b) < 1e-6

def is_balance(sheet, D, sx, sy, k):
    sum_x = 0
    sum_y = 0
    cx = sx + float(k) / 2
    cy = sy + float(k) / 2
    for i in range(k):
        for j in range(k):
            if (i, j) not in ((0, 0), (0, k - 1), (k - 1, 0), (k - 1, k - 1)):
                x = sx + i
                y = sy + j
                sum_x += (D + sheet[x][y]) * (x + 0.5 - cx)
                sum_y += (D + sheet[x][y]) * (y + 0.5 - cy)
    return eq(sum_x, 0) and eq(sum_y, 0)

def solve():
    R, C, D = [int(s) for s in raw_input().split()]
    sheet = []
    for i in range(R):
        sheet.append([int(s) for s in raw_input()])
    max_k = 0
    for i in range(R):
        for j in range(C):
            for k in range(3, min(R - i, C - j) + 1):
                if is_balance(sheet, D, i, j, k):
                    max_k = max(max_k, k)
    if max_k:
        return max_k
    else:
        return 'IMPOSSIBLE'

T = int(raw_input())
for i in range(T):
    print 'Case #%d: %s' % (i + 1, solve())
