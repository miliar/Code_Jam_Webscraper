def parseboard(boardstr):
    return boardstr.readlines()
    
def wincombo(letter, board):
    combo = ''
    for i in range(len(board)):
        combo += letter
    return combo
    
def checkrows(letter, board):
    win = False
    for row in board:
        if row.replace('T', letter) == wincombo(letter, board):
            win = True
    return win
    
def checkcols(letter, board):
    win = False
    for i in range(len(board)):
        col = ''
        for row in board:
            col += row[i]
        if col.replace('T', letter) == wincombo(letter, board):
            win = True
    return win
    
def checkdiags(letter, board):
    win = False
    diag0 = ''
    diag1 = ''
    for i in range(len(board)):
        diag0 += board[i][i]
        diag1 += board[len(board) - i - 1][i]
    diags = [diag0, diag1]
    for diag in diags:
        if diag.replace('T', letter) == wincombo(letter, board):
            win = True
    return win
    
def checkwin(letter, board):
    return checkrows(letter, board) or checkcols(letter, board) \
        or checkdiags(letter, board)
    
def findresult(board):
    if checkwin('X', board):
        return 'X won'
    elif checkwin('O', board):
        return 'O won'
    else:
        existsdot = False
        for row in board:
            if '.' in row:
                existsdot = True
        if existsdot:
            return 'Game has not completed'
        else:
            return 'Draw'
            
def processfile(filename, out):
    lines = open(filename, 'r').read().replace('\n\n', '\n') \
        .split('\n')[1:]
    result = ''
    for i in range(len(lines) / 4):
        result += 'Case #' + str(i+1) + ': ' + findresult(lines[4*i:4*i+4]) \
            + '\n'
    open(out, 'w').write(result[:-1])
         
processfile('A-small-attempt0.in', 'tictac.out')
processfile('A-large.in', 'tictac-large.out')