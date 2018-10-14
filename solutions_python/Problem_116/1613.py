#!/usr/bin/env python

T = int(raw_input())

def winner(line):
    if 'X' in line and 'O' in line:
        return 0
    elif '.' in line:
        return 1
    elif 'X' in line:
        return 2
    elif 'O' in line:
        return 3

for t in range(T):
    board = []
    for i in range(4):
        board += [raw_input()]
    raw_input()
    rows = (
        board + 
        [[x[i] for x in board] for i in range(4)] +
        [
            [board[i][i] for i in range(4)],
            [board[i][3-i] for i in range(4)]
        ]
    )
    rm = 0
    for r in rows:
        rr = winner(r)
        if rm < 2:
            rm = max(rm, rr)
        elif rr >= 2 and rm != rr:
            rm = 0
            break
    print "Case #%d:" % (t+1,),
    if rm == 0:
        print "Draw"
    elif rm == 1:
        print "Game has not completed"
    elif rm == 2:
        print "X won"
    elif rm == 3:
        print "O won"
