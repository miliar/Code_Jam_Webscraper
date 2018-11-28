import os

def analyse(board, case):
    stringStart = str('Case #' + str(case) + ': ')
    for row in board:
        while row.count('\n')>0:
            row.remove('\n')
    if 'won' in winhori(board):
        return(stringStart+ winhori(board))
    elif 'won' in winvert(board):
        return(stringStart+ winvert(board))
    elif 'won' in windiag(board):
        return(stringStart+ windiag(board))
    elif draw(board):
        return(stringStart + 'Draw')
    else:
        return(stringStart + 'Game has not completed')
        
def draw(board):
    result = True
    for row in board:
        if '.' in row:
            result = False
    return (result)
        
def windiag(board):
    diag1 = []
    diag2 = []
    for i in range (4):
        diag1.append(board[i][i])
        diag2.append(board[i][3-i])
    newboard = [diag1, diag2]
    return winhori(newboard)

def winvert(board):
    newboard = [['.','.','.','.'],['.','.','.','.'],['.','.','.','.'],['.','.','.','.']]
    for i in range (4):
        for j in range (4):
            newboard[i][j] = board[j][i]
    return winhori(newboard)

def winhori(board):
    result = 'no'
    for row in board:
        if 'T' in row:
            if row.count('X')== 3:
                result = "X won"
            if row.count('O')== 3:
                result = "O won"
        else:
            if row.count('X')== 4:
                result = "X won"
            if row.count('O')== 4:
                result = "O won"
    return (result)

filein = open ('A-large.in', 'r') 
outfile = open ('sample.out', 'wt')
instances = int(filein.readline())

for i in range (instances):
    board = []
    for j in range(4):
        board.append(list(filein.readline()))
    filein.readline()
    outfile.write(analyse(board,i+1))
    outfile.write('\n')
filein.close()
outfile.close()
