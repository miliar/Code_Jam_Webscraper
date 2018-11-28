def status(x):
    #Look for a winner

    #Horizontal case
    for player in [['X',1],['O',2]]:
        for i in range(4):
            win=0
            for j in range(4):
                if x[i][j]==player[0] or x[i][j]=='T':
                    win=win+1
                else:
                    if 0<j<3:
                        win=-3
            if win>=4:
                return player[1]
    #Vertical case
        for i in range(4):
            win=0
            for j in range(4):
                if x[j][i]==player[0] or x[j][i]=='T':
                    win=win+1
                else:
                    if 0<j<3:
                        win=-3
            if win>=4:
                return player[1]
            
        win=0
        for i in range(4):
            if x[i][i]==player[0] or x[i][i]=='T':
                    win=win+1
            else:
                break
        if win>=4:
            return player[1]
        win=0
        for i in range(4):
            if x[i][3-i]==player[0] or x[i][3-i]=='T':
                    win=win+1
            else:
                break
        if win>=4:
            return player[1]
        
    #Look for incomplete game
    for i in x:
        for j in range(4):
            if i[j]=='.':
                return 3
    #Only case missing
    return 0
        
if __name__=='__main__':
    challenge='A-large.in'
    caso={0:'Draw',1:'X won',2:'O won',3:'Game has not completed'}
    i=1
    x=[]

    entrada=open(challenge,'r')
    salida=open('01result.txt','w')
    n=int(entrada.readline())

    while i<=n:
        x.append(entrada.readline())
        x.append(entrada.readline())
        x.append(entrada.readline())
        x.append(entrada.readline())
        entrada.readline()
        salida.write('Case #%d: %s\n'%(i,caso[status(x)]))
        x=[]
        i=i+1
    entrada.close()
    salida.close()
