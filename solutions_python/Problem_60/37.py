cn=input()
for c in xrange(cn):
    
    chinum, oknum, dist, tim=[int(i) for i in raw_input().split()]
    pos=[int(i) for i in raw_input().split()]
    vol=[int(i) for i in raw_input().split()]
    spend=[]
    for i in xrange(len(pos)):
        s=(dist-pos[i])/vol[i]
        r=(dist-pos[i])%vol[i]
        if r!=0:
            s+=1
        spend.append(s)
    spend.reverse()
    ok=0
    cant=[]
    for i in xrange(len(pos)):
        if spend[i]<=tim:
            ok+=1
        else:
            cant.append(i)
        if ok==oknum:
            las=i
            break
    if ok<oknum:
        print "Case #%d: IMPOSSIBLE" %(c+1)
        continue
    res=0
    for nn,cc in enumerate(cant):
        res+=las-cc-(len(cant)-nn-1)
    
    print "Case #%d: %d" %(c+1, res)
