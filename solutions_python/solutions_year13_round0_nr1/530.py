#! /usr/bin/env python3


def parse_board(*lines):
    return ''.join(lines)


def evaluate_board(board):
    lines = []

    X = board.replace("T", "X")
    for i in range(4):
        # horizontal lines
        lines.append(X[i * 4:i * 4 + 4])
        # vertical lines
        lines.append(X[i:i + 13:4])
    # diagonal lines
    lines.append(X[:16:5])
    lines.append(X[3:13:3])
    O = board.replace("T", "O")
    for i in range(4):
        lines.append(O[i * 4:i * 4 + 4])
        lines.append(O[i:i + 13:4])
    lines.append(O[:16:5])
    lines.append(O[3:13:3])

    if 'XXXX' in lines:
        return 'X won'
    if 'OOOO' in lines:
        return 'O won'
    if '.' in board:
        return 'Game has not completed'
    return 'Draw'


T = int(input())
for case in range(T):
    board = parse_board(input(), input(), input(), input())
    if case != T - 1:
        input()
    print("Case #{0}: {1}".format(case + 1, evaluate_board(board)))
