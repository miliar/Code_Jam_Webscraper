#!/usr/bin/env python

import fileinput

result = {
    False: { False: "Neither", True: "Blue" },
    True:  { False: "Red",     True: "Both" } }

def main():
    reader = fileinput.input()
    t = int(reader.next())
    for i in range(1, t+1):
        n, k = reader.next().strip().split()
        n = int(n)
        k = int(k)
        result = joink(reader, k, n)
        print 'Case #%d: %s' % (i, result)

def joink(reader, k, n):
    board = []
    for i in range(n):
        board.append(reader.next().strip())

    b2 = rotate(board)
    gravity(b2)

    r = find(b2, k, 'R')
    b = find(b2, k, 'B')
    return result[r][b]

def rotate(board):
    n = len(board)
    b2 = [None] * n
    for r in range(n):
        b2[r] = [None] * n
        for c in range(n):
            b2[r][c] = board[n-c-1][r]
    return b2

def gravity(board):
    n = len(board)
    for c in range(n):
        r0 = n - 1
        r1 = n - 1
        while 0 <= r0:
            if board[r0][c] == '.':
                r0 -= 1
            else:
                board[r1][c] = board[r0][c]
                r0 -= 1
                r1 -= 1
        while 0 <= r1:
            board[r1][c] = '.'
            r1 -= 1

def dump(board):
    print
    for r in range(len(board)):
        print ''.join(board[r])

def find(board, k, ch):
    n = len(board)
    for r in range(n):
        for c in range(n):
            if (chase(board, r, c, k, ch, 0, 1) or
                chase(board, r, c, k, ch, 1, 0) or
                chase(board, r, c, k, ch, 1, 1) or
                chase(board, r, c, k, ch, -1, 1)):
                return True
    return False

def chase(board, r, c, k, ch, dr, dc):
    n = len(board)
    for i in range(k):
        r1 = r + dr*i
        c1 = c + dc*i
        if r1 < 0 or c1 < 0 or n <= r1 or n <= c1 or board[r1][c1] != ch:
            return False
    return True

main()
