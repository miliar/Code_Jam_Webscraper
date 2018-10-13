fin = open("A-large.in", "r")
fout = open("largeA.out", "w")


def next():
    return fin.readline().strip()
    
# 00 01 02 03
# 04 05 06 07
# 08 09 10 11
# 12 13 14 15
    
    
wins = [
    [0,1,2,3],
    [4,5,6,7],
    [8,9,10,11],
    [12,13,14,15],
    
    [0,4,8,12],
    [1,5,9,13],
    [2,6,10,14],
    [3,7,11,15],
    
    [0,5,10,15],
    [3,6,9,12]
    ]
    
    
def winner(board):
    for i in wins:
        row = board[i[0]] + board[i[1]] + board[i[2]] + board[i[3]]
        if "." not in row:
            if "X" not in row:
                #O wins
                return "O won"
            if "O" not in row:
                #X wins
                return "X won"
                
    if "." not in board: #no winner
        return "Draw"
                
    return "Game has not completed"
                
    
for case in xrange(1, int(next()) + 1):
    board = next() + next() + next() + next()
    
    fout.write("Case #" + str(case) + ": ")
    fout.write(winner(board))
    fout.write("\n")
    
    
    next() #empty line
        
fout.close()