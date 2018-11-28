#!/usr/bin/env python
#
# Luke Southam <luke@devthe.com>
# GCJ Problem A. Tic-Tac-Toe-Tomek
#

T = int(raw_input())

symbols = ["X","O",".","T"]

for test_i in xrange(T):
    board = [[],[],[],[]]
    unfinished = 0

    for i in xrange(4):
        line = raw_input()
        for char in line:
            if char == ".":
                unfinished += 1
            if char in symbols:
                board[i].append(char)

    state = None

    lists = [board[i] for i in xrange(4)]
    lists.extend([[board[i][j] for i in xrange(4)] for j in xrange(4)])
    lists.append([board[i][i] for i in xrange(4)])
    lists.append([board[3 - i][i] for i in xrange(4)])

    for l in lists:
        symbols_freq = {symbol:0 for symbol in symbols}

        for c in l:
            symbols_freq[c] += 1

        if symbols_freq["O"] == 4 or (symbols_freq["T"] == 1 and symbols_freq["O"] == 3):
            state = "O won"
        elif symbols_freq["X"] == 4 or (symbols_freq["T"] == 1 and symbols_freq["X"] == 3):
            state =  "X won"

    if unfinished and not state:
        state = "Game has not completed"
    elif not state:
        state = "Draw"


    print "Case #%i: %s" % (test_i + 1, state)
    try:
        raw_input()
    except EOFError:
        pass
