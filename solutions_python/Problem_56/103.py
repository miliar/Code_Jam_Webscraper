#!python3

from pprint import pprint
from itertools import zip_longest

def diagonals(b, anti=False):
    if anti:
        shifted = list(r[:] for r in list(reversed(b)))
    else:
        shifted = list(r[:] for r in b)
    for i, row in enumerate(shifted):
        row[0:0] = i * [None]
    for col in zip_longest(*shifted):
        yield list(x for x in col if x)

def winner(board, n, k):
    # make gravity act towards the left
    # by removing all dots
    rotated_board = [list(''.join(row).replace('.', '')) for row in board]

    # remove empty rows
    rotated_board = list(filter(None, rotated_board))

    # pad with dots
    try:
        l = max(len(row) for row in rotated_board)
    except:
        l = 0
    for row in rotated_board:
        row[0:0] = ['.'] * (l - len(row))

    blue_wins = False
    red_wins = False

    # create lists of rows, cols and both diagonals
    # as strings
    rows = [''.join(row) for row in rotated_board]
    cols = [''.join(col) for col in zip(*rotated_board)]
    diags = [''.join(d) for d in diagonals(rotated_board)]
    antidiags = [''.join(d) for d in diagonals(rotated_board, anti=True)]

    #print()
    #pprint(rows, width=10)
    #pprint(cols, width=10)
    #pprint(diags, width=10)
    #pprint(antidiags, width=10)

    for l in [rows, cols, diags, antidiags]:
        red_wins  = red_wins  or any('R' * K in s for s in l)
        blue_wins = blue_wins or any('B' * K in s for s in l)

    if blue_wins and red_wins:
        return 'Both'
    elif blue_wins:
        return 'Blue'
    elif red_wins:
        return 'Red'
    else:
        return 'Neither'

T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    board = [list(input()) for i in range(N)]
    print('Case #{}: {}'.format(t, winner(board, N, K)))

