#!/usr/bin/env python

f = open('large.in')
num_games = int(f.readline().strip())
for case in xrange(num_games):
    xwin = False
    owin = False
    complete = True
    game = []
    for j in xrange(4):
        line = f.readline().strip()
        if line.count('.'): complete = False
        if line.replace("T", "X") == "XXXX": xwin = True
        if line.replace("T", "O") == "OOOO": owin = True
        game.append(line)
    # Check diagonals
    d1 = "".join([game[j][j] for j in xrange(4)])
    d2 = "".join([game[j][3-j] for j in xrange(4)])
    if d1.replace("T", "X") == 'XXXX': xwin = True
    if d1.replace("T", "O") == 'OOOO': owin = True
    if d2.replace("T", "X") == 'XXXX': xwin = True
    if d2.replace("T", "O") == 'OOOO': owin = True
    # Check verticals
    verticals = ["".join(x) for x in [[game[i][j] for i in xrange(4)] for j in xrange(4)]]
    for line in verticals:
        if line.replace("T", "X") == "XXXX": xwin = True
        if line.replace("T", "O") == "OOOO": owin = True

    status = "Draw"
    if xwin:
        status = "X won"
    elif owin:
        status = "O won"
    elif not complete:
        status = "Game has not completed"
    print "Case #%d: %s" % (case + 1, status)

    #skip blank line
    f.readline()
