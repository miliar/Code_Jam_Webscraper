# -*- coding: utf-8 -*-
"""


@author: showshow
"""
from math import pi
import heapq

fileName = "A-large"
finName  = fileName+".in"
foutName = fileName+"-ans.txt"

with open(finName, "r") as f:
    filein = f.readlines()

fileout = open(foutName, "w")

#######################################################

totalCaseNum = filein[0]

hCnt = 0
cnt = 0
readNK = 1
cakeList = []
maxoneCakeTotal =0
for line in filein[1:]:
    if readNK == 1:
        N, K = [int(s) for s in line.split(" ")]
        readNK = 0
    else:
        R, H = [int(s) for s in line.split(" ")]
        face = pi*R*R
        side = 2*pi*R*H
        oneCakeTotal = face+side
        cakeList.append([face, side, oneCakeTotal, R, H])
        maxoneCakeTotal = max(maxoneCakeTotal, oneCakeTotal)
        hCnt += 1  
        
        
        if hCnt == N:
            maxFace = 0
            for item in cakeList:
                maxR = item[3]
                ansT = pi*maxR*maxR
                ansT+= 2*pi*maxR*item[4]
                #print("ansT", ansT)
                cakeLists = cakeList[:]
                cakeLists.remove(item)
                #print(cakeList)
                #print(cakeLists)
                cList = heapq.nlargest(N-1, cakeLists, key=lambda x: x[1])
                #print("cList", cList)
                sideSum = 0
                addCnt = 0
                for i in cList:
                    if addCnt == K-1:
                        #print ('x')
                        break
                    if i[3]>maxR:
                        #print ('xx', i[3], maxR)
                        continue
                    else:
                        #print ('xxx')
                        sideSum+=i[1]
                        addCnt+=1
                    
                #print('addCnt',addCnt)
                if addCnt == K-1:
                    ansT+=sideSum
                else:
                    continue

                maxFace = max(maxFace, ansT)
                #print("maxFace", maxFace)
                          
            cnt += 1
            print ("Case #{}: {:.9f}".format(cnt, maxFace))
            fileout.write("Case #{}: {:.9f}\n".format(cnt, maxFace))
            maxoneCakeTotal = 0
            readNK = 1
            hCnt = 0
            cakeList  =  []

    #print(D,N,K,S)
    
fileout.close()
