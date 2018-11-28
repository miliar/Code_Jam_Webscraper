fin=open("B-large.in","r")
fout=open("OutputB.out","w")
Ans=""
T=int(fin.readline())

for t in range(T):
    Ans+="Case #"+str(t+1)+": "
    C,F,X=map(float,fin.readline().split())
    time=C/2
    coins=C
    f=0
    while(1):
        if(X/(2+(f+1)*F)>=(X-C)/(2+f*F)):
            time+=(X-C)/(2+f*F)
            break
        else:
            f+=1
            time+=C/(2+f*F)
    Ans+=str(time)+"\n"
fout.write(Ans)
fout.close()
