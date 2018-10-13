# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 11:47:53 2017

@author: kprashan
"""
inStr = '-+'
outStr = '+-'
trantab = str.maketrans(inStr,outStr)
def getHappyFace(panStr,targetStr,k):
    currPanStr = panStr
    count = 0
#    if (currPanStr == targetStr):
#        return 0
    for  i in range(len(panStr)-k+1):
        if currPanStr[i] == '-' :
#            print('Flipping currPanstr[{}:{}]{}:'.format(i,i+k,currPanStr[i:i+k]))
            currPanStr = currPanStr[0:i] + currPanStr[i:i+k].translate(trantab) + currPanStr[i+k:]
            count += 1
        else : 
            continue
    if (currPanStr == targetStr):
        return count
    else :
        return 'IMPOSSIBLE'

file_in = "A-large.in"
#file_in = "A-small.in.txt"
array = []
with open(file_in) as f :
    for line in f :
        array.append(line.rstrip())
        
#for line in array :
#    print(line)        
n = int(array[0])
fileOut = open("A-large.out","w")
for i in range(n):
    panStr,k = array[i+1].rstrip().split()
    node = [panStr,0]
    targetStr = '+'*len(panStr)
#    print("Case #{}: {}".format(i+1, getHappyFace(panStr,targetStr,int(k))))
    print("Case #{}: {}".format(i+1, getHappyFace(panStr,targetStr,int(k))),file=fileOut)
#    getHappyFace(panStr,targetStr,k)
fileOut.close()
    

      