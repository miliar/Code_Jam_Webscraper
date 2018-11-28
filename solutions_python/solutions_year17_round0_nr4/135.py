#!/usr/bin/env python3

def solve(N, board):
    '''This only works for the small test case, i.e.
    if only the first row may be filled.'''
    cycle = ([i for i, c in enumerate(board[0]) if c in 'ox']+[0])[0]
    added = [('o' if i == cycle else '+', 0, i)
             for i, c in enumerate(board[0])
             if c not in "o+" or i == cycle and c == '+'] + \
            [('x', i+1, i + (i >= cycle) if cycle < N-1 else N-2-i)
             for i in range(N-1)] + \
            [('+', N-1, i+1) for i in range(N-2)]
    return 3*N-2 + (N == 1), added

tests = int(input())
for test in range(tests):
    N, M = map(int, input().split())
    board = [['.' for i in range(N)] for j in range(N)]
    for i in range(M):
        c, *s = input().split()
        i, j = map(int, s)
        board[i-1][j-1] = c
    score, added = solve(N, board)
    print("Case #{}: {} {}".format(1+test, score, len(added)))
    for c, i, j in added: print("{} {} {}".format(c, i+1, j+1))
