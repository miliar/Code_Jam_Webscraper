#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print('Usage: {0} IN_FILE [OUT_FILE]'.format(sys.argv[0]))
        return

    in_file = open(sys.argv[1])
    out_file = open(sys.argv[1]+'.txt' if len(sys.argv) == 2 else sys.argv[2], mode='w')
    cases = int(next(in_file))
    for i in range(cases):
        lines = [next(in_file).strip() for x in range(4)]
        board = make_board(lines)
        result = check_result(board)
        out_file.write('Case #{0}: {1}\n'.format(i+1, Result.to_str(result)))
        try:
            next(in_file)
        except StopIteration:
            break

def make_board(lines):
    x = 0
    y = 0
    board = [['.' for x in range(4)] for x in range(4)]
    for line in lines:
        x = 0
        for char in line:
            board[x][y] = Piece.from_char(char)
            x += 1
        y += 1
    return board

def check_result(board):
    for y in range(4):
        result = check_x(board, y)
        if Result.is_win(result):
            return result
    for x in range(4):
        result = check_y(board, x)
        if Result.is_win(result):
            return result
    for x in (0, 3):
        result = check_diag(board, x)
        if Result.is_win(result):
            return result
    for x in range(4):
        for y in range(4):
            if board[x][y] == Piece.E:
                return Result.NOT
    return Result.DRAW

def check_x(board, y):
    piece = board[0][y]
    for i in range(4):
        if board[i][y] != piece and board[i][y] != Piece.T:
            break
    else:
        return Piece.to_res(piece)
    return Result.NOT

def check_y(board, x):
    piece = board[x][0]
    for i in range(4):
        if board[x][i] != piece and board[x][i] != Piece.T:
            break
    else:
        return Piece.to_res(piece)
    return Result.NOT

def check_diag(board, x):
    piece = board[x][0]
    sign = 1 if x == 0 else -1
    for i in range(4):
        if board[x+i*sign][i] != piece and board[x+i*sign][i] != Piece.T:
            break
    else:
        return Piece.to_res(piece)
    return Result.NOT

class Piece:
    E, X, O, T = range(4)

    def to_res(piece):
        if piece == Piece.X or piece == Piece.O:
            return piece
        else:
            return Result.NOT

    def from_char(char):
        if char == 'X': return Piece.X
        if char == 'O': return Piece.O
        if char == 'T': return Piece.T
        return Piece.E

class Result:
    NOT, X, O, DRAW = range(4)

    def is_win(result):
        return result == Result.X or result == Result.O

    def to_str(result):
        if result == Result.NOT:
            return "Game has not completed"
        if result == Result.X:
            return "X won"
        if result == Result.O:
            return "O won"
        return "Draw"

if __name__ == "__main__":
    main()
