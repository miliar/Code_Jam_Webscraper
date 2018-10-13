#!/usr/bin/python2

def readf(f):
    board = []
    for i in range(4):
        board.append(f.readline()[:-1])
    f.readline()
    return board

def try_row(board, r, s):
    line = board[r];
    for c in line:
        if c != s and c != 'T':
            return False
    return True

def try_col(board, c, s):
    for r in range(len(board)):
        if board[r][c] != s and board[r][c] != 'T':
            return False
    return True

def try_dia(board, s):
    res = True
    for r in range(len(board)):
        if board[r][r] != s and board[r][r] != 'T':
            res = False
            break
    if res:
        return res
    for r in range(len(board)):
        if board[r][3 - r] != s and board[r][3 - r] != 'T':
            return False
    return True

def try_all(board, s):
    N = 4
    for r in range(N):
        if try_row(board, r, s):
            return True
    for c in range(N):
        if try_col(board, c, s):
            return True
    if try_dia(board, s):
        return True
    return False
    
def solve_case(f):
    board = readf(f)
    if try_all(board, 'X'):
        print 'X', "won"
        return
    if try_all(board, 'O'):
        print 'O', "won"
        return
    N = 4
    for r in range(N):
        for c in range(N):
            if board[r][c] == '.':
                print 'Game has not completed'
                return
    print 'Draw'

if __name__=="__main__":
    f = file("tictac.case")
    n = int(f.readline())
    for i in range(n):
        print "Case #%d:" % (i + 1),
        solve_case(f)

