#!/usr/bin/env python



grpPtr=0
grpList=[]
numGrp=0
#grpList=[1,4,2,1]
#
#numGrp=len(grpList)
#print 'numgrp', numGrp
#grpPtr=0
#print 'grpPtr', grpPtr

def getGrp(num):

    global grpPtr
    global grpList
    global numGrp

    total=0
    
    gLoaded=0
    
    #print 'called'
    while True:
        curSize=grpList[grpPtr]
        if total+curSize>num or gLoaded>=numGrp:
            return total
        else:
            total+=curSize
            gLoaded+=1
            #print curSize
            grpPtr=(grpPtr+1)%numGrp    
    
def calc(run, cap, gList):
    income=0
    
    global grpPtr
    grpPtr=0
    
    global grpList
    grpList=gList
    
    global numGrp
    numGrp=len(grpList)
    
    
    
    for r in xrange(0,run):
        income+=getGrp(cap)
        
    return income
    
import sys
fname=sys.argv[1]

#print calc(run,cap,grpList)

f=open(fname,'r')
numInput=int(f.readline())
for num in xrange(1,numInput+1):
    line=f.readline().strip()
    raw=line.split()
    
    run=int(raw[0])
    cap=int(raw[1])
    grp=int(raw[2])

    line=f.readline().strip()
    raw=line.split()
    
    gList=[]
    for i in raw:
        gList.append(int(i))
        

   
    print 'Case #'+str(num)+': '+str(calc(run,cap,gList))#, '-----------------------------------------------'#, n , k



