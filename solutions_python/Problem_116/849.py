inp=open('A-large.in','r')
n=int(inp.readline().rstrip('\n'))
for counter in range(1,n+1):
    game=[[None for _ in range(4)] for _ in range(4)]
    for i in range(4):
        line=inp.readline().rstrip('\n')
        j=0
        for letter in line:
            game[i][j]=letter
            j+=1
    result=0
    for i in range(4):
        
        if set(game[i])==set(['X']) or set(game[i])==set(['X','T']) or set(game[i])==set(['T','X']):
            result=1
        elif set(game[i])==set(['O']) or set(game[i])==set(['O','T']) or set(game[i])==set(['T','O']):
            result=2
    for i in range(4):
        vert=[]
        for j in range(4):
            vert.append(game[j][i])
        if set(vert)==set(['X']) or set(vert)==set(['X','T']) or set(vert)==set(['T','X']):
            result=1
        elif set(vert)==set(['O']) or set(vert)==set(['O','T']) or set(vert)==set(['T','O']):
            result=2
    diag=[game[0][0],game[1][1],game[2][2],game[3][3]]
    if set(diag)==set(['X']) or set(diag)==set(['X','T']) or set(diag)==set(['T','X']):
        result=1
    elif set(diag)==set(['O']) or set(diag)==set(['O','T']) or set(diag)==set(['T','O']):
        result=2
    diag=[game[3][0],game[2][1],game[1][2],game[0][3]]
    if set(diag)==set(['X']) or set(diag)==set(['X','T']) or set(diag)==set(['T','X']):
        result=1
    elif set(diag)==set(['O']) or set(diag)==set(['O','T']) or set(diag)==set(['T','O']):
        result=2
    
    if result==0:
        for i in range(4):
            if '.' in game[i]:
                result=4
        if result!=4:
            result=3
    if result==1:
        res='X won'
    elif result==2:
        res='O won'
    elif result==3:
        res='Draw'
    else:
        res='Game has not completed'
    print 'Case #%d: %s'%(counter,res)
        
        
    if counter!=n:
        line=inp.readline()
   
    


