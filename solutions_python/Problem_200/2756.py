test=int(input())
for test in range(test):
    rt=input()
    it=0
    kj=0
    kj=it
    it=it-1
    it=it%10
    if(it==0):
        kj=it-1
    rt=list(rt)
    it=it+1
    rt.reverse()
    print('Case #',end='')
    print(test+1,end=': ')
    for i in range(len(rt)-1):
        if(rt[i]>=rt[i+1]):
            continue
        else:
            rt[i+1]=str(int(rt[i+1])-1)
            for j in range(i+1):
                rt[j]='9'
    #joining the stings    
    x=''.join(rt)
    #print(x)
    rt.reverse()
    #again printing the reverse 
    rt=''.join(rt)
    lt=0
    lt=lt-1
    #preserve the mod
    if(lt==it):
        lt=kj
    else:
        lt=0
    print(int(rt))
