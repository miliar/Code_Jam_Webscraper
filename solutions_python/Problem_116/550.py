'''
Created on April 13, 2013

@author: Anand
'''

import sys

sys.stdin = open('../ATicTacToeTomek.in')
sys.stdout = open('../ATicTacToeTomek.out', 'w')

def main():
    T = int(raw_input())
    for testcase in xrange(1, T + 1):
        grid = []
        for i in range(4):
            grid.append([c for c in raw_input()])
        raw_input()

        if winner(grid, 'X'):
            answer = 'X won'
        elif winner(grid, 'O'):
            answer = 'O won'
        elif any(('.' in row) for row in grid):
            answer = 'Game has not completed'
        else:
            answer = 'Draw'

        print "Case #%d: %s" % (testcase, answer)


def winner(original_grid, x):
    grid = [[' ' for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            grid[i][j] = original_grid[i][j]
            if grid[i][j] == 'T':
                grid[i][j] = x
    if any(sum(1 for c in row if c == x) == 4 for row in grid):
        return True
    for i in range(4):
        for j in range(4):
            grid[i][j] = original_grid[j][i]
            if grid[i][j] == 'T':
                grid[i][j] = x
    if any(sum(1 for c in row if c == x) == 4 for row in grid):
        return True
    grid = [[' ' for i in range(4)] for j in range(2)]
    for j in range(4):
        grid[0][j] = original_grid[j][j]
    for j in range(4):
        grid[1][j] = original_grid[j][3 - j]
    for i in range(2):
        for j in range(4):
            if grid[i][j] == 'T':
                grid[i][j] = x
    if any(sum(1 for c in row if c == x) == 4 for row in grid):
            return True


main()
