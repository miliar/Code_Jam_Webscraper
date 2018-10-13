def checkdraw(game):
    i=0
    while i<4:
        if ('.' in game[i])==True:
            return 0
        i=i+1
    return 1
def checkwin(str1):
    co=0
    cx=0
    ct=0
    i=0
    while(i<4):
        if(str1[i]=='X'):
            cx=cx+1
        elif str1[i]=='O':
            co=co+1
        elif str1[i]=='T':
            ct=ct+1
        i=i+1
    if(cx==4) or (cx==3 and ct==1):
        return 1
    elif (co==4) or (co==3 and ct==1):
        return 2
    else:
        return -1
def checkdiag(game):
    i=0
    g=[]
    g1=[]
    while i<4:
        j=0
        while j<4:
            if(i==j):
                g.append(game[i][j])
            if(i+j==3):
                g1.append(game[i][j])
            j=j+1
        i=i+1
    g=''.join(g)
    g1=''.join(g1)
    n=checkwin(g)
    t=checkwin(g1)
    if n==1 or n==2:
        return n
    elif t==1 or t==2:
        return t
    else:
        return -1
    
def checkgame(game):
    c=0
    n=checkdiag(game)
    if n!=-1:
        return n
    else:
        c=c+2
        
    i=0
    while i<4:
        n=checkwin(game[i])
        if n==1 or n==2:
            return n
        elif n==-1:
            c=c+1
        i=i+1
        
    i=0
    while i<4:
        j=0
        g=[]
        while j<4:
            g.append(game[j][i])
            j=j+1
        g=''.join(g)
        n=checkwin(g)
        if n==1 or n==2:
            return n
        elif n==-1:
            c=c+1
        i=i+1

    if c==10:
        return -1
    
            
    
    
def ticTacToe():
    infile=file("G:\ONLINE COURSES\Google Code Jam 2013\ALIN.IN",'r')
    whole=infile.readlines()
    infile.close()
    n=int(whole[0])
    i=1
    output=[]
    while(i<=(n*5)):
        j=0
        game=[]
        while j<4:
            game.append(whole[i+j])
            j=j+1
        ch=checkgame(game)
        if ch==1:
            output.append(1)
        elif ch==2:
            output.append(2)
        elif ch==-1 and checkdraw(game)==1:
            output.append(0)
        elif ch==-1 and checkdraw(game)==0:
            output.append(-1)
        i=i+5
    i=0
    while i<n:
        if output[i]==1:
            print"Case #"+str(i+1)+": X won"
        elif output[i]==2:
            print"Case #"+str(i+1)+": O won"
        elif output[i]==0:
            print"Case #"+str(i+1)+": Draw"
        elif output[i]==-1:
            print"Case #"+str(i+1)+": Game has not completed"
        i=i+1
        
        
            
        

if __name__=="__main__":
    ticTacToe()
