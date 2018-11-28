
T=int(input())

for i in range(T):
    tab=[[],[],[],[]]
    tab[0]=input()
    tab[1]=input()
    tab[2]=input()
    tab[3]=input()
    input()
    r="Draw"
	
    for j in range(4):
        if(r=="Draw" and (tab[j][0]=="." or tab[j][1]=="." or tab[j][2]=="." or tab[j][3]==".")):
            r="Game has not completed"
        if((tab[j][0]=="X" or tab[j][0]=="T") and (tab[j][1]=="X" or tab[j][1]=="T") and (tab[j][2]=="X" or tab[j][2]=="T") and (tab[j][3]=="X" or tab[j][3]=="T")):
            r="X won"
        if((tab[j][0]=="O" or tab[j][0]=="T") and (tab[j][1]=="O" or tab[j][1]=="T") and (tab[j][2]=="O" or tab[j][2]=="T") and (tab[j][3]=="O" or tab[j][3]=="T")):
            r="O won"

    for j in range(4):
        if((tab[0][j]=="X" or tab[0][j]=="T") and (tab[1][j]=="X" or tab[1][j]=="T") and (tab[2][j]=="X" or tab[2][j]=="T") and (tab[3][j]=="X" or tab[3][j]=="T")):
            r="X won"
        if((tab[0][j]=="O" or tab[0][j]=="T") and (tab[1][j]=="O" or tab[1][j]=="T") and (tab[2][j]=="O" or tab[2][j]=="T") and (tab[3][j]=="O" or tab[3][j]=="T")):
            r="O won"

    if((tab[0][0]=="X" or tab[0][0]=="T") and (tab[1][1]=="X" or tab[1][1]=="T") and (tab[2][2]=="X" or tab[2][2]=="T") and (tab[3][3]=="X" or tab[3][3]=="T")):
        r="X won"

    if((tab[0][0]=="O" or tab[0][0]=="T") and (tab[1][1]=="O" or tab[1][1]=="T") and (tab[2][2]=="O" or tab[2][2]=="T") and (tab[3][3]=="O" or tab[3][3]=="T")):
        r="O won"

    if((tab[0][3]=="X" or tab[0][3]=="T") and (tab[1][2]=="X" or tab[1][2]=="T") and (tab[2][1]=="X" or tab[2][1]=="T") and (tab[3][0]=="X" or tab[3][0]=="T")):
        r="X won"

    if((tab[0][3]=="O" or tab[0][3]=="T") and (tab[1][2]=="O" or tab[1][2]=="T") and (tab[2][1]=="O" or tab[2][1]=="T") and (tab[3][0]=="O" or tab[3][0]=="T")):
        r="O won"
    
    print("Case #"+str(i+1)+": "+str(r))
