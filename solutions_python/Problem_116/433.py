# -*- coding: utf-8 -*-


def who_win(board):
    for player in ['X', 'O']:

        for i in xrange(0, 4):
            line = board[i]
            line_processed = [c for c in line if c == player or c == 'T']
            if len(line_processed) == 4:
                return player

        for i in xrange(0, 4):
            column = [line[i] for line in board]
            column_processed = [c for c in column if c == player or c == 'T']
            if len(column_processed) == 4:
                return player

        for i in [0, -3]:
            diagonal = []
            for line in board:
                diagonal.append(line[abs(i)])
                i += 1
            diagonal_processed = [c for c in diagonal if c == player or c == 'T']
            if len(diagonal_processed) == 4:
                return player

    return 0


n = int(input())
board_set = []
for i in xrange(0, n):
    current_board = []
    for j in xrange(0, 4):
        current_board.append(list(raw_input()))
    if i != n-1:
        blank_line = raw_input()
    board_set.append(current_board)

i = 1
for board in board_set:
    if who_win(board) == 'X':
        print "Case #" + str(i) + ": X won"
    elif who_win(board) == 'O':
        print "Case #" + str(i) + ": O won"
    else:
        united_board = []
        for line in board:
            united_board += line
        is_finish = False if '.' in united_board else True
        if is_finish:
            print "Case #" + str(i) + ": Draw"
        else:
            print "Case #" + str(i) + ": Game has not completed"
    i += 1