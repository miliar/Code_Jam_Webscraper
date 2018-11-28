#!/usr/bin/env python -B

import sys

def analyze(board):
    winning_o = [{"O"}, {"T", "O"}]
    winning_x = [{"X"}, {"T", "X"}]

    for line in board:
        if set(line) in winning_o:
            return "O won"
        if set(line) in winning_x:
            return "X won"

    for column in map(list, zip(*board)):
        if set(column) in winning_o:
            return "O won"
        if set(column) in winning_x:
            return "X won"

    diag = set()
    for i in xrange(4):
        diag.add(board[i][i])
    if diag in winning_o:
        return "O won"
    if diag in winning_x:
        return "X won"

    diag = set()
    for i in xrange(4):
        diag.add(board[i][3-i])
    if diag in winning_o:
        return "O won"
    if diag in winning_x:
        return "X won"

    for line in board:
        if "." in line:
            return "Game has not completed"

    return "Draw"


def main():
    n = int(raw_input())
    for case_number in xrange(1, n + 1):
        board = []
        for __ in xrange(4):
            line = raw_input()
            board.append(line)
        raw_input()

        print "Case #{}: {}".format(case_number, analyze(board))


if __name__ == "__main__":
    import a
    a.main()
