#!/usr/bin/env python
import sys

X_WIN = ({'X', 'T'}, {'X'})
O_WIN = ({'O', 'T'}, {'O'})

case = 0
cases = None
board = list()
with open(sys.argv[1] if sys.argv[1:] else '/dev/stdin') as iostream:
    for line in iostream:
        line = line.strip()
        if not line:
            continue

        if not cases and line.isdigit():
            cases = int(line)
            continue

        board.extend(line)
        if len(board) == 16:
            case += 1
            slices = list()
            # Vertical
            for i in range(4):
                slices.append(set(board[i::4]))

            # Horizontal
            for i in range(0, 16, 4):
                slices.append(set(board[i:i+4]))

            # Diagonals
            slices.append(set(board[::5]))
            slices.append(set(board[3:15:3]))

            if X_WIN[0] in slices or X_WIN[1] in slices:
                message = "X won"
            elif O_WIN[0] in slices or O_WIN[1] in slices:
                message = "O won"
            elif '.' not in board:
                message = "Draw"
            else:
                message = "Game has not completed"

            board = list()
            print("Case #%i: %s" % (case, message))
