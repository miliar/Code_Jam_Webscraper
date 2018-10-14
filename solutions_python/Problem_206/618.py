T = int(raw_input())
for t in range(T):
    D,N=[int(i) for i in raw_input().split()]
    d=float(D)
    K=[]
    S=[]
    T=[]
    for i in range(N):
        ki,si=[int(j) for j in raw_input().split()]
        K.append(ki)
        S.append(si)
        T.append((d-ki)/si)
    ts = sorted(T)
    #print ts
    tx = ts[-1]
    #print d,tx
    v= d/float(tx)
    print "Case #%d: %f" %(t+1,v)
        
        
