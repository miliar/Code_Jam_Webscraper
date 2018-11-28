def tttt():
    f=open('A-large.in', 'r')
    cases=f.readline()
    cases=int(cases)
    for i in range(cases):
        temp=[]
        temp.append(['.']*4)
        temp.append(['.']*4)
        temp.append(['.']*4)
        temp.append(['.']*4)
        for k in range(4):
            line=f.readline()
            for j in range(4):
                temp[k][j]=line[j]
        f.readline()
        print 'Case #'+str((i+1))+': '+winning(temp)

def winning(board):
#    print board
    Xs=['X','T']
    Ys=['O','T']
    for i in range(4):
        if (board[i][0] in Xs) and (board[i][1] in Xs) and (board[i][2] in Xs) and (board[i][3] in Xs):
            return 'X won'
        if (board[i][0] in Ys) and (board[i][1] in Ys) and (board[i][2] in Ys) and (board[i][3] in Ys):
            return 'O won'
        if (board[0][i] in Xs) and (board[1][i] in Xs) and (board[2][i] in Xs) and (board[3][i] in Xs):
            return 'X won'
        if (board[0][i] in Ys) and (board[1][i] in Ys) and (board[2][i] in Ys) and (board[3][i] in Ys):
            return 'O won'
    if (board[0][0] in Ys) and (board[1][1] in Ys) and (board[2][2] in Ys) and (board[3][3] in Ys):
        return 'O won'
    if (board[0][0] in Xs) and (board[1][1] in Xs) and (board[2][2] in Xs) and (board[3][3] in Xs):
        return 'X won'
    if (board[0][3] in Xs) and (board[1][2] in Xs) and (board[2][1] in Xs) and (board[3][0] in Xs):
        return 'X won'
    if (board[0][3] in Ys) and (board[1][2] in Ys) and (board[2][1] in Ys) and (board[3][0] in Ys):
        return 'O won'
    for i in range(4):
        for j in range(4):
            if board[i][j]=='.':
                return 'Game has not completed'
    return 'Draw'

tttt()
