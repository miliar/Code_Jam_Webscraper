__author__ = 'Xapheus'

import sys

f = open("D-small-attempt4.in", 'r')
o = open("output.txt", 'w')
num_cases = int(f.readline())

for c in range(num_cases):
    # read in misc problem constants
    gameParameters = list(map(int, f.readline().split(' ')))
    x, y, z = gameParameters

    if x == 1:
        o.write("Case #%d: GABRIEL" % ((c+1)))
    if x == 2:
        if ((y * z)% 2 == 0):
            o.write("Case #%d: GABRIEL" % ((c+1)))
        else:
            o.write("Case #%d: RICHARD" % ((c+1)))

    if x == 3:
        if ((y * z) % 3 == 0):
            if (y == 1 or z == 1):
                o.write("Case #%d: RICHARD" % ((c+1)))
            else:
                o.write("Case #%d: GABRIEL" % ((c+1)))
        else:
            o.write("Case #%d: RICHARD" % ((c+1)))
    if x == 4:
        if ((y * z) % 4 == 0):
            if (y == 1 or z == 1):
                o.write("Case #%d: RICHARD" % ((c+1)))
            elif (y == 2 or z == 2):
                o.write("Case #%d: RICHARD" % ((c+1)))
            elif (y == 3 or z == 3):
                o.write("Case #%d: GABRIEL" % ((c+1)))
            else:
                print("Case #%d: GABRIEL" % ((c+1)))
        else:
            print("Case #%d: RICHARD" % ((c+1)))