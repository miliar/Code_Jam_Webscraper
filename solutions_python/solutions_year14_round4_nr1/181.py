fin=open("A-large.in","r")
fout=open("/home/ahmed_ossama/Round 2/Task A/Output.txt","w")

T=int(fin.readline())
Ans=""
for t in range(T):
    print(t)
    Ans+="Case #"+str(t+1)+": "
    n,x=map(int,fin.readline().split())
    L=list(map(int,fin.readline().split()))
    L.sort(reverse=True)
    Cnt=[0]*701
    for item in L:
        Cnt[item]+=1
    ans=0
    for i in range(x,-1,-1):
        if(Cnt[i]==0):
            continue
        while(Cnt[i]>0):
            rem=x-i
            Cnt[i]-=1
            ans+=1
            for j in range(rem,0,-1):
                if(Cnt[j]>=1):
                    Cnt[j]-=1
                    break
    Ans+=str(ans)+"\n"
fout.write(Ans)
fout.close()
        
                
