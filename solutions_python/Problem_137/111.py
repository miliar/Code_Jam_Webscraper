fin=open("C-small-attempt11.in","r")
fout=open("OutputC.out","w")

def Solve(L,M):
    if(M<0):
        return False
    #print(L,M)
    if(M==0):
        e=True
        
        for i in range(nn[0]):
            for j in range(mm[0]):
                x=L[i][j]
                if(x=='.' and e):
                    valid=True
                    for dx in range(-1,2):
                        for dy in range(-1,2):
                            if(i+dx<nn[0] and i+dx>=0 and j+dy>=0 and j+dy<mm[0]):
                                if(L[i][j]=='*'):
                                    valid=False
                    if(valid):
                        e=False
                        Ans[0]+="c"
                    else:
                        Ans[0]+=x
                    continue
                Ans[0]+=x
            Ans[0]+="\n"
        return True
    n=len(L)
    m=len(L[0])
    for i in range(nn[0]):
        for j in range(mm[0]):
            if(L[i][j]=='*'):
                continue
            V=[]
            for dx in range(-1,2):
                for dy in range(-1,2):
                    if(dx==0 and dy==0):
                        continue
                    if(i+dx>=0 and i+dx<nn[0] and j+dy>=0 and j+dy<mm[0]):
                        if(L[i+dx][j+dy]=='*'):
                            L[i+dx][j+dy]='.'
                            V.append((i+dx,j+dy))
            if(len(V)==0):
                continue
            if(M-len(V)<0):
                for item in V:
                    L[item[0]][item[1]]='*'
                continue
            if(Solve(L,M-len(V))):
                return True
            for item in V:
                L[item[0]][item[1]]='*'
    return False

T=int(fin.readline())
Ans=[""]
nn=[0]
mm=[0]
for t in range(T):
    Ans[0]+="Case #"+str(t+1)+":\n"
    n,m,M=map(int,fin.readline().split())
    nn=[n]
    mm=[m]
    F=n*m-M
    if(M==0):
        e=True
        for i in range(n):
            for j in range(m):
                if(i==0 and j==0):
                    Ans[0]+="c"
                    continue
                Ans[0]+="."
            Ans[0]+="\n"
        continue
    if(F==1):
        for i in range(n):
            for j in range(m):
                if(i==0 and j==0):
                    Ans[0]+="c"
                else:
                    Ans[0]+="*"
            Ans[0]+="\n"
        continue
    if(n==2 and m==2):
        Ans[0]+="Impossible\n"
        continue
    done=False
    for x in range(n):
        if(done):
            break
        for y in range(m):
            L=[]
            for i in range(n):
                L.append(['*']*m)
            cnt=1
            L[x][y]='.'
            
            if(Solve(L,F-cnt)):
                done=True
                break
    if(not done):
        Ans[0]+="Impossible\n"
    
fout.write(Ans[0])
fout.close()
