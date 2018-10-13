#!/usr/bin/env python

# let O be 0, X be 1 and we check that the sum % M == 0. So
# 0 % M = 0
# 4 % M = 0
# T % M == 0 
# (3+T) % M = 0
# 1 % M != 0
# 2 % M !=0
# 
# 1 X, 3 O  | 1
# 2 X, 2 O  | 2
# 3 X, 1 O  | 3
#
# 1 X, 1 T, 2 O | 1+T
# 2 X, 1 T, 1 O | 2+T


def readBoard():
    board = []

    for row in range(4):
        board.append(raw_input())
        
    return board

def isSolution(board):
    # check diag 1
    diag1 = (board[0][0], False if board[0][0]=='.' else all([(board[i][i]==board[0][0]) for i in range(1,4)]))
    if diag1[1]:
        return diag1[0]+' won'
    # check diag 2
    diag2 = (board[3][0], False if board[0][0]=='.' else all([board[3-i][i]==board[3][0] and board[3-i][i]!='.' for i in range(3,0,-1)]))
    if diag2[1]:
        return diag2[0]+' won'
    # check column1
    if board[0][0] == board[3][0]!='.':
        if board[1][0] == board[2][0] == board[3][0]:
            return board[0][0]+' won'
    # check column4
    if board[0][3] == board[3][3]!='.':
        if board[0][1] == board[0][2] == board[0][3]:
            return board[0][3]+' won'
    # check column2
    if board[1][1] == board[2][1]!='.':
        if board[0][1] == board[3][1] == board[1][1]:
            return board[1][1]+' won'
    # check column3
    if board[2][2] == board[1][2]!='.':
        if board[0][2] == board[3][2] == board[2][2]:
            return board[2][2]+' won'
    # check row1
    if board[0][0] == board[0][3]!='.':
        if board[0][1] == board[0][2] == board[0][3]:
            return board[0][0]+' won'
    # check column4
    if board[3][0] == board[3][3]!='.':
        if board[1][0] == board[2][0] == board[3][0]:
            return board[0][3]+' won'
    # check column2
    if board[1][1] == board[1][2]!='.':
        if board[1][0] == board[1][3] == board[1][1]:
            return board[1][1]+' won'
    # check column3
    if board[2][2] == board[2][1]!='.':
        if board[2][0] == board[2][3] == board[2][2]:
            return board[2][2]+' won'
    # check if game has ended
    if any(map(lambda r: '.' in r, board)):
        return 'Game has not completed'
    else:
        return 'Draw'


def result(board):
    # if there is T, duplicate the board
    hasT = any(map(lambda r: 'T' in r, board))
    if not hasT:
        return isSolution(board)
    # duplicate board
    for T in 'XO':
        b = map(lambda r: r.replace('T', T), board)
        s = isSolution(b)
        if 'won' in s:
            return s
        if T=='O':
            return s

if __name__ == '__main__':
    z = raw_input()
    for i in range(1, int(z)+1):
        board = readBoard()
        print 'Case #%d: %s' % (i, result(board))
        raw_input()
    pass
