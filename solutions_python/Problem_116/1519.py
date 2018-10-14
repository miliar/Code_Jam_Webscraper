#!/usr/bin/python

nCases=int(raw_input())

testCase=1

def getCol(g,j):
    i=0
    col = ""
    while i<4:
        col = col + g[i][j]
        i = i+1
    return col

def checkWinner(x):
    if x=="OOOO" or x=="TOOO" or x=="OTOO" or x=="OOTO" or x=="OOOT":
        return "O won"
    if x=="XXXX" or x=="TXXX" or x=="XTXX" or x=="XXTX" or x=="XXXT":
        return "X won"
    return "none"

def winner(game,gameCol,diag1,diag2):
    i = 0
    board = ""
    while i<4:
        board = board + game[i]
        winner = checkWinner (game[i])
        if winner != 'none':
            return winner

        winner = checkWinner (gameCol[i])
        if winner != 'none':
            return winner
        i = i+1

    winner = checkWinner(diag1)
    if winner != 'none':
        return winner

    winner = checkWinner(diag2)
    if winner != 'none':
        return winner

    if '.' in board :
        return "Game has not completed"
    return "Draw"



while (testCase <= nCases):
    
    game=[]
    
# First get the input     
    i=0
    while i<4 :
        row=raw_input()
        game=game+[row]
        i = i+1

    gameCol = []
    i = 0
    while i < 4:
        gameCol = gameCol+ [getCol(game,i)]
        i = i+1

    diag1 = game[0][0] + game[1][1] + game[2][2] + game[3][3]
    diag2 = game[0][3] + game[1][2] + game[2][1] + game[3][0]
    
    print "Case #"+str(testCase)+": "+winner(game,gameCol,diag1,diag2)
#    print game

    raw_input()
    testCase = testCase+1


