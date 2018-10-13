#!/usr/bin/env python
import sys

T = int(sys.stdin.readline())
casenum = 1
spolgloski = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

for i in range(0, T):
    SN = []
    SN = (sys.stdin.readline().split(' '))
    
    slowo = SN[0]
    n = int(SN[1])
    startPodslowa = 0
    nValue = 0
    
    for x in range(0, len(slowo)):
        if slowo[x] in spolgloski:
            tempIndex = x
            s=0
            while (x+s)<len(slowo) and s<n:
                if slowo[x+s] in spolgloski:
                    s+=1
                else:
                    break
            if s==n:
                #print str(nValue)
                literyPrzed = tempIndex-startPodslowa
                literyPo = len(slowo)-(tempIndex+n-1)-1
                
                #print str(tempIndex) + "          " +str(literyPrzed)+"   "+str(literyPo)
                
                nValue+=1
                
                if literyPrzed==0:
                    nValue+=literyPo
                    #print 'x'
                if literyPo==0:
                    nValue+=literyPrzed
                    #print 'y'
                if literyPrzed!=0 and literyPo!=0:
                    nValue+=(literyPrzed*(1+literyPo))+literyPo
                    #print 'z'
                
                startPodslowa = tempIndex+1
                #print "Start podslowa: "+str(startPodslowa)
                
    print 'Case #'+str(casenum)+': '+str(nValue)
    casenum+=1
    
    