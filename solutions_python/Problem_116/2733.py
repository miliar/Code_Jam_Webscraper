def solve(Board):

    Is_point=False    
    
    L_T=[0,0,0,0]
    L_X=[0,0,0,0]
    L_O=[0,0,0,0]
    C_T=[0,0,0,0]
    C_X=[0,0,0,0]
    C_O=[0,0,0,0]   

    for i in range(4):
        for j in range(4):
            if Board[i][j]=='X':
                L_X[i]+=1
                C_X[j]+=1
            elif Board[i][j]=='O':
                L_O[i]+=1
                C_O[j]+=1
            elif Board[i][j]=='T':
                L_T[i]+=1
                C_T[j]+=1
            elif Board[i][j]=='.':
                Is_point=True            
    
    for i in range(4):
        if L_X[i]==4 or (L_X[i]==3 and L_T[i]==1):
            return "X won"
        elif L_O[i]==4 or (L_T[i]==3 and L_T[i]==1):
            return "O won"
        if C_X[i]==4 or (C_X[i]==3 and C_T[i]==1):
            return "X won"
        elif C_O[i]==4 or (C_T[i]==3 and C_T[i]==1):
            return "O won"
    
    D1_X=D2_X=D1_O=D2_O=D1_T=D2_T=0 
    for i in range(4):
        if Board[i][i]=='X':
            D1_X+=1
        elif Board[i][i]=='O':
            D1_O+=1
        elif Board[i][i]=='T':
            D1_T+=1
        if Board[i][-i-1]=='X':
            D2_X+=1
        elif Board[i][-i-1]=='O':
            D2_O+=1
        elif Board[i][-i-1]=='T':
            D2_T+=1
    if D1_X==4 or (D1_X==3 and D1_T==1)or D2_X==4 or (D2_X==3 and D2_T==1):
        return "X won"
    elif D1_O==4 or (D1_O==3 and D1_T==1)or D2_O==4 or (D2_O==3 and D2_T==1):
        return "O won"

    if Is_point:
        return "Game has not completed"
    else:
        return "Draw"
    

  
                
    
            


#Main
f=open("A-small-attempt0.in","r")
lines=f.readlines()
f.close()

N_cases=eval(lines[0])
solutions=[]

line=1
for i in range(N_cases):
    Board=[]
    for j in range(line,line+4):
        temp=[]
        for el in lines[j].strip('\n'):
            temp.append(el)
        Board.append(temp)
    line+=5
    solution="Case #"+str(i+1)+": "+solve(Board)+"\n"
    solutions.append(solution)
    print("Case "+str(i+1)+" done.")

f=open("o.in","w")
f.writelines(solutions)
f.close()
