#!/usr/bin/env pypy3

def blank(y1, x1, y2, x2, board):
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            if board[y][x] != '?':
                return False

    return True

def fill(y1, x1, y2, x2, board, c):
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            board[y][x] = c

def solve(R, C, board):
    chars = set()
    for row in board:
        chars.update(list(row))

    if '?' in chars:
        chars.remove('?')

    region = {}

    for c in chars:
        for y1, row in enumerate(board):
            try:
                x1 = row.index(c)
                break
            except ValueError:
                pass

        for y2, row in reversed(list(enumerate(board))):
            try:
                x2 = C - list(reversed(row)).index(c) - 1
                break
            except ValueError:
                pass

        fill(y1, x1, y2, x2, board, c)

        region[c] = ((y1, x1), (y2, x2))

    for c, ((y1, x1), (y2, x2)) in region.items():
        for top in range(0, y1):
            if blank(top, x1, y1 - 1, x2, board):
                fill(top, x1, y1 - 1, x2, board, c)
                region[c] = ((top, x1), (y2, x2))
                break

    for c, ((y1, x1), (y2, x2)) in region.items():
        for right in range(C - 1, x2, -1):
            if blank(y1, x2 + 1, y2, right, board):
                fill(y1, x2 + 1, y2, right, board, c)
                region[c] = ((y1, x1), (y2, right))
                break

    for c, ((y1, x1), (y2, x2)) in region.items():
        for bottom in range(R - 1, y2, -1):
            if blank(y2 + 1, x1, bottom, x2, board):
                fill(y2 + 1, x1, bottom, x2, board, c)
                region[c] = ((y1, x1), (bottom, x2))
                break

    for c, ((y1, x1), (y2, x2)) in region.items():
        for left in range(0, x1):
            if blank(y1, left, y2, x1 - 1, board):
                fill(y1, left, y2, x1 - 1, board, c)
                region[c] = ((y1, left), (y2, x2))
                break

    return '\n'.join(''.join(row) for row in board)

for i in range(int(input())):
    r, c = [int(x) for x in input().split()]
    board = [list(input()) for _ in range(r)]
    print('Case #{}:\n{}'.format(i + 1, solve(r, c, board)))
