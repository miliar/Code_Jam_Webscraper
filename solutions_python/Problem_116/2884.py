def isWin(board, player):
    for i in range(4):
        if (board[i][0]==player or board[i][0]=='T') and (board[i][1]==player or board[i][1]=='T') and (board[i][2]==player or board[i][2]== 'T') and (board[i][3]==player or board[i][3]=='T'):
            return 1
        if (board[0][i]==player or board[0][i]=='T') and (board[1][i]==player or board[1][i]=='T') and (board[2][i]==player or board[2][i]== 'T') and (board[3][i]==player or board[3][i]=='T'):
            return 1
    if (board[0][0]==player or board[0][0]=='T') and (board[1][1]==player or board[1][1]=='T') and (board[2][2]==player or board[2][2]== 'T') and (board[3][3]==player or board[3][3]=='T'):
        return 1
    if (board[0][3]==player or board[0][3]=='T') and (board[1][2]==player or board[1][2]=='T') and (board[2][1]==player or board[2][1]== 'T') and (board[3][0]==player or board[3][0]=='T'):
        return 1
    return 0
inp = file("A-small-attempt0.in")
temp = inp.read()
lines1 = temp.split('\n')
lines = []
for value in lines1:
    if value == '':
        print 
    else:
        lines.append(value)
board = []
T = int(lines[0])
tag = 0
outp = file("output.txt","w")
for i in range(T):
    board = []
    for j in range(4):
        board.append(lines[1+i*4+j])
    if isWin (board, 'X'):
        outp.write('Case #'+str(i+1)+': X won\n')
    elif isWin(board, 'O'):
        outp.write('Case #'+str(i+1)+': O won\n')
    else:
        for line in board:
            if '.' in line:
                tag = 1
            else:
                tag = 2
    if tag == 1:
        outp.write('Case #'+str(i+1)+': Game has not completed\n')
        tag = 0
    if tag == 2:
        outp.write('Case #'+str(i+1)+': Draw\n')
        tag = 0
outp.close()
