filein = open('A-large.in', mode='r')
fileout = open('A-large.out', mode='w')
T = filein.readline()

for case in range(1, int(T)+1):
    board = list((filein.readline().strip(),filein.readline().strip(),filein.readline().strip(),filein.readline().strip()))
    won = '' #d draw, O for O, X for X and '' if not decided yet.

    #Check horizontal
    if won != 'd':
        for i in range(0, 4):
            if board[i] == 'XXXX' or board[i] == 'XXXT' or board[i] == 'XXTX' or board[i] == 'XTXX' or board[i] == 'TXXX':
                if won == 'O':
                    won = 'd'
                else:
                    won = 'X'
            if board[i] == 'OOOO' or board[i] == 'OOOT' or board[i] == 'OOTO' or board[i] == 'OTOO' or board[i] == 'TOOO':
                if won == 'X':
                    won = 'd'
                else:
                    won = 'O'
            
    #check vertical
    if won != 'd':
        for i in range(0, 4):
            boardv = str(board[0][i]) + str(board[1][i]) + str(board[2][i]) + str(board[3][i])
            if boardv == 'XXXX' or boardv == 'XXXT' or boardv == 'XXTX' or boardv == 'XTXX' or boardv == 'TXXX':
                if won == 'O':
                    won = 'd'
                else:
                    won = 'X'
            if boardv == 'OOOO' or boardv == 'OOOT' or boardv == 'OOTO' or boardv == 'OTOO' or boardv == 'TOOO':
                if won == 'X':
                    won = 'd'
                else:
                    won = 'O'
                    
    #check diagnol
    if won != 'd':
        boardd1 = str(board[0][0]) + str(board[1][1]) + str(board[2][2]) + str(board[3][3])
        if boardd1 == 'XXXX' or boardd1 == 'XXXT' or boardd1 == 'XXTX' or boardd1 == 'XTXX' or boardd1 == 'TXXX':
            if won == 'O':
                 won = 'd'
            else:
                won = 'X'
        if boardd1 == 'OOOO' or boardd1 == 'OOOT' or boardd1 == 'OOTO' or boardd1 == 'OTOO' or boardd1 == 'TOOO':
            if won == 'X':
                won = 'd'
            else:
                won = 'O'
    if won != 'd':              
        boardd2 = str(board[0][3]) + str(board[1][2]) + str(board[2][1]) + str(board[3][0])
        if boardd2 == 'XXXX' or boardd2 == 'XXXT' or boardd2 == 'XXTX' or boardd2 == 'XTXX' or boardd2 == 'TXXX':
            if won == 'O':
                won = 'd'
            else:
                won = 'X'
        if boardd2 == 'OOOO' or boardd2 == 'OOOT' or boardd2 == 'OOTO' or boardd2 == 'OTOO' or boardd2 == 'TOOO':
            if won == 'X':
                won = 'd'
            else:
                won = 'O'
                
    result = "Case #" + str(case) + ": "
    if won == 'X':
        result = result + won + " won\n"
    elif won == "O":
        result = result + won + " won\n"
    elif won == 'd':
        result = result + "Draw\n"
    else:
        if "." in board[0] or "." in board[1] or "." in board[2] or "." in board[3]:
            result = result + "Game has not completed\n"
        else:
            result = result + "Draw\n"
    fileout.write(result)
    filein.readline()
filein.close()
fileout.close()
