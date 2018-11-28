filename  = "A-small-attempt0.in" #"A-large.in"
f = open(filename,'r')
out = open("output.out",'w')
T =int(f.readline())
for Ca in range(T):
    [N,P]=[int(j) for j in f.readline().split(" ")]
    G= [int(j) for j in f.readline().split(" ")]
    GmP =[g %P for g in G]
    Count =[GmP.count(i) for i in range(P)]
    fresh = Count[0]
    Count=Count[1:]
    print("asdf")
    print(Count)
    for i in range((len(Count)+1)//2):
        m=min(Count[i],Count[P-2-i])
        fresh+=m
        Count[i]-=m
        Count[P-2-i]-=m
    if P<=3:
        s=sum(Count)
        fresh+=(s+P-1)//P
    if P==4:
        fresh+=Count[1]//2
        Count[1]=Count[1]%2    
        a = max(Count[0],Count[2])
        if Count[1]>0 and (a>1):
            a-=2
            fresh+=1
        fresh+=(a+3)//4   
    ret=str(fresh)
    print("Case #"+str(Ca+1)+": "+ret)
    out.write("Case #"+str(Ca+1)+": "+ret+"\n")

f.close()
out.close()
