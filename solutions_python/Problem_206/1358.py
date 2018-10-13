def llegada(xf,xi,v):
    return (xf-xi)/v

T = int(input())
i=0
while(i<T):
    i+=1
    print("Case #%i: "%(i),end="")
    D,N = [int(e) for e in input().split()]
    k = 0
    t = 0
    while(k<N):
        ki,vi = [int(e) for e in input().split()]
        if(ki<D):
            ti=llegada(D,ki,vi)
            if(ti>t):
                t = ti
        k+=1    
    if(t==0):
        print("%.6f"%(D))
    else:
        print("%.6f"%(D/t))
