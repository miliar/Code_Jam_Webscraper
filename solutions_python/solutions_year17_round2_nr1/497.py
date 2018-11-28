T = int(input())
for i in xrange(T):
    D,N =str(raw_input()).split()
    D=float(D)
    ss=[]
    for j in xrange(int(N)):
            K,S = str(raw_input()).split()
            K=float(K)
            S=float(S)
            T= (D-K)/S
            ss.append([K,T])
    ss =sorted(ss, reverse=True, key=lambda horse: horse[0])
    t=ss[0][1]
    for h in ss:
        t=max(t,h[1])
    
    answer=str(D/t)
    print "Case #"+str(i+1)+": "+answer


    
        
