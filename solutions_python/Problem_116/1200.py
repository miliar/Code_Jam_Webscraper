#!/usr/bin/env python

import sys

def parse_boards(boardfile):
    num_boards = int(boardfile.readline().strip())

    boards = []

    for i in range(num_boards):
        board = []
        for j in range(4):
            board.append(boardfile.readline().strip())
        boardfile.readline()
        boards.append(board)

    return boards

def check_board_state(board):
    not_done = False
    for row in board:
        if '.' in row:
            not_done = True
        rowset = set(row)
        rowset.discard('T')
        if rowset == set(('X')) or rowset == set(('O')):
            return rowset.pop() + ' won'

    for col in zip(*board):
        col = ''.join(col)
        if '.' in col:
            not_done = True
        colset = set(col)
        colset.discard('T')
        if colset == set(('X')) or colset == set(('O')):
            return colset.pop() + ' won'

    diags = ["", ""]
    for i, row in enumerate(board):
        diags[0] += row[i]
        diags[1] += row[3-i]

    for diag in diags:

        if '.' in diag:
            not_done = True
        diagset = set(diag)
        diagset.discard('T')
        if diagset == set(('X')) or diagset == set(('O')):
            return diagset.pop() + ' won'

    if not_done:
        return 'Game has not completed'
    else:
        return 'Draw'

if __name__ == '__main__':
    boards = parse_boards(open(sys.argv[1]))
    for i, board in enumerate(boards, start=1):
        print 'Case #%d: %s' % (i, check_board_state(board))
