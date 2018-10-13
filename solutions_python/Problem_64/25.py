#!/usr/bin/env python

from collections import defaultdict
import numpy as np

import sys

def update_ps(M, N, ps, board):
    for x in xrange(M - 2, -1, -1):
        for y in xrange(N - 2, -1, -1):
            if board[x, y] < 0:
                ps[x, y] = 0
            elif min(ps[x + 1, y], ps[x, y + 1], ps[x + 1, y + 1]) == 0:
                ps[x, y] = 1
            elif (board[x, y] != board[x + 1, y]
                    and board[x, y] == board[x + 1, y + 1]
                    and board[x, y] != board[x, y + 1]):
                ps[x, y] = min(ps[x + 1, y], ps[x, y + 1], ps[x + 1, y + 1]) + 1

T = int(sys.stdin.readline())

for i in xrange(1, T + 1):
    M, N = [int(x) for x in sys.stdin.readline().split()]
    board = np.zeros((M, N), dtype=np.int8)
    for j in xrange(M):
        line = sys.stdin.readline().strip()
        for k, c in enumerate(line):
            v = int(c, 16)
            board[j, 4 * k    ] = int(bool(v & 8))
            board[j, 4 * k + 1] = int(bool(v & 4))
            board[j, 4 * k + 2] = int(bool(v & 2))
            board[j, 4 * k + 3] = int(bool(v & 1))
    ps = np.ones((M, N), dtype=np.int8)
    results = defaultdict(int)
    while True:
        update_ps(M, N, ps, board)
        idx = np.unravel_index(np.argmax(ps), ps.shape)
        v = ps[idx]
        if v == 1:
            results[1] = len(np.argwhere(board >= 0))
            if not results[1]:
                del results[1]
            break
        results[v] += 1
        board[idx[0]:idx[0] + v, idx[1]:idx[1] + v] = -1

    result = 0

    print 'Case #%i: %s' % (i, len(results))
    for k, v in reversed(results.items()):
        print k, v
