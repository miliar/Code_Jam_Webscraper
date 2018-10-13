import sys
import re
from math import *
from cmath import *


T = int(sys.stdin.readline())

for Case in range(T):
    ss = [int(s) for s in sys.stdin.readline()[:-1].split()]
    R = ss[0]
    C = ss[1]
    D = ss[2]
    board = []
    for r in range(R):
        board.append([int(s) for s in sys.stdin.readline()[:-1]])
    K = 0
    for k in range(3, min(R, C) + 1):
        for sr in range(R):
            for sc in range(C):
                if sr + k > R or sc + k > C:
                    continue
                wh = 0
                wv = 0
                for r in range(sr, sr + k):
                    for c in range(sc, sc + k):
                        if (r == sr or r == sr + k - 1) and (c == sc or c == sc + k - 1): continue
                        if k % 2 == 1:
                            dr = r - (sr + k // 2)
                            dc = c - (sc + k // 2)
                        else:
                            if r < sr + k // 2:
                                dr = (r - sr) - k // 2
                            else:
                                dr = (r - sr) - k // 2 + 1
                            if c < sc + k // 2:
                                dc = (c - sc) - k // 2
                            else:
                                dc = (c - sc) - k // 2 + 1
                        wv += dr * (board[r][c])
                        wh += dc * (board[r][c])
#                        print('wh += {0} * {1}'.format(dc, board[r][c]))
#                    print('wh[{0}] = {1}'.format(r - sr, wh))
                if wh == 0 and wv == 0:
                    K = k
#                print('wh = {0}, wv = {1}'.format(wh, wv))
    print('Case #{0}: {1}'.format(Case + 1, K if K > 0 else 'IMPOSSIBLE'))

