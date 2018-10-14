#!/usr/bin/env python

def get_winner(lines):
    X = ["X","X","X","X"]
    XT = ["T","X","X","X"]
    O = ["O","O","O","O"]
    OT = ["O","O","O","T"]

    for line in lines:
        line.sort()
        if line == X or line == XT: return "X"
        if line == O or line == OT: return "O"

    return None

file = open("input.txt")
num_cases = int(file.readline().strip())

for i in range(num_cases):
    board = file.readline().strip()
    board += file.readline().strip()
    board += file.readline().strip()
    board += file.readline().strip()
    file.readline().strip()

    lines = [list(board[0:4]),
             list(board[4:8]),
             list(board[8:12]),
             list(board[12:]),
             [board[0], board[4], board[8], board[12]],
             [board[1], board[5], board[9], board[13]],
             [board[2], board[6], board[10], board[14]],
             [board[3], board[7], board[11], board[15]],
             [board[0], board[5], board[10], board[15]],
             [board[3], board[6], board[9], board[12]]]

    result = get_winner(lines)
    print("Case #" + str(i+1) + ":", end=" ")
    if result:
        print(result + " won")
    elif "." in board:
        print("Game has not completed")
    else:
        print("Draw")

file.close()
