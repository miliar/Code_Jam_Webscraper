#!/usr/bin/env python2

M = ['X', 'O']

with open("a.in") as f:
    k = int(f.readline().strip())

    for kk in range(k):
        board = []
        dot = False
        winner = None

        for l in range(4):
            board.append(f.readline().strip())

        f.readline()

        for i in range(4):
            row = board[i]
            col = "".join([board[j][i] for j in range(4)])

            for check in (row, col):
                if '.' in check:
                    dot = True
                elif check.replace('T', 'X') == 'XXXX':
                    winner = 'X'
                elif check.replace('T', 'O') == 'OOOO':
                    winner = 'O'

        dia = ["", ""]
        for i in range(4):
            dia[0] += board[i][i]
            dia[1] += board[i][3-i]

        for d in dia:
            if d.replace('T', 'X') == 'XXXX':
                winner = 'X'
            elif d.replace('T', 'O') == 'OOOO':
                winner = 'O'


        if winner:
            print "Case #{0}: {1} won".format(kk + 1, winner)
        elif not dot:
            print "Case #{0}: Draw".format(kk + 1)
        else:
            print "Case #{0}: Game has not completed".format(kk + 1)


