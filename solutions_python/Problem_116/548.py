#! /usr/bin/env python

from sys import stdin


class Board(object):
    STATUS_X_WON = 'X won'
    STATUS_O_WON = 'O won'
    STATUS_DRAW = 'Draw'
    STATUS_NOT_COMPLETED = 'Game has not completed'

    def __init__(self, lines):
        self.squares = lines

    def get_scanlines(self):
        scanlines = self.squares[:] # Rows
        scanlines += [''.join([line[c] for line in self.squares]) for c in range(4)] # Columns
        scanlines.append(''.join([line[idx] for idx, line in enumerate(self.squares)])) # Diagonal 1
        scanlines.append(''.join([line[3 - idx] for idx, line in enumerate(self.squares)])) # Diagonal 2
        return scanlines

    def status(self):
        scanlines = self.get_scanlines()
        value = self.STATUS_DRAW
        for scanline in scanlines:
            scanline = ''.join(sorted(scanline))
            if '.' in scanline:
                value = self.STATUS_NOT_COMPLETED
            elif scanline in ('TXXX', 'XXXX'):
                return self.STATUS_X_WON
            elif scanline in ('OOOT', 'OOOO'):
                return self.STATUS_O_WON
        return value


if __name__ == '__main__':
    num_cases = int(stdin.readline().strip())

    for i in range(num_cases):
        lines = [stdin.readline().strip() for r in range(4)]
        dummy_line = stdin.readline()
        board = Board(lines)
        status = board.status()
        #print lines
        #print board.get_scanlines()
        print('Case #{}: {}'.format(i+1, status))

