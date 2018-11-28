f=open("A-large.in","r")
f2=open("ans.out","w")
x=int(f.readline())
for a in range(x):
    temp=[]
    for i in range(4):
        temp.append([i for i in f.readline()])
    f.readline()
    x=False
    o=False
    empty=False
    for i in [0,1,2,3]:
        if 'O' not in temp[i] and '.' not in temp[i]:
            x=True
            break
        if 'X' not in temp[i] and '.' not in temp[i]:    
            o=True
            break
    for i in [0,1,2,3]:
        countx,counto=0,0
        for j in[0,1,2,3]:
            if 'O' not in temp[j][i] and '.' not in temp[j][i]:
                countx+=1
            if 'X' not in temp[j][i] and '.' not in temp[j][i]: 
                counto+=1
        if countx==4:
            x=True
            break
        if counto==4:
            o=True
            break
    diag1=[temp[0][0],temp[1][1],temp[2][2],temp[3][3]]
    diag2=[temp[0][3],temp[1][2],temp[2][1],temp[3][0]]
    if 'O' not in diag1 and '.' not in diag1:
            x=True
    if 'X' not in diag1 and '.' not in diag1:
            o=True
    if 'O' not in diag2 and '.' not in diag2:
            x=True
    if 'X' not in diag2 and '.' not in diag2:
            o=True
    for i in temp:
        if '.' in i:
                empty=True
                break
    t=a+1
    if x==True:
        f2.write("Case #%d: X won\n"%t)
    elif o==True:
        f2.write("Case #%d: O won\n"%t)
    elif x==False and o==False and empty==False:
        f2.write("Case #%d: Draw\n"%t)
    else:
        f2.write("Case #%d: Game has not completed\n"%t)
f.close()
f2.close()
        