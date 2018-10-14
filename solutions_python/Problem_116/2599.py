#!/usr/bin/env python
# -*- coding: utf-8 -*-

def game_status(board):
    statuses = ('X won', 'O won', 'Draw', 'Game has not completed')
    point = False
    for row in board:
        if row.count('X') == 4 or row.count('X') == 3 and 'T' in row:
            return statuses[0]
        elif row.count('O') == 4 or row.count('O') == 3 and 'T' in row:
            return statuses[1]
        if '.' in row:
            point = point or True
    for i in xrange(0, 4):
        col = [row[i] for row in board]
        if col.count('X') == 4 or col.count('X') == 3 and 'T' in col:
            return statuses[0]
        elif col.count('O') == 4 or col.count('O') == 3 and 'T' in col:
            return statuses[1]
    for i in xrange(0, 2):
        diag = [board[j][j] for j in xrange(i, 4)]
        if diag.count('X') == 4 or diag.count('X') == 3 and 'T' in diag:
            return statuses[0]
        elif diag.count('O') == 4 or diag.count('O') == 3 and 'T' in diag:
            return statuses[1]
    for i in xrange(2, 4):
        diag = [board[j][3 - j] for j in xrange(0, i + 1)]
        if diag.count('X') == 4 or diag.count('X') == 3 and 'T' in diag:
            return statuses[0]
        elif diag.count('O') == 4 or diag.count('O') == 3 and 'T' in diag:
            return statuses[1]
    return statuses[3] if point else statuses[2]     
        
def main():
    (cases, results) = (int(raw_input()), [])
    for i in xrange(0, cases):
        board = [[k for k in raw_input()] for j in xrange(0, 4)]
        try:
            empty = raw_input()
        except EOFError:
            pass
        results.append((i + 1, game_status(board)))
    for result in results:
        print "Case #%d: %s" % (result[0], result[1])
    
if __name__ == '__main__':
    main()