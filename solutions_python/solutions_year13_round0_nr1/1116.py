#!/usr/bin/env python
statuses = {
    'X': 'X won',
    'O': 'O won',
    'D': 'Draw',
    '.': 'Game has not completed'
}

def getstatus(board):
    n = len(board)
    diags = [[board[i][i] for i in range(n)],
             [board[n - i - 1][i] for i in range(n)]]
    for player in 'XO':
        # horizontal (rows) & vertical (columns) & 2 diagonals
        if any(row.count(player) + row.count('T') == len(row)
               for row in board + zip(*board) + diags):
            return player
    if any('.' in row for row in board):
        return '.' # not completed
    return 'D' # draw

for i in range(1, int(raw_input()) + 1):
    st = statuses[getstatus([raw_input() for _ in range(4)])]
    print "Case #%d: %s" % (i, st)
    raw_input() # consume empty line
