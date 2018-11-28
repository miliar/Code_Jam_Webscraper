#!/usr/bin/python

import sys

# Initialize columns
cols = []
for i in range(4):
    col = []
    for j in range(4):
       col += ['']
    cols += [col]

# Check if a sequence of chars results in a win
def check_sequence(chars):
    global x_wins, o_wins, incomplete

    x = 0
    o = 0

    for c in chars:
        if c == 'X':
            x += 1
        elif c == 'O':
            o += 1
        elif c == 'T':
            x += 1 
            o += 1
        elif c == '.':
            incomplete = True

    if x == 4:
        x_wins = True
    elif o == 4:
        o_wins = True

# Read one case from the file and determine its result
def handle_case(infile):
    global x_wins, o_wins, incomplete

    x_wins = False
    o_wins = False
    incomplete = False

    # Check rows as they are read, then store for column checks
    for i in range(4):
        line = infile.readline().strip()
        check_sequence(line)
        for j in range(4):
            cols[j][i] = line[j]

    # Check columns
    for i in range(4):
        check_sequence(''.join(cols[i]))

    # Check diagonals
    check_sequence(''.join([cols[x][x] for x in range(4)]))
    check_sequence(''.join([cols[3-x][x] for x in range(4)]))

    if x_wins:
        print 'X won'
    elif o_wins:
        print 'O won'
    elif incomplete:
        print 'Game has not completed'
    else:
        print 'Draw'

    infile.readline()   # throw away empty space

with open(sys.argv[1], 'r') as infile:
    cases = int(infile.readline().strip())
    for n in range(cases):
        print 'Case #' + str(n+1) + ': ',
        handle_case(infile)
