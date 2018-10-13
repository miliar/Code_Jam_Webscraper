#!/usr/bin/python

""""Solve Problem A of the the Google Code Jam 2013 Qualification Round -
Tic-Tac-Toe-Tomek."""

import sys

BOARD_SIZE = 4


class Board(object):

    def __init__(self):
        self.board = []

    def read(self, ):
        for i in range(BOARD_SIZE):
            row = list(sys.stdin.readline().strip())
            assert len(row) == BOARD_SIZE
            self.board.append(row)

    def getRow(self, rowNumber):
        return self.board[rowNumber]

    def getCol(self, colNumber):
        return [self.board[i][colNumber] for i in range(BOARD_SIZE)]

    def getDiag(self, diagNumber):
        """Diagonal number 0 is top left to bottom right."""
        if diagNumber == 0:
            return [self.board[i][i] for i in range(BOARD_SIZE)]
        elif diagNumber == 1:
            return [self.board[i][BOARD_SIZE-1-i] for i in range(BOARD_SIZE)]
        else:
            raise ValueError("Only diagonals 0 and 1 exist")

    def _wonBy(self, player, line):
        wonOutright = line.count(player) == 4
        wonWithHelp = line.count(player) == 3 and line.count('T') == 1
        return wonOutright or wonWithHelp

    def rowWonBy(self, player, rowNumber):
        return self._wonBy(player, self.getRow(rowNumber))

    def colWonBy(self, player, colNumber):
        return self._wonBy(player, self.getCol(colNumber))

    def diagWonBy(self, player, diagNumber):
        return self._wonBy(player, self.getDiag(diagNumber))

    def gameWonBy(self, player):
        for i in range(BOARD_SIZE):
            if self.rowWonBy(player, i) or self.colWonBy(player, i):
                return True
        return self.diagWonBy(player, 0) or self.diagWonBy(player, 1)

    def completed(self):
        return '.' not in ''.join(''.join(row) for row in self.board)


def main():
    numberOfBoards = int(sys.stdin.readline().strip())
    for i in range(numberOfBoards):
        print "Case #%i: "%(i+1),
        board = Board()
        board.read()
        if board.gameWonBy('X'):
            print "X won"
        elif board.gameWonBy('O'):
            print "O won"
        elif board.completed():
            print "Draw"
        else:
            print "Game has not completed"
        sys.stdin.readline()  # Consume empty line


if __name__ == '__main__':
    main()
