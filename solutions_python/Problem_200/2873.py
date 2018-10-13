def untidy(N):
    u=-1
    n=list(map(int,str(N)))
    for i in range(len(n)-1):
        if n[i]>n[i+1]:
            u=i
            break
    return u
def tidy(N):
    u=untidy(N)
    if u==-1:
        return N
    else:
        n=list(map(int,str(N)))
        n[u]-=1
        for i in range(u+1,len(n)):
            n[i]=9
        N=int(''.join(map(str,n)))
        return tidy(N)
f=open('B-large.in','r')
o=open('out.txt','w')
T=int(f.readline())
for t in range(T):
    N=int(f.readline())
    o.write('Case #'+str(t+1)+': '+str(tidy(N))+'\n')
o.close()
f.close()