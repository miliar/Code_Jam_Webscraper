#!/usr/bin/python

def read_ints():
    return map(int, raw_input().split())

def read_str():
    return raw_input()

def read_board():
    board=[]
    for i in xrange(4):
        board.append(read_str())
    try:
        read_str()
    except:
        pass
    return board

def has_empty(board):
    for r in board:
        for c in r:
            if c == '.':
                return True
    return False

def is_win(board, player_tokens):
    # Check diagonals
    if all([board[i][i] in player_tokens for i in range(len(board))]):
        return True
    if all([board[3-i][i] in player_tokens for i in range(len(board))]):
        return True
    # Check rows
    for i in range(len(board)):
        if all([board[i][j] in player_tokens for j in range(len(board[i]))]):
            return True
    # Check columns
    for i in range(len(board)):
        if all([board[j][i] in player_tokens for j in range(len(board[i]))]):
            return True
    return False

def tictac():
    board=read_board()
    if is_win(board, ['X', 'T']):
        return "X won"
    if is_win(board, ['O', 'T']):
        return "O won"
    if not has_empty(board):
        return "Draw"
    return "Game has not completed"

T=read_ints()[0]
for t in xrange(T):
    print "Case #%d: %s" %(t+1, tictac())
