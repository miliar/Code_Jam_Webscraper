
filename = 'A-large.in'
noWin = 'N'
def main():
    with open(filename) as f:
        lines = f.readlines()
    outFile =  open('out_' + filename, 'w')

    nCases = int(lines[0])
    for i in range(nCases):
        board = []
        for l in lines[i*4 + 1 + 1*i:i*4 + 4 + 1 + 1*i]: # 1*i skips empty lines. +1 skips first line
            board.append( tuple(l[:-1]) ) # ignore newline
        (winner, gameOver) = SolveTomek(board)

        
        outText = 'Case #' + str((i+1)) + ': '
        if winner == noWin:
            if not gameOver:
                outText += 'Game has not completed'
            else:
                outText += 'Draw'
        else:
            outText += winner
            outText += ' won'
        outFile.write( outText + '\n')
            

def SolveTomek(board):
    res = []
    for rInd in range(4):
        if rInd == 0: # 1st row is special case. Afterwards only need to check row wins.
            res.append( checkRow( (board[0][0],board[1][1],board[2][2],board[3][3]) ) )
            res.append( checkRow( (board[0][3],board[1][2],board[2][1],board[3][0]) ) )
            for cInd in range(4):
                res.append( checkRow( (board[0][cInd], board[1][cInd], board[2][cInd], board[3][cInd]) ) )
        res.append( checkRow(board[rInd]) )

    for winner in res:
        if winner == 'X':
            return ('X', True)
        if winner =='O':
            return ('O', True)

    gameOver = not any([True for i in range(4) for j in range(4) if board[i][j] == '.'])
    return (noWin, gameOver)

def checkRow(row):
    setRow = set(row)
    setLen = len(setRow)
    
    if setLen <= 2:
        if setLen <= 1:
            return row[0]
        e1 = setRow.pop()
        e2 = setRow.pop()
        if e1 == 'T':
            return e2
        if e2 == 'T':
            return e1
        
    return noWin

main()
