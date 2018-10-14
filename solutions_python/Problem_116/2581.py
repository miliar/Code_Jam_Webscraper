from sys import argv
import ast

script, datafilename, outputfilename = argv

outfile = open(outputfilename, mode='w')

rtext = {
        'o': 'O won',
        'x': 'X won',
        'draw': 'Draw',
        'notdone': 'Game has not completed'}
results = []
boards = []

with open(datafilename) as datafile:
    T = int(datafile.readline())
    for i in range(T):
        board = []
        for j in range(4):
            row = datafile.readline().replace('\n','')
            board.append(row)
        boards.append(board)
        datafile.readline()

for boardnum, board in enumerate(boards):
    owin = False
    xwin = False
    nilcount = 0
    for row in board:
        for space in row:
            if space == '.':
                nilcount = nilcount + 1
    for row in board:
        ocount = 0
        xcount = 0
        for space in row:
            if space == 'T':
                ocount = ocount + 1
                xcount = xcount + 1
            elif space == 'O':
                ocount = ocount + 1
            elif space == 'X':
                xcount = xcount + 1
        if ocount == 4:
            owin = True
        elif xcount == 4:
            xwin = True
    for j in range(4):
        ocount = 0
        xcount = 0
        for i in range(4):
            space = board[i][j]
            if space == 'T':
                ocount = ocount + 1
                xcount = xcount + 1
            elif space == 'O':
                ocount = ocount + 1
            elif space == 'X':
                xcount = xcount + 1
        if ocount == 4:
            owin = True
        elif xcount == 4:
            xwin = True

    ocount = 0
    xcount = 0
    for i in range(4):
        line = board[i]
        space = line[i]
        if space == 'T':
            ocount = ocount + 1
            xcount = xcount + 1
        elif space == 'O':
            ocount = ocount + 1
        elif space == 'X':
            xcount = xcount + 1
    if ocount == 4:
        owin = True
    elif xcount == 4:
        xwin = True

    ocount = 0
    xcount = 0
    for i in range(4):
        space = board[i][3-i]
        if space == 'T':
            ocount = ocount + 1
            xcount = xcount + 1
        elif space == 'O':
            ocount = ocount + 1
        elif space == 'X':
            xcount = xcount + 1
    if ocount == 4:
        owin = True
    elif xcount == 4:
        xwin = True

    if owin == True:
        results.append(rtext['o'])
    elif xwin == True:
        results.append(rtext['x'])
    elif nilcount == 0:
        results.append(rtext['draw'])
    else:
        results.append(rtext['notdone'])

for num, val in enumerate(results):
    outfile.write('Case #%d: %s\n' % (num + 1, val))
outfile.close()
