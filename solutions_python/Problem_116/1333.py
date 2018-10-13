#!/usr/bin/python

import sys

def get_cases(fo):
    """Convert the input file into a list of 16-chars board strings"""
    f=fo.readlines()
    num_cases=int(f[0])
    cases=[]
    for i in range(num_cases):
        first=i*5+1
        last=first+4
        case= ''.join([l.strip() for l in f[first:last]])
        cases.append(case)
    return cases

class TTTT(object):
    """A Tic-Tac-Toe-Tomek board."""
    
    _x_wins = set(["XXXX", "TXXX", "XTXX", "XXTX", "XXXT"])
    _o_wins = set(["OOOO", "TOOO", "OTOO", "OOTO", "OOOT"])
    
    def __init__(self, board):
        """Build a board from a 16-chars string of {'X', 'Y', 'O', '.'}"""
        self._board        = board
        self._quartests    = self._get_quartets()
        self._has_finished = '.' in self._board
    
    def get_result(self):
        if self._is_x_wins():
            return "X won"
        elif self._is_o_wins():
            return "O won"
        elif self._has_finished:
            return "Game has not completed"
        else:
            return "Draw"    
    
    def _is_x_wins(self):
        return len(set(self._quartests).intersection(TTTT._x_wins))>0

    def _is_o_wins(self):
        return len(set(self._quartests).intersection(TTTT._o_wins))>0
    
    def _get_quartets(self):
        return self._get_rows()+self._get_columns()+self._get_diagonals()
    
    def _get_rows(self):
        return [self._board[i*4:i*4+4] for i in range(4)]

    def _get_columns(self):
        return [self._board[i]+self._board[i+4]+self._board[i+8]+self._board[i+12] for i in range(4)]

    def _get_diagonals(self):
        return [self._board[0]+self._board[5]+self._board[10]+self._board[15],
            self._board[3]+self._board[6]+self._board[9]+self._board[12]]

cases=get_cases(sys.stdin)
boards=[TTTT(case) for case in cases]

for i in range(len(boards)):
    print "Case #%d: %s" % (i+1, boards[i].get_result())

