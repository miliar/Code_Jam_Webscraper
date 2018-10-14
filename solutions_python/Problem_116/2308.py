#!/usr/bin/env python

import re
import pprint
import sys

class Board(object):

    finished = True

    def __init__(self, board):
        self.board = board
        for row in self.board:
            if '.' in row:
                self.finished = False

    def parse_board(self):
        t = list()
        for row in self.rows:
            t.append(row)
        for col in self.cols:
            t.append(col)
        for diag in self.diags:
            t.append(diag)

        for r in t:
            w = self.winner(r)
            if w:
                return w
        return None

    def winner(self, row):
        for player in ['X', 'O']:
            if re.match('[%sT]{4}' % (player,), ''.join(row)):
                return player
        return None

    @property
    def rows(self):
        for row in self.board:
            yield row

    @property
    def cols(self):
        t = list()
        for i in range(4):
            t.append(range(4))
        for i in range(4):
            for j in range(4):
                t[j][i] = self.board[i][j]
        for row in t:
            yield row

    @property
    def diags(self):
        t = list()
        for i in range(2):
            t.append(range(4))
        for i in range(4):
            t[0][i] = self.board[i][i]
        for i in range(4):
            t[1][i] = self.board[3-i][i]

        for row in t:
            yield row

    def pprint(self):
        pprint.pprint(self.board)

if __name__  == "__main__":
    T = int(sys.stdin.readline())
    for case in range(1, T+1):
        b = list()
        for i in range(4):
            row = [c for c in sys.stdin.readline()]
            b.append(row[:4])
        b = Board(b)
        winner = b.parse_board()
        if winner:
            print "Case #%d: %s won" % (case, winner)
        elif b.finished:
            print "Case #%d: Draw" % (case)
        else:
            print "Case #%d: Game has not completed" % (case)
        sys.stdin.readline()
