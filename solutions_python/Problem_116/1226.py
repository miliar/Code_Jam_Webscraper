#!/usr/bin/env python

def check_full(board):
    return '.' in board[0] or '.' in board[1] or '.' in board[2] or '.' in board[3]

def check_set(s):
    s.discard('T')
    if s == set(['X']):
        return 'X'
    elif s == set(['O']):
        return 'O'

def check_rows(board):
    for i in xrange(4):
        r = set(board[i])
        res = check_set(r)
        if res:
            return res

def check_cols(board):
    for i in xrange(4):
        c = set(board[j][i] for j in xrange(4))
        res = check_set(c)
        if res:
            return res

def check_diag(board):
    d1 = set(board[i][i] for i in xrange(4))
    res = check_set(d1)
    if res:
        return res
    return check_set(set(board[i][3-i] for i in xrange(4)))

t = int(raw_input())

for caseno in xrange(1, t+1):
    board = [raw_input() for _ in xrange(4)]
    winner = None
    completed = False

    winner = check_rows(board)
    if winner is None:
        winner = check_cols(board)
    if winner is None:
        winner = check_diag(board)
    if winner is None:
        completed = check_full(board)

    if winner is None:
        if not completed:
            result = "Draw"
        else:
            result = "Game has not completed"
    else:
        result = winner + " won"
    print "Case #%d: %s" % (caseno, result)
    if caseno != t:
        raw_input()
