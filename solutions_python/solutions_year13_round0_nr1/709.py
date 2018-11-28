# tic-tac-toe-tomek
# https://code.google.com/codejam/contest/2270488/dashboard

import sys
sys.stdout = open('a.out', 'w')
sys.stdin = open('a.in', 'r')

t = int(input())

for i in range(1, t + 1):
    board = []
    left_diag = []
    right_diag = []
    col = [[], [], [], []]
    for j in range(4):
        line = list(input())
        board.append(line)
        left_diag.append(line[j])
        right_diag.append(line[3 - j])
        for l in range(4):
            col[l].append(line[l])
    board.append(left_diag)
    board.append(right_diag)
    board.extend(col)
    #print(board)

    won = False
    has_empty_cell = False
    for k in range(10):
        line = board[k]
        if '.' in line:
            has_empty_cell = True
        else:
            if 'X' in line and 'O' not in line:
                print('Case #%d: X won' % i)
                won = True
                break
            elif 'O' in line and 'X' not in line:
                print('Case #%d: O won' % i)
                won = True
                break
    if not won:
        if not has_empty_cell:
            print('Case #%d: Draw' % i)
        else:
            print('Case #%d: Game has not completed' % i)
    input()
