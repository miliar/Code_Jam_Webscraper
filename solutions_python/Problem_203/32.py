#!/usr/bin/python

def applyInitial(cake, from_row, to_row, from_col, to_col, initial):
    for r in range(from_row, to_row):
        for c in range(from_col, to_col):
            cake[r + 1][c + 1] = initial

def fillCake(cake):
    last_row_filled = -1
    for r, row in enumerate(cake):
        last_column_filled = -1
        last_initial = ''
        row_done = False
        for c, initial in enumerate(row):
            if initial != '?':
                applyInitial(cake, last_row_filled, r, last_column_filled, c, initial)
                last_column_filled = c
                last_initial = initial
                row_done = True
        if row_done:
            applyInitial(cake, last_row_filled, r, last_column_filled, len(row) - 1, last_initial)
            last_row_filled = r
    for r in range(last_row_filled + 1, len(cake)):
        cake[r] = cake[last_row_filled]
    return cake

def printCake(cake):
    for r in cake:
        print ''.join(r)

T = int(raw_input())
for t in range(T):
    R, C = map(int, raw_input().split())
    cake = []
    for r in range(R):
        cake.append(list(raw_input().strip()))

    fillCake(cake)
    print "Case #%d:" % (t + 1)
    printCake(cake)