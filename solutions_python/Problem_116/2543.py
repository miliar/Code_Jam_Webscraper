def p1(inName, outName):
    inFile = open(inName, "r")
    outFile = open(outName, "w")
    T = int(inFile.readline())
    for t in range(T):
        board = []
        for _ in range(4):
            l = inFile.readline()
            lBoard = []
            for i in range(4):
                lBoard.append(l[i])
            board.append(lBoard)
        checkBoard(board, outFile, t)    
        inFile.readline()

def checkBoard(board, outFile, t):
    hasDot = False
    # Check diagonal
    diag1 = []
    diag2 = []
    for i in range(4):
        diag1.append(board[i][i])
        diag2.append(board[i][3-i])
    print diag2
    final, hasDot = checkLine(diag1, outFile, t)
    if final:
        outFile.write("\n")
        return
    final, hasDot = checkLine(diag2, outFile, t)
    if final:
        outFile.write("\n")
        return
       
    # Check rows
    for i in range(4):
        final, hasDot = checkLine(board[i], outFile, t)
        if final:
            outFile.write("\n")
            return
        
    # Check columns
    board = zip(board[0], board[1], board[2], board[3])
    for i in range(4):
        final, hasDot = checkLine(board[i], outFile, t)
        if final:
            outFile.write("\n")
            return
        
    if hasDot == True:
        outFile.write("Case #" + str(t+1) + ": " + "Game has not completed")
    else:
        outFile.write("Case #" + str(t+1) + ": " + "Draw")
    outFile.write("\n")
        
def checkLine(l, outFile, t):
    countX = len(filter(lambda x: x == 'X', l))
    countO = len(filter(lambda x: x == 'O', l))
    countT = len(filter(lambda x: x == 'T', l))
    countDot = len(filter(lambda x: x == '.', l))
    if countX + countT == 4:
        outFile.write("Case #" + str(t+1) + ": " + "X won")
        return True, False
    if countO + countT == 4:
        outFile.write("Case #" + str(t+1) + ": " + "O won")
        return True, False
    if countDot > 0:
        return False, True
    return False, False
    
p1('A-small-attempt0.in', 'A-small-attempt0.out')
                 
            
    