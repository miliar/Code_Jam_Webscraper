import sys
import os
import math
from itertools import product
from copy import deepcopy
from collections import defaultdict

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def can_grow(board, tboard, i, j, sym):
    if board[i][j] not in ['?', sym]:
        return False

    rows = [i for i, r in enumerate(board)  if sym in r] + [i]
    cols = [i for i, r in enumerate(tboard) if sym in r] + [j]

    rows = list(range(min(rows), max(rows) + 1))
    cols = list(range(min(cols), max(cols) + 1))

    for r, c in product(rows, cols):
        if board[r][c] not in [sym, '?']:
            return False
    return True

def fix_rects(brd, tbrd, ss):
    for s in ss:
        rows = [i for i, r in enumerate(brd)  if s in r]
        cols = [i for i, r in enumerate(tbrd) if s in r]

        rows = list(range(min(rows), max(rows) + 1))
        cols = list(range(min(cols), max(cols) + 1))

        # print(s, rows, cols)
        for r, c in product(rows, cols):
            brd[r][c] = s
            tbrd[c][r] = s


def solve(board):
    # print('-----')
    # print_board(board)


    solution = deepcopy(board)
    tboard = list(map(list, zip(*board)))
    syms = sorted(set(sum(board, [])) - set('?'), reverse=True)

    # print(syms)
    for i in range(len(solution)):
        for j in range(len(solution[0])):
            if solution[i][j] == '?':
                # if i == 0 and j == 5:
                # print(syms, [(s, can_grow(solution, tboard, i, j, s)) for s in syms])
                for s in syms:
                    if can_grow(solution, tboard, i, j, s):
                        # print('Growing', i, j, s)
                        solution[i][j] = s
                        tboard[j][i] = s 
                        fix_rects(solution, tboard, syms)
                # print_board_accent(solution, board)
                # print()
                # break

    # print()
    # print_board_accent(solution, board)
    fix_rects(solution, tboard, syms)


    # print()
    return solution

    # print('-----')


def print_board(board):
    for r in board:
        print(''.join(r)) 

def print_board_accent(solution, board):
    def acc(s, b):
        if b == '?':
            return color.YELLOW + s + color.END
        elif b == s:
            return color.BOLD + s + color.END
        elif b == s:
            return color.RED + s + color.END

    for r, rs in zip(board, solution):
        print(''.join(acc(s, b) for (s, b) in zip(rs, r))) 


def line():
    return sys.stdin.readline().strip()

def write_solution(i, ans):
    sys.stdout.write(
        'Case #%s:\n' % (i)
    )
    print_board(ans)

if __name__ == '__main__':
    count = int(line())

    for i in range(count):
        r, c = line().split()
        grid = []
        for j in range(int(r)):
            grid.append(list(line()))
        result = solve(grid)
        write_solution(i + 1, result)
        


