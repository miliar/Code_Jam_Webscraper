#Code Jam 2013 - QR - PA
#Ben Fishbein
#4/13
#Tic-Tac-Toe-Tomek
#Find if someone has won a game of Tic-Tac-Toe-Tomek
#https://code.google.com/codejam/contest/2270488/dashboard

#into = open('CJ2013QRPA1.in')
#out = open('CJ2013QRPA1.out', 'w')
into = open('CJ2013QRPA2.in')
out = open('CJ2013QRPA2.out', 'w')

lines = []
lines = into.readlines()

for x in range(int(lines[0])):
    currentBoard = []
    for y in range(4):
        if (y == 3 and x == int(lines[0])-1):
            currentBoard.append(lines[x*4+y+1+x])
        else:
            currentBoard.append(lines[x*4+y+1+x][:-1])
    #print currentBoard
    currentPiece = "p"
    winner5 = "Draw"
    xWin = 1
    oWin = 1
    winner = 0
    
    for i in range(4):
        if (winner == 0):
            for j in range(4):
                if (currentBoard[i][j] == "."):
                    winner5 = "Game has not completed"
                if (currentBoard[i][j] != "X" and currentBoard[i][j] != "T"):
                    xWin = 0
                if (currentBoard[i][j] != "O" and currentBoard[i][j] != "T"):
                    oWin = 0
            if (xWin == 1):
                winner = 1
            if (oWin == 1):
                winner = 2
            xWin = 1
            oWin = 1

    for j in range(4):
        if (winner == 0):
            for i in range(4):
                if (currentBoard[i][j] == "."):
                    winner5 = "Game has not completed"
                if (currentBoard[i][j] != "X" and currentBoard[i][j] != "T"):
                    xWin = 0
                if (currentBoard[i][j] != "O" and currentBoard[i][j] != "T"):
                    oWin = 0
            if (xWin == 1):
                winner = 1
            if (oWin == 1):
                winner = 2
            xWin = 1
            oWin = 1
            
    for j in range(4):
        if (winner == 0):
            for j in range(4):
                if (currentBoard[j][j] == "."):
                    winner5 = "Game has not completed"
                if (currentBoard[j][j] != "X" and currentBoard[j][j] != "T"):
                    xWin = 0
                if (currentBoard[j][j] != "O" and currentBoard[j][j] != "T"):
                    oWin = 0
            if (xWin == 1):
                winner = 1
            if (oWin == 1):
                winner = 2
            xWin = 1
            oWin = 1

    for j in range(4):
        if (winner == 0):
            for j in range(4):
                if (currentBoard[3-j][j] == "."):
                    winner5 = "Game has not completed"
                if (currentBoard[3-j][j] != "X" and currentBoard[3-j][j] != "T"):
                    xWin = 0
                if (currentBoard[3-j][j] != "O" and currentBoard[3-j][j] != "T"):
                    oWin = 0
            if (xWin == 1):
                winner = 1
            if (oWin == 1):
                winner = 2
            xWin = 1
            oWin = 1
    

    if (winner == 1):
        out.write("Case #" + str(x + 1) + ": " + "X won\n")
    elif (winner == 2):
        out.write("Case #" + str(x + 1) + ": " + "O won\n")
    else:
        out.write("Case #" + str(x + 1) + ": " + winner5 + "\n")
out.close()
        
