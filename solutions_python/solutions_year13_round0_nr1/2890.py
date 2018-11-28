#!/usr/bin/env python

import sys
import numpy as np

def check(raw_board):
    board = np.zeros((4,4), dtype=int);
    Tx = 0; Ty = 0
    empty_cell = False
    for i,line in enumerate(raw_board):
        for j,ch in enumerate(line):
            if ch == "X":
                board[i,j] = -1;
            elif ch == "O":
                board[i,j] = 1;
            elif ch == "T":
                Tx = i; Ty = j
                board[i,j] = 1
            elif ch == ".":
                empty_cell = True;

    #print(board);
    hor = np.sum(board, axis=0)
    if (hor == 4).any():
        return "O won";
    ver = np.sum(board, axis=1);
    if (ver == 4).any():
        return "O won";
    if np.sum(np.diag(board)) == 4:
        return "O won";
    if board[0,3] + board[1,2] + board [2,1] + board[3,0] == 4:
        return "O won";

    board *= -1;
    board[Tx, Ty] = 1;

    hor = np.sum(board, axis=0)
    if (hor == 4).any():
        return "X won";
    ver = np.sum(board, axis=1);
    if (ver == 4).any():
        return "X won";
    if np.sum(np.diag(board)) == 4:
        return "X won";
    if (board[0,3] + board[1,2] + board [2,1] + board[3,0]) == 4:
        return "X won";

    if not empty_cell:
        return "Draw"
    else:
        return "Game has not completed"

def main():
    with open(sys.argv[1], 'r') as fin:
        num_boards = int(fin.readline());
        for idx in range(num_boards):
            board = [];
            while len(board) != 4:
                line = fin.readline().strip();
                if len(line) == 4:
                    board.append(line);
            #for l in board:
            #    print(l);

            # Brute force all possible ways to win.
            r = check(board);
            print("Case #%i: %s" % (idx+1, r));


if __name__ == "__main__":
    main();

