import math
f = open('C-small-2-attempt2.in', 'r')

T = int(f.readline().strip())


for t in xrange(T):

    line = f.readline().strip()
    N=int(line.split(" ")[0])
    K=int(line.split(" ")[1])

    L=int(math.floor((N-1)/2.0))
    R=int(math.ceil((N-1)/2.0))
    nLR=[[1,[L,R]]]
    for i in xrange(K-1):

        maxLR=0
        maxLR2=0
        sLR=[0,0]
        for j in xrange(len(nLR)):
            LR=nLR[j]
            if LR[0]>0:
                if min(LR[1][0],LR[1][1])>=maxLR:
                    maxLR=min(LR[1][0],LR[1][1])
                    if max(LR[1][0],LR[1][1])>=maxLR2:
                        sLR=nLR[j][1]
                        maxLR2=max(LR[1][0],LR[1][1])
                        js=j
        #print "j",js,sLR,jsa
        if sLR[0]>0:
            L0=int(math.floor((sLR[0]-1)/2.0))
            R0=int(math.ceil((sLR[0]-1)/2.0))
        if sLR[1]>0:
            L1=int(math.floor((sLR[1]-1)/2.0))
            R1=int(math.ceil((sLR[1]-1)/2.0))

        #print "i",i,"nLR",nLR
        nLR[js][0]-=1
        if nLR[js][0]==0:
            del nLR[js]
        LR0=False
        LR1=False
        for j in xrange(len(nLR)):
            if sLR[0]>0:
                if [L0,R0] in nLR[j]:
                    nLR[j][0]+=1
                    LR0=True
            if sLR[1]>0:
                if [L1,R1] in nLR[j]:
                    nLR[j][0]+=1
                    LR1=True
        if L0==L1 and R0==R1 and not LR0 and not LR1:
            if sLR[0]>0 and sLR[1]>0:
                nLR.append([2,[L0,R0]])
        else:
            if not LR0:
                if sLR[0]>0:
                    nLR.append([1,[L0,R0]])
            if not LR1:
                if sLR[1]>0:
                    nLR.append([1,[L1,R1]])

        #print ""
        #if i>8:
        #    break

    #print "nLR",nLR

    maxLR=0
    maxLR2=0
    sLR=[0,0]
    for j in xrange(len(nLR)):
        LR=nLR[j]
        if LR[0]>0:
            if min(LR[1][0],LR[1][1])>=maxLR:
                maxLR=min(LR[1][0],LR[1][1])
                if max(LR[1][0],LR[1][1])>=maxLR2:
                    sLR=nLR[j][1]
                    maxLR2=max(LR[1][0],LR[1][1])

    print 'Case #%d: %d %d'% (t+1,max(sLR),min(sLR))