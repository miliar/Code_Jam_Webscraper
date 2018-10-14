#!/usr/bin/python3

import sys

def read():
    return tuple(sys.stdin.readline().split())

def readint():
    return tuple(map(int, read()))

def calc(s, D, i, j, p):
    return (D + ord(s[i][j]) - ord('0'))*p

T, = readint()
for case in range(1, T+1):
    R, C, D = readint()
    s = [read()[0] for i in range(R)]
    x = [[0 for j in range(C)] for i in range(R)]
    y = [[0 for j in range(C)] for i in range(R)]
    w = [[0 for j in range(C)] for i in range(R)]
    for i in range(R):
        for j in range(C):
            x[i][j] = calc(s, D, i, j, i) 
            if i > 0: x[i][j] += x[i-1][j]
            if j > 0: x[i][j] += x[i][j-1]
            if i > 0 and j > 0: x[i][j] -= x[i-1][j-1]

            y[i][j] = calc(s, D, i, j, j) 
            if i > 0: y[i][j] += y[i-1][j]
            if j > 0: y[i][j] += y[i][j-1]
            if i > 0 and j > 0: y[i][j] -= y[i-1][j-1]

            w[i][j] = calc(s, D, i, j, 1)
            if i > 0: w[i][j] += w[i-1][j]
            if j > 0: w[i][j] += w[i][j-1]
            if i > 0 and j > 0: w[i][j] -= w[i-1][j-1]

    def print_a(a):
        for i in range(R): print(a[i])
        print()
    ret = 'IMPOSSIBLE'
    for k in range(3, min(R, C)+1):
        for i in range(R-k+1):
            for j in range(C-k+1):
                tx = x[i+k-1][j+k-1]
                if i > 0: tx -= x[i-1][j+k-1]
                if j > 0: tx -= x[i+k-1][j-1]
                if i > 0 and j > 0: tx += x[i-1][j-1]
                tx -= calc(s, D, i, j, i)
                tx -= calc(s, D, i+k-1, j, i+k-1)
                tx -= calc(s, D, i, j+k-1, i)
                tx -= calc(s, D, i+k-1, j+k-1, i+k-1)

                ty = y[i+k-1][j+k-1]
                if i > 0: ty -= y[i-1][j+k-1]
                if j > 0: ty -= y[i+k-1][j-1]
                if i > 0 and j > 0: ty += y[i-1][j-1]
                ty -= calc(s, D, i, j, j)
                ty -= calc(s, D, i+k-1, j, j)
                ty -= calc(s, D, i, j+k-1, j+k-1)
                ty -= calc(s, D, i+k-1, j+k-1, j+k-1)

                tw = w[i+k-1][j+k-1]
                if i > 0: tw -= w[i-1][j+k-1]
                if j > 0: tw -= w[i+k-1][j-1]
                if i > 0 and j > 0: tw += w[i-1][j-1]
                tw -= calc(s, D, i, j, 1)
                tw -= calc(s, D, i+k-1, j, 1)
                tw -= calc(s, D, i, j+k-1, 1)
                tw -= calc(s, D, i+k-1, j+k-1, 1)

                if tx*2 == tw*(i*2+k-1) and ty*2 == tw*(j*2+k-1):
                    ret = k
                    break
            if j < C-k: break
    print('Case #{}: {}'.format(case, ret))
