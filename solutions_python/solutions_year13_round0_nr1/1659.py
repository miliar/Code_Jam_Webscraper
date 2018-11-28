'''
Created on 2013/4/13

@author: kaimugen
'''


f=open("A-large.in",'r')
caseTotal=f.readline()
caseCount=0
f2=open("output2.txt",'w')
print(caseTotal)
while(caseCount<int(caseTotal)):
    board=[]
    caseCount+=1
    for i in range(4):
        temp=f.readline()
        board.append(temp[:-1])
    print(board)
    state=0
    dot=0
    """check row"""
    for i in range(4):
        T=0
        X=0
        O=0       
        for w in range(4):
            if(board[i][w]=="T"):
                T+=1
            elif(board[i][w]=="X"):
                X+=1
            elif(board[i][w]=="O"):
                O+=1
            elif(board[i][w]=="."):
                dot+=1
        if(T==1 and X==3):
            state=1
        elif(T==1 and O==3):
            state=2
        elif(X==4):
            state=1
        elif(O==4):
            state=2   
    """check column"""
    for i in range(4):
        T=0
        X=0
        O=0       
        for w in range(4):
            if(board[w][i]=="T"):
                T+=1
            elif(board[w][i]=="X"):
                X+=1
            elif(board[w][i]=="O"):
                O+=1
            elif(board[w][i]=="."):
                dot+=1
        if(T==1 and X==3):
            state=1
        elif(T==1 and O==3):
            state=2
        elif(X==4):
            state=1
        elif(O==4):
            state=2
    """check diogonal"""
    T=0
    X=0
    O=0  
    for i in range(4):          
        if(board[i][i]=="T"):
            T+=1
        elif(board[i][i]=="X"):
            X+=1
        elif(board[i][i]=="O"):
            O+=1
        elif(board[i][i]=="."):
            dot+=1
    if(T==1 and X==3):
        state=1
    elif(T==1 and O==3):
        state=2
    elif(X==4):
        state=1
    elif(O==4):
        state=2
    if(caseCount==6):
        print([board[0][0]],[board[1][1]],[board[2][2]],[board[3][3]])
        print(T,X,O,dot)
    T=0
    X=0
    O=0 
    for i in range(4):   
        if(board[i][3-i]=="T"):
            T+=1
        elif(board[i][3-i]=="X"):
            X+=1
        elif(board[i][3-i]=="O"):
            O+=1
        elif(board[i][3-i]=="."):
            dot+=1
    if(T==1 and X==3):
        state=1
    elif(T==1 and O==3):
        state=2
    elif(X==4):
        state=1
    elif(O==4):
        state=2
    
    if(state==1):
        f2.write(("Case #%d: X won")%(caseCount))
    elif(state==2):
        f2.write(("Case #%d: O won")%(caseCount))
    elif(dot==0):
        f2.write(("Case #%d: Draw")%(caseCount))
    else:        
        f2.write(("Case #%d: Game has not completed")%(caseCount))
    f2.write("\n")           
    f.readline()
f.close()
f2.close()
                
    