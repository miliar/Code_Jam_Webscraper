#!/usr/bin/env python

import numpy

num = int(raw_input())

for i in range(num):
    game = []
    for j in range(4):
        row = raw_input()
        row = [c for c in row]
        game.append(row)
    raw_input()

    has_dot = False
    owin = False
    xwin = False
    for row in game:
        if '.' in row:
            has_dot = True
            continue

        ord_row = map(ord, row)
        row_sum = sum(ord_row)
        if row_sum==ord('O')*4 or row_sum==(ord('O')*3+ord('T')):
            owin = True
            break
        elif row_sum==ord('X')*4 or row_sum==(ord('X')*3+ord('T')):
            xwin=True
            break

    if xwin:
        print "Case #%d: X won" % (i+1)
        continue
    elif owin:
        print "Case #%d: O won" % (i+1)
        continue

    tgame = numpy.transpose(numpy.array(game))
    for row in tgame:
        ord_row = map(ord, row)
        row_sum = sum(ord_row)
        if row_sum==ord('O')*4 or row_sum==(ord('O')*3+ord('T')):
            owin = True
            break
        elif row_sum==ord('X')*4 or row_sum==(ord('X')*3+ord('T')):
            xwin=True
            break
    if xwin:
        print "Case #%d: X won" % (i+1)
        continue
    elif owin:
        print "Case #%d: O won" % (i+1)
        continue

    dia = ord(game[0][0]) + ord(game[1][1]) + ord(game[2][2]) + ord(game[3][3])
    if dia==ord('O')*4 or dia==(ord('O')*3+ord('T')):
        owin = True
    elif dia==ord('X')*4 or dia==(ord('X')*3+ord('T')):
        xwin = True
    
    dia = ord(game[0][3]) + ord(game[1][2]) + ord(game[2][1]) + ord(game[3][0])
    if dia==ord('O')*4 or dia==(ord('O')*3+ord('T')):
        owin = True
    elif dia==ord('X')*4 or dia==(ord('X')*3+ord('T')):
        xwin = True

    if xwin:
        print "Case #%d: X won" % (i+1)
        continue
    elif owin:
        print "Case #%d: O won" % (i+1)
        continue
    elif has_dot:
        print "Case #%d: Game has not completed" % (i+1)
    else:
        print "Case #%d: Draw" % (i+1)


