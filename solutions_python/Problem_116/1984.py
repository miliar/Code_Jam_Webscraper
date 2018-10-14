#!/usr/bin/env python3 

def check(board,ti,tj,side):
    if(ti != -1):
        board[ti][tj] = side
#        print(board)

    for row in range(4):
        if board[row].count(side) == 4:
            return True;

    for col in range(4):
        if [board[i][col] for i in range(4)].count(side) == 4:
            return True;
    
    if [board[i][i] for i in range(4)].count(side) == 4:
        return True

    if [board[i][3-i] for i in range(4)].count(side) == 4:
        return True


    if(ti != -1):
        board[ti][tj] = 'T'

    return False

def solve(board):
    any_dot = False
    ti = -1
    tj = -1
    for i in range(4):
        for j in range(4):
            if board[i][j] == '.':
                any_dot = True
            if board[i][j] == 'T':
                ti = i
                tj = j
    

    if (check(board,ti,tj,'X')):
        return "X won"
    elif(check(board,ti,tj,'O')):
        return "O won"
    elif any_dot:
        return "Game has not completed"
    else:
        return "Draw"
         
if __name__ == "__main__":
    T = int(input())
    for c in range(T):
        board = []
        for i in range(4):
            I = input().strip()
            board.append([c for c in I])
        if c != T-1:
            input()
#        print(board)
        o = solve(board)
        print( ("Case #%d: " % (c+1)) + o )

        
