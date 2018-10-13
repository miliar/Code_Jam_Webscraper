#! /usr/bin/env python

import sys

# Heavy assumption on 4x4 board
def win(letter, board):
    w = letter * 4
    s = board.replace('T', letter)
    horiz = s[0:4] == w or s[4:8] == w or s[8:12] == w or s[12:] == w
    vert = False
    for i in xrange(4):
        vert = vert or ''.join([s[i], s[i+4], s[i+8], s[i+12]]) == w
    diag = ''.join([s[0], s[5], s[10], s[15]]) == w or \
        ''.join([s[3], s[6], s[9], s[12]]) == w

    return horiz or vert or diag

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage: %s [FILE]' % sys.argv[0]

    with open(sys.argv[1], 'r') as f:
        num = int(f.readline())

        for i in xrange(num):
            print 'Case #%d:' % (i + 1),

            # Dirty
            s = ''
            for i in xrange(4):
                s += f.readline().strip()

            if win('X', s):
                print 'X won'
            elif win('O', s):
                print 'O won'
            elif '.' in s:
                print 'Game has not completed'
            else:
                print 'Draw'

            f.readline()
