#!/bin/python

import sys

inf = sys.stdin
T = int(inf.readline())
    
for t in range(T):
    N, K = map(int, inf.readline().split())
    #print 'N', N, 'K', K
    board = []
    r, b = False, False
    for i in range(N):
        l = inf.readline().strip()
        # shift lines right as we add
        l = l.replace('.', '')
        l = '.' * (N - len(l)) + l
        board.append(l)

    #print '\n'.join(board)
    
    rwin = 'R' * K
    bwin = 'B' * K
        
    # rows
    for i in range(N):
        if board[i].find(rwin) != -1: r = True
        if board[i].find(bwin) != -1: b = True

    # cols, diags
    diag1 = [l[i:] + ('.' * (N-1)) + l[:i] for i, l in enumerate(board)]
    diag2 = [('.' * (i)) + l + ('.' * (N-1-i))  for i, l in enumerate(board)]
    
    #print 'diag1'
    #print '\n'.join(diag1)
    #print 'diag2'
    #print '\n'.join(diag2)
    for i in range(N):
        if not r and ''.join([l[i] for l in board]).find(rwin) != -1: r = True
        if not b and ''.join([l[i] for l in board]).find(bwin) != -1: b = True

    for i in range(2*N-1):
        if not r and ''.join([l[i] for l in diag1]).find(rwin) != -1: r = True
        if not b and ''.join([l[i] for l in diag1]).find(bwin) != -1: b = True
        if not r and ''.join([l[i] for l in diag2]).find(rwin) != -1: r = True
        if not b and ''.join([l[i] for l in diag2]).find(bwin) != -1: b = True
    
    print 'Case #%d: %s' % (t+1, (r and b and 'Both') or (r and 'Red') or (b and 'Blue') or 'Neither')