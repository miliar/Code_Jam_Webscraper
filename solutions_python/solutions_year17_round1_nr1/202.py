import math, collections, copy, sys
f = open('input.in','r')
g = open('output.txt','w')
"""
just find a way to fill the board.
"""
for index in xrange(1, int(f.readline()[:-1]) + 1):
    R, C = [int(x) for x in f.readline()[:-1].split(' ')]
    board = [0]*R
    for i in xrange(R):
        board[i] = list(f.readline()[:-1])
    i = j = 0
    while i < R and j < C:
        if board[i][j] == '?':
            j += 1
            if j == C:
                j = 0
                i += 1
        else:
            initial = board[i][j]
            start_i = i-1
            while start_i >= 0 and board[start_i][j] == '?':
                start_i -= 1
            start_j = j-1
            while start_j >= 0 and board[i][start_j] == '?':
                start_j -= 1
            end_j = j+1
            while end_j <= C-1 and board[i][end_j] == '?':
                end_j += 1
            for r in xrange(start_i+1, i+1):
                for c in xrange(start_j+1, end_j):
                    board[r][c] = initial
            j = end_j
            if j == C:
                j = 0
                i += 1
    if board[R-1][0] == '?':
        start_i = R-1
        while board[start_i][0] == '?':
            start_i -= 1
        for r in xrange(start_i+1, R):
            for c in xrange(C):
                board[r][c] = board[start_i][c]
    for i in xrange(R):
        board[i] = ''.join(board[i])
    result = '\n' + '\n'.join(board)
    g.write("Case #{}:{}\n".format(index, result))
    print "Case #{}:{}\n".format(index, result)
f.close()
g.close()