#! /usr/bin/env python

def read_board():
    return [raw_input().replace('\n', '') for i in range(4)]

def check_seq(seq):
    xcount = seq.count('X')
    ycount = seq.count('O')
    tcount = seq.count('T')
    if xcount + tcount == 4:
        return 'X won'
    elif ycount + tcount == 4:
        return 'O won'
    return None

def result(board):
    for row in board:
        result = check_seq(row)
        if result:
            return result

    for col in [[row[i] for row in board] for i in range(4)]:
        result = check_seq(col)
        if result:
            return result

    diag = [board[i][i] for i in range(4)]
    result = check_seq(diag)
    if result:
        return result
    diag = [board[3-i][i] for i in range(4)]
    result = check_seq(diag)
    if result:
        return result

    for row in board:
        for c in row:
            if c == '.':
                return 'Game has not completed'
    return 'Draw'

def main():
    n = int(raw_input())

    for i in range(n):
        board = read_board()
        print 'Case #%d: %s' % (i+1, result(board))
        raw_input() # discard new line

if __name__ == '__main__':
    main()
