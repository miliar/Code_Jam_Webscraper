def Dic(T,K):
    mi,ma,k=0,0,0
    while k!=K:
        for i in range(len(T)):
            if T[i]==max(T):
                if T[i]%2==0:
                    mi=(T[i]-2)//2
                    ma=(T[i])//2
                    T=T[:i]+[mi]+[ma]+T[i+1:]
                else:
                    mi=(T[i]-1)//2
                    ma=(T[i]-1)//2
                    T=T[:i]+[mi]+[ma]+T[i+1:]
                break
        k+=1
    return ([ma,mi])
R=int(input())
for i in range(1,R+1):
    N, K=[int(s) for s in input().split(' ')]
    print ('Case #{}: {} {}'.format(i, Dic([N],K)[0],Dic([N],K)[1]))