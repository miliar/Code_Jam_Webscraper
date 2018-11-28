#! /usr/local/bin/python2.7
import sys
import os


if len(sys.argv) < 2: sys.exit(-1)
if not os.path.isfile(sys.argv[1]): sys.exit(-2)

f = open(sys.argv[1])

num_inputs = int(f.readline())

for case in range(num_inputs):
    rows = []
    for i in range(4):
        line = f.readline()
        row = []
        for j in range(4):
            row.append(line[j])
        rows.append(row)
    f.readline()

    winner = None
    
    # Check diags
    if rows[0][0] in ['X', 'T'] and rows[1][1] in ['X', 'T'] and rows[2][2] in ['X', 'T'] and rows[3][3] in ['X', 'T']:
        winner = 'X won'
    if rows[0][0] in ['O', 'T'] and rows[1][1] in ['O', 'T'] and rows[2][2] in ['O', 'T'] and rows[3][3] in ['O', 'T']:   
        winner = 'O won'
    if rows[3][0] in ['X', 'T'] and rows[2][1] in ['X', 'T'] and rows[1][2] in ['X', 'T'] and rows[0][3] in ['X', 'T']:
        winner = 'X won'
    if rows[3][0] in ['O', 'T'] and rows[2][1] in ['O', 'T'] and rows[1][2] in ['O', 'T'] and rows[0][3] in ['O', 'T']:   
        winner = 'O won'
    
    # Check rows
    for x in range(4):
        if winner is not None: break
        if rows[0][x] in ['X', 'T'] and rows[1][x] in ['X', 'T'] and rows[2][x] in ['X', 'T'] and rows[3][x] in ['X', 'T']:
            winner = 'X won'
        if rows[0][x] in ['O', 'T'] and rows[1][x] in ['O', 'T'] and rows[2][x] in ['O', 'T'] and rows[3][x] in ['O', 'T']:
            winner = 'O won'

    # Check columns
    for y in range(4):
        if winner is not None: break
        if rows[y][0] in ['X', 'T'] and rows[y][1] in ['X', 'T'] and rows[y][2] in ['X', 'T'] and rows[y][3] in ['X', 'T']:
            winner = 'X won'
        if rows[y][0] in ['O', 'T'] and rows[y][1] in ['O', 'T'] and rows[y][2] in ['O', 'T'] and rows[y][3] in ['O', 'T']:
            winner = 'O won'
    
    # Check for not completed
    if winner is None:
        for y in range(4):
            if winner is not None: break
            for x in range(4):
                if rows[y][x] == '.':
                    winner = 'Game has not completed'

    # Set to draw otherwise
    if winner is None:
        winner = 'Draw'

    print "Case #%i: %s" % (case + 1, winner)

