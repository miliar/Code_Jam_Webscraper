T=int(input())
for t in range(0,T):
    L=input().split(" ")
    Smax=int(L[0])
    S=L[1]
    Standing=0
    Needed=0
    for c in range(0,Smax+1):
        i=int(S[c])
        if i>0:
            if c>Standing:
                Needed=Needed+c-Standing
                Standing=Standing+Needed
            Standing=Standing+i
    print("Case #%d: %d"%(t+1,Needed))
                
