#!/usr/bin/env python3

def check(board):
    available = 0
    for r in range(4):
        count = 0
        possibles = 3
        for c in range(4):
            if board[r][c] == 'O': possibles &= ~1
            if board[r][c] == 'X': possibles &= ~2
            if board[r][c] != '.': count += 1

            if board[r][c] == '.': available += 1

        if(count == 4 and possibles == 1): return 'X'
        if(count == 4 and possibles == 2): return 'O'

    for c in range(4):
        count = 0
        possibles = 3
        for r in range(4):
            if board[r][c] == 'O': possibles &= ~1
            if board[r][c] == 'X': possibles &= ~2
            if board[r][c] != '.': count += 1

        if(count == 4 and possibles == 1): return 'X'
        if(count == 4 and possibles == 2): return 'O'

    count = 0
    possibles = 3
    for i in range(4):
        if board[i][i] == 'O': possibles &= ~1
        if board[i][i] == 'X': possibles &= ~2
        if board[i][i] != '.': count += 1
    if(count == 4 and possibles == 1): return 'X'
    if(count == 4 and possibles == 2): return 'O'

    count = 0
    possibles = 3
    for i in range(4):
        if board[3-i][i] == 'O': possibles &= ~1
        if board[3-i][i] == 'X': possibles &= ~2
        if board[3-i][i] != '.': count += 1
    if(count == 4 and possibles == 1): return 'X'
    if(count == 4 and possibles == 2): return 'O'
        
    return available != 0

T = int(input())

for t in range(T):
    board = [input(), input(), input(), input()]
    try:
        input()
    except: pass
    r = check(board)

    if(r == 'O'): print("Case #" + str(t+1) + ": O won")
    if(r == 'X'): print("Case #" + str(t+1) + ": X won")
    if(r == True): print("Case #" + str(t+1) + ": Game has not completed")
    if(r == False): print("Case #" + str(t+1) + ": Draw")
