#!/usr/bin/env python
# -*- coding: utf-8 -*-



if __name__ == "__main__":
    
    inFile = open("B-large.in","r")
    outFile = open("realtest.out","w")
    
    caseNum = int(inFile.readline())
    
    for i in range(1,caseNum+1):        
        items = inFile.readline().replace("\n","").split(" ")
        N = int(items[0])
        dataList = []
        for j in range(1,len(items)):
            dataList.append(int(items[j]))

        dataList.sort()

        gapData = []
        for j in range(1,len(dataList)):
            gapData.append(dataList[j] - dataList[j-1])

        gapData.sort()
        
        theFactor = 0
        
        while len(gapData)>1:
            tmpFactor = gapData[0]
            
            if tmpFactor == 0:
                gapData.pop(0)
                continue
            
            elif tmpFactor == 1:
                testFactor = 1
                break
            
            else:
                for j in range(1,len(gapData)):
                    gapData[j] = gapData[j]%tmpFactor
                gapData.sort()
                
        if theFactor != 1:
            theFactor = gapData[0]       

        if theFactor == 1:
            outFile.write("Case #%d: 0\n" % (i,))
        else:
            outFile.write("Case #%d: %d\n" % (i, (theFactor - dataList[0])%theFactor))
        
        
        
    outFile.close()
    inFile.close()
