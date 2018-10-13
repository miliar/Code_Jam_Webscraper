#!/usr/bin/python

import sys

# argument check
if(len(sys.argv) < 2):
    print("No input file provided!")
    sys.exit()

# open input
try:
    f = open(sys.argv[1], "r")
except:
    print( "Cannot open {0}".format(sys.argv[1]))
    sys.exit()

# open output
try:
    fo = open("out.txt", "w")
except:
    print( "Cannot open out.txt")
    sys.exit()

# get testcase count
count = int(f.readline())

# for each testcase
for i in range(count):
    # read table
    table = []
    for ln in range(4):
        table.append(f.readline());
    f.readline()

    # dot (unused space) counter
    ds = 0
    # solution found
    found = False

    # check diagonal \
    os = 0
    xs = 0
    for p in range(4):
        if(table[p][p] == 'X' or table[p][p] == 'T'):
            xs = xs + 1
        if(table[p][p] == 'O' or table[p][p] == 'T'):
            os = os + 1
        if(table[p][p] == '.'):
            ds = ds + 1
    if(xs == 4):
        fo.write("Case #{0}: X won\n".format(i+1))
        continue
    elif (os == 4):
        fo.write("Case #{0}: O won\n".format(i+1))
        continue

    # check diagonal /
    os = 0
    xs = 0
    for p in range(4):
        if(table[p][3-p] == 'X' or table[p][3-p] == 'T'):
            xs = xs + 1
        if(table[p][3-p] == 'O' or table[p][3-p] == 'T'):
            os = os + 1
        if(table[p][3-p] == '.'):
            ds = ds + 1
    if(xs == 4):
        fo.write("Case #{0}: X won\n".format(i+1))
        continue
    elif (os == 4):
        fo.write("Case #{0}: O won\n".format(i+1))
        continue

    # check lines -
    for r in range(4):
        os = 0
        xs = 0
        for c in range(4):
            if(table[r][c] == 'X' or table[r][c] == 'T'):
                xs = xs + 1
            if(table[r][c] == 'O' or table[r][c] == 'T'):
                os = os + 1
            if(table[r][c] == '.'):
                ds = ds + 1
        if(xs == 4):
            fo.write("Case #{0}: X won\n".format(i+1))
            found = True
            break
        elif (os == 4):
            fo.write("Case #{0}: O won\n".format(i+1))
            found = True
            break
    if found: continue

    # check columns |
    for c in range(4):
        os = 0
        xs = 0
        for r in range(4):
            if(table[r][c] == 'X' or table[r][c] == 'T'):
                xs = xs + 1
            if(table[r][c] == 'O' or table[r][c] == 'T'):
                os = os + 1
            if(table[r][c] == '.'):
                ds = ds + 1
        if(xs == 4):
            fo.write("Case #{0}: X won\n".format(i+1))
            found = True
            break
        elif (os == 4):
            fo.write("Case #{0}: O won\n".format(i+1))
            found = True
            break
    if found: continue

    if(ds == 0):
        fo.write("Case #{0}: Draw\n".format(i+1))
    else:
        fo.write("Case #{0}: Game has not completed\n".format(i+1))

