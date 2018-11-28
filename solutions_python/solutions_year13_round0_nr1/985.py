f=open("A-large.in")
f2 = open("output.txt","w")
n = int(f.readline())
list_t = list()
win=0
status=[[0 for i in range(0,4)] for j in range(0,4)]
game=[[0 for i in range(0,4)] for j in range(0,4)]
for i in range (0,n):
    status=[[0 for p in range(0,4)] for l in range(0,4)]
    game=[[0 for p in range(0,4)] for l in range(0,4)]
    win=0
    for j in range (0,4):
        game[j]=list(f.readline().strip("\n"))
    for k in range (0,4):
        for m in range (0,4):
            if game[k][m]=='X':
                status[k][m]=1
            elif game[k][m]=='O':
                status[k][m]=2
            elif game[k][m]=='T':
                status[k][m]=3
    for x in range(0,4):
        if (status[x][0]==1 or status[x][0]==3)  and (status[x][1]==1 or status[x][1]==3) and (status[x][2]==1 or status[x][2]==3) and (status[x][3]==1 or status[x][3]==3):
            win=1
        elif (x==0) and (status[x][0]==1 or status[x][0]==3)  and (status[x+1][1]==1 or status[x+1][1]==3) and (status[x+2][2]==1 or status[x+2][2]==3) and (status[x+3][3]==1 or status[x+3][3]==3):
            win=1
        elif (x==3) and (status[x][0]==1 or status[x][0]==3)  and (status[x-1][1]==1 or status[x-1][1]==3) and (status[x-2][2]==1 or status[x-2][2]==3) and (status[x-3][3]==1 or status[x-3][3]==3):
            win=1
        elif (status[x][0]==2 or status[x][0]==3)  and (status[x][1]==2 or status[x][1]==3) and (status[x][2]==2 or status[x][2]==3) and (status[x][3]==2 or status[x][3]==3):
            win=2
        elif (x==0) and (status[x][0]==2 or status[x][0]==3)  and (status[x+1][1]==2 or status[x+1][1]==3) and (status[x+2][2]==2 or status[x+2][2]==3) and (status[x+3][3]==2 or status[x+3][3]==3):
            win=2
        elif (x==3) and (status[x][0]==2 or status[x][0]==3)  and (status[x-1][1]==2 or status[x-1][1]==3) and (status[x-2][2]==2 or status[x-2][2]==3) and (status[x-3][3]==2 or status[x-3][3]==3):
            win=2
    for x in range(0,4):
        if (status[0][x]==1 or status[0][x]==3)  and (status[1][x]==1 or status[1][x]==3) and (status[2][x]==1 or status[2][x]==3) and (status[3][x]==1 or status[3][x]==3):
            win=1
        
        if (status[0][x]==2 or status[0][x]==3)  and (status[1][x]==2 or status[1][x]==3) and (status[2][x]==2 or status[2][x]==3) and (status[3][x]==2 or status[3][x]==3):
           
            win=2
    if win==0:
        for q in range(0,4):
            for r in range(0,4):
                if status[q][r]==0:
                    win=-1
                    break
            if win==-1:
                break
   
    if win==0:
        out = "Case #"+str(i+1)+": "+"Draw"+"\n"
    elif win==1:
        out = "Case #"+str(i+1)+": "+"X won"+"\n"
    elif win==2:
        out = "Case #"+str(i+1)+": "+"O won"+"\n"
    else:
        out = "Case #"+str(i+1)+": "+"Game has not completed"+"\n"
    f2.write(out)
    temp=f.readline()
    
f2.close()  

