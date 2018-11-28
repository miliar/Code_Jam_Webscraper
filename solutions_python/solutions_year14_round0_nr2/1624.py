T=int(input())

for t in range(0,T):
    L=input().split()
    C=float(L[0])
    F=float(L[1])
    X=float(L[2])
    f=float(2.0)
    secs=0.0
    t1=X/f
    t2=C/f
    f+=F
    t3=X/f
    while (t1-t2)>t3:
        secs+=t2
        t1=t3
        t2=C/f
        f+=F
        t3=X/f
    secs+=t1
    print("Case #%d: %.10f"%(t+1,secs))
