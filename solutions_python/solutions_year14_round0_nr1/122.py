fin=open("A-small-attempt0.in","r")
fout=open("OutputA.out","w")
T=int(fin.readline())
Anss=""
for t in range(T):
    x=int(fin.readline())
    X=[]
    for i in range(4):
        X.append(list(map(int,fin.readline().split())))
    y=int(fin.readline())
    Y=[]
    for i in range(4):
        Y.append(list(map(int,fin.readline().split())))
    x-=1
    y-=1
    Ans=[]
    for item in X[x]:
        if(item in Y[y]):
            Ans.append(item)
    Anss+="Case #"+str(t+1)+": "
    if(len(Ans)==1):
        Anss+=str(Ans[0])+"\n"
    elif(len(Ans)==0):
        Anss+="Volunteer cheated!\n"
    else:
        Anss+="Bad magician!\n"
fout.write(Anss)
fout.close()
