#!/usr/bin/env python3

T = int(input())

def winner(s):
    for t in s:
        if '.' in t:
            continue
        if 'X' in t and 'O' in t:
            continue
        return True, 'X' if 'X' in t else 'O'
    return False, '.'

def won(board):
    t = []
    for i in range(4):
        t.append(set(board[i][j] for j in range(4)))
        t.append(set(board[j][i] for j in range(4)))

    t.append(set(board[i][i] for i in range(4)))
    t.append(set(board[i][3-i] for i in range(4)))

    return winner(t)

def is_full(board):
    return '.' not in set(board[i][j] for i in range(4) for j in range(4))

for case in range(1,T+1):
    board = [input()[:4] for i in range(4)]
    input()

    W, w = won(board)

    ans = ""
    if W:
        ans = "{} won".format(w)
    elif is_full(board):
        ans = "Draw"
    else:
        ans = "Game has not completed"

    print("Case #{}: {}".format(case, ans))

