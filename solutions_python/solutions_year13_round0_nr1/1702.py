#!/usr/bin/env python

import sys

t = int(sys.stdin.readline())

for i in range(t):
    map = []
    for j in range(4):
        map.append((sys.stdin.readline()))
    sys.stdin.readline()
    xw = False
    yw = False
    finished = True

    d1x = 0; d1o = 0; d1t = False
    d2x = 0; d2o = 0; d2t = False

    for x in range(4):
        hnx = 0; hno = 0; ht = False
        vnx = 0; vno = 0; vt = False

        if map[x][x] == 'X':
            d1x += 1
        elif map[x][x] == 'O':
            d1o += 1
        elif map[x][x] == 'T':
            d1t = True

        if map[x][3-x] == 'X':
            d2x += 1
        elif map[x][3-x] == 'O':
            d2o += 1
        elif map[x][3-x] == 'T':
            d2t = True

        for y in range(4):
            if map[x][y] == 'X':
                hnx += 1
            elif map[x][y] == 'O':
                hno += 1
            elif map[x][y] == 'T':
                ht = True
            else:
                finished = False

            if map[y][x] == 'X':
                vnx += 1
            elif map[y][x] == 'O':
                vno += 1
            elif map[y][x] == 'T':
                vt = True

        if (hnx == 4 or (hnx == 3 and ht) or
            vnx == 4 or (vnx == 3 and vt)):
            xw = True

        if (hno == 4 or (hno == 3 and ht) or
            vno == 4 or (vno == 3 and vt)):
            yw = True

    if (d1x == 4 or (d1x == 3 and d1t) or
        d2x == 4 or (d2x == 3 and d2t)):
        xw = True

    if (d1o == 4 or (d1o == 3 and d1t) or
        d2o == 4 or (d2o == 3 and d2t)):
        yw = True


    if xw and yw:
        print "Case #%d: Draw" % (i+1)
    elif xw:
        print "Case #%d: X won" % (i+1)
    elif yw:
        print "Case #%d: O won" % (i+1)
    elif finished:
        print "Case #%d: Draw" % (i+1)
    else:
        print "Case #%d: Game has not completed" % (i+1)
