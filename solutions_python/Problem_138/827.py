
fname="D-large.in"

inputF=open(fname,'r+')
outF=open('outputdlarge','w+')

T=int(inputF.readline())
for q in xrange(T):
    noOfRocks=int(inputF.readline())
    #~ print noOfRocks
    noOfRocksDyn=noOfRocks
    noOfRocksDynDWar=noOfRocks
    nPoints=0
    kPoints=0
    #~ [float(x) for x in s.split()]
    nRocks=sorted([float(x) for x in inputF.readline().split()])
    kRocks=sorted([float(x) for x in inputF.readline().split()])
    
    nRocksDWar=nRocks[:]
    kRocksDWar=kRocks[:]
    
    for i in xrange(noOfRocks):
        kgotpoint=0
        #~ print nRocks,kRocks
        nRock=nRocks.pop(0)
        #~ print nRock
        for j in xrange(noOfRocksDyn):
            kRock=kRocks[j]
            if kRock>nRock:
                kRocks.pop(j)           
                kPoints+=1
                kgotpoint=1
                break
        if not kgotpoint:
            kRocks.pop(0)            
            nPoints+=1
        noOfRocksDyn-=1
        
    #~ print nRocksDWar,kRocksDWar
    #~ print 'W',nPoints
    
    nPointsD=0
    kPointsD=0
    for i in xrange(noOfRocks):
        kgotpoint=0
        #~ print nRocks,kRocks
        if nRocksDWar[-1]<kRocksDWar[-1]:
            
            nRock=nRocksDWar.pop(0)
        else:
            nRock=nRock=nRocksDWar.pop(-1)
        if noOfRocksDynDWar>1:            
            nRockTold=(kRocksDWar[-1]+kRocksDWar[-2])/2
            if nRock<nRockTold:
                nRock=nRockTold
        #~ print nRock
        for j in xrange(noOfRocksDynDWar):
            kRock=kRocksDWar[j]
            if kRock>nRock:
                kRocksDWar.pop(j)           
                kPointsD+=1
                kgotpoint=1
                break
        if not kgotpoint:
            kRocksDWar.pop(-1)            
            nPointsD+=1
        noOfRocksDynDWar-=1
    
    #~ print nPointsD,nPoints
    outF.write('Case #'+str(q+1)+': '+str(nPointsD)+' '+str(nPoints)+'\n')
    #~ print 'Case #'+str(q+1)+': '+str(nPointsD)+' '+str(nPoints)+'\n',
inputF.close()
outF.close()
