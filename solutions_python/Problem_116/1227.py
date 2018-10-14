fu=open('A-large.in','r')
prob=(fu).read().split()
fu.close()
out=''


N=int(prob[0])


def whowon(X):
    O=[[1 if (i=='O' or i=='T') else 0 for i in row] for row in X]
    if yes(O):
        return 'O won'
    
    Y=[[1 if (i=='X' or i=='T') else 0 for i in row] for row in X]
    if yes(Y):
        return 'X won'

    count=0
    for i in range(4):
        for j in range(4): 
            count=count + (0 if X[i][j]=='.' else 1)
    #import pdb; pdb.set_trace()
    if count==16:
        return 'Draw'

    return 'Game has not completed'
    

def yes(X):
    
    for i in range(4):
        count=0
        for j in range(4):
            count=count + X[i][j]
        if count==4:
            return True

        count=0
        for j in range(4):
            count=count + X[j][i]
        if count==4:
            return True

    if X[0][0]+X[1][1]+X[2][2]+X[3][3]==4 or X[0][3]+X[1][2]+X[2][1]+X[3][0]==4:
        return True

    return False



for n in range(N):
    board= prob[1+4*n:5+4*n]

    out=out + 'Case #%d: '%(n+1) + whowon(board) + '\n'


f=open('output','w')
f.write(out)
f.close()



