fi=open("input.txt")
for testNum in range(int(fi.readline().strip())):
    fi.readline()
    n=sorted([float(i) for i in fi.readline().strip().split(" ")])
    k=sorted([float(i) for i in fi.readline().strip().split(" ")])
    k1 = k[:]
    nPoints=0
    for ni in n:
        nKiller=-1
        for ke in k:
            if (ke > ni):
                nKiller=ke
                break
        if (nKiller!=-1):
            k.remove(nKiller)
        else:
            nPoints+=1
    nDPoints=0
    k = k1[:]
    for ni in reversed(n):
        if (ni > max(k)):
            nDPoints +=1
            k.remove(max(k))
        else:
            n.remove(min(n))
            k.remove(max(k))
    print("Case #"+str(testNum+1)+": "+str(nDPoints)+" "+str(nPoints))
        
    
    
    
    
