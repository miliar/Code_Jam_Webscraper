T=int(raw_input())
for t in range(T):
    z=raw_input()
    S=z.split()[0]
    K = int(z.split()[1])
    rv=0
    flips=[False]*len(S)
    ok=True
    for i in range(len(S)):
        if S[i]=='+' and flips[i]==False or S[i]=='-' and flips[i]==True:
            continue
        rv+=1
        if i+K>len(S):
            ok=False
            break
        
        for j in range(K):
            flips[i+j]=not flips[i+j]
    if ok:
        print "Case #%d: %d" %(t+1,rv)
    else:
        print "Case #%d: IMPOSSIBLE" % (t+1)
        
        
