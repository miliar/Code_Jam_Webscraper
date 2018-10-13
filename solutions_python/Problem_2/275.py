#!/usr/bin/python

import sys

def GetAvTime(arr, ta):
    
    hour, min = arr.split(':')
    hour = int(hour)
    min = int(min)
        
    if (min + ta) >= 60:
        hour += 1
        min = min + ta - 60
    else:
        min = min + ta
    
    return('%02d:%02d' % (hour, min))

def prepDicts(table, ta):
    
    tdep = {}
    tarr = {}
    tav = {}
    for time in table:
            
        dep, arr = time.split(' ')            
            
        if tdep.has_key(dep):
            tdep[dep] += 1
        else:
            tdep[dep] = 1
            
        tarr[arr] = 1            
            
        avTime = GetAvTime(arr, ta)
        if tav.has_key(avTime):
            tav[avTime] +=  1
        else:
            tav[avTime] = 1
        
    return(tdep, tarr, tav)

def CountTrains(tdep, tav):

    count = 0
    for depKey in sorted(tdep.iterkeys()):
        
        depValue = tdep[depKey]
        for i in xrange(depValue):            

            hasTrain = False            
            for avKey in sorted(tav.iterkeys()):                
            
                avValue = tav[avKey]
                if (depKey >= avKey) and (tav[avKey] > 0):
                    tav[avKey] -= 1
                    hasTrain = True
                    break
            
            if hasTrain == False:
                count += 1
            
    return(count)        

def main():
    
    caseCount = int(sys.stdin.readline().strip())
    
    for caseNum in xrange(1, caseCount+1):
        
        turnAround = int(sys.stdin.readline().strip())       
        
        travelCount = sys.stdin.readline().strip().split()
        na = int(travelCount[0])
        nb = int(travelCount[1])
        
        tab = []
        tba = []
        
        for i in xrange(na):
            tab.append(sys.stdin.readline().strip())
            
        for i in xrange(nb):
            tba.append(sys.stdin.readline().strip())
        
        tab.sort()
        tba.sort()
                
        tabDep, tabArr, tbaAv = prepDicts(tab, turnAround)
        tbaDep, tbaArr, tabAv = prepDicts(tba, turnAround)        
            
        trainACount = 0
        trainBCount = 0        
                
        trainACount = CountTrains(tabDep, tabAv)
        trainBCount = CountTrains(tbaDep, tbaAv)    
        
        print 'Case #%d: %d %d' % (caseNum, trainACount, trainBCount)
    
main()