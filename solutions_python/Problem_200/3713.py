def liste(L):
    LL=L[:]
    l=len(LL)
    S=0
    for j in range (l):
        S+=LL[-1]*(10**j)
        LL.pop()
    return (int(S))

def tidy(x):
    R=[int(s) for s in str(x)]
    if R==sorted(R) or x==0:
        return (x)
    for k in range (len(R)-1):
        if R[k]>R[k+1]:
            if R[k]==1:
                kk=k-1
                if kk==-1:
                    return (x-liste(R[1:])-1)
                if R[kk]==1 or kk==0:
                    return (x-liste(R[1:])-1)
                while kk>=1:
                    if R[kk]==R[kk-1]:
                        kk-=1
                        continue
                    break
                return(x-liste(R[:kk]+[R[kk]-1]+(len(R)-k+1)*[9]))
            else:
                if k==0:
                    s=R[:k]+[R[k]-1]+(len(R)-k-1)*[9]
                    return(liste(s))
                if R[k-1]==R[k]:
                    kk=k
                    l=R[k]
                    while kk>=1:
                        if R[kk-1]==l:
                            kk=kk-1
                            continue
                        break
                    s=R[:kk]+[R[kk]-1]+(len(R)-kk-1)*[9]
                    return(liste(s))                    
                    
                        
                s=R[:k]+[R[k]-1]+(len(R)-k-1)*[9]
                return(liste(s))
T=int(input())
for i in range (1, T+1):
    N=int(input())
    print("Case #{}: {}".format(i,tidy(N)))