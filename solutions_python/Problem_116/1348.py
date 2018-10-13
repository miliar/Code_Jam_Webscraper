#!/usr/bin/env python
import copy

def readboards(filename):
    f = open(filename)
    numtests = int(f.readline())
    emptyboard = [['', '', '', ''], ['', '', '', ''],
                  ['', '', '', ''], ['', '', '' ,'']]
    boards = [copy.deepcopy(emptyboard) for _ in xrange(numtests)]
    row = 0
    t = 0
    for line in f:
        if t >= numtests:
            break
        if row >= 4:
            row = 0
            col = 0
            t += 1
            continue
        col = 0
        for char in line:
            if col >= 4:
                col = 0
                break
#            print 't =', t, 'row =', row, 'col =', col, 'char =', char
            boards[t][row][col] = char
            col += 1
        row += 1
    return boards

# returns 'X', 'O', 'D', or 'N'
# X = X won
# Y = Y won
# D = draw (all squares filled, no winner)
# N = not complete (there are still empty squares)
def checkseq(seq):
    assert len(seq) == 4
    has_x = 'X' in seq
    has_o = 'O' in seq
    has_empty = '.' in seq
    if has_x and not has_o and not has_empty:
        return 'X'
    if has_o and not has_x and not has_empty:
        return 'O'
    if has_empty:
        return 'N'
    else:
        return 'D'

def evalboard(board):
    rows = board
    cols = zip(*board)
    rdiag = [board[0][0], board[1][1], board[2][2], board[3][3]]
    ldiag = [board[3][0], board[2][1], board[1][2], board[0][3]]
    notcomplete = False
    for seq in rows + cols + [rdiag] + [ldiag]:
        result = checkseq(seq)
        if result == 'X' or result == 'O':
            return result
        if result == 'N':
            notcomplete = True
    if notcomplete:
        return 'N'
    else:
        return 'D'

def evalboards(boards):
    case = 1
    for board in boards:
        result = evalboard(board)
        if result == 'X':
            print 'Case #{}: X won'.format(case)
        elif result == 'O':
            print 'Case #{}: O won'.format(case)
        elif result == 'N':
            print 'Case #{}: Game has not completed'.format(case)
        elif result == 'D':
            print 'Case #{}: Draw'.format(case)
        case += 1

def main():
    import sys
    if len(sys.argv) < 2:
        print 'usage: ttt.py filename'
        exit(1)
    filename = sys.argv[1]
    boards = readboards(filename)
    evalboards(boards)

if __name__ == '__main__':
    main()
