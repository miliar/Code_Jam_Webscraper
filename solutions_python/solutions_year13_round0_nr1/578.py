#!/usr/bin/env python
# coding=utf-8
from __future__ import print_function
from sys import stdin, stdout

patterns = [ map(f, range(4)) for f in
        [(lambda y:(lambda x: (x, y)))(y) for y in range(4)]
      + [(lambda x:(lambda y: (x, y)))(x) for x in range(4)]
      + [(lambda x: (x, x))]
      + [(lambda x: (x, 3-x))] ]

def won(player, board, pattern):
    return all(map(lambda (x,y): (board[x][y] in (player, 'T')), pattern))

def solve(board):
    res = "Game has not completed" if any(map((lambda row: '.' in row), board)) else "Draw"
    winner = None
    for player in "XO":
        for pattern in patterns:
            if won(player, board, pattern):
                if winner is not None and winner != player:
                    raise AssertionError("Two winners!")
                winner = player
    if winner:
        res = "{0} won".format(winner)
    return res


if __name__ == "__main__":
    n = int(stdin.readline())
    for i in range(n):
        board = [stdin.readline().strip() for j in range(4)]
        print("Case #{0}: {1}".format(i+1, solve(board)))
        stdin.readline()
