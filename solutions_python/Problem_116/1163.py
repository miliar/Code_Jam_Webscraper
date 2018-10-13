#!/usr/bin/env python3

from functools import reduce
from itertools import chain

X, O, T, D = 'XOT.'

def read():
    n = int(input())
    for i in range(n):
        grid = [input().strip() for j in range(4)]
        input()  # Blank line
        yield grid

def combine(a, b):
    if a == b:
        return a
    elif a == T:
        return b
    elif b == T:
        return a
    else:
        return '.'

def everything(grid):

    def rows(grid):
        return iter(grid)

    def cols(grid):
        return zip(*grid)

    def diag(grid):
        yield [grid[j][i] for j, i in zip(range(4), range(4))]
        yield [grid[j][i] for j, i in zip(range(4), range(3, -1, -1))]

    return chain(rows(grid), cols(grid), diag(grid))

def judge(grid):
    winner = D
    for row in everything(grid):
        result = reduce(combine, row)
        if result in (X, O):
            winner = result
            break
    return winner

def board_full(grid):
    return all(x != '.' for x in chain(*grid))

if __name__ == '__main__':
    for i, grid in enumerate(read(), 1):
        result = judge(grid)
        print('Case #{0}: '.format(i), end='')
        if result in (X, O):
            print(result, 'won')
        elif board_full(grid):
            print('Draw')
        else:
            print('Game has not completed')
