#!/usr/bin/env python
import sys

Jam = 'welcome to code jam'

f = open('input3.txt')

N = int(f.readline())

for case in range(1, N+1):
    
    text = f.readline().rstrip('\n')
    #text = text.lower()
    
    phraseMap = []
    weights = []
    for l in range(len(Jam)):
        
        letterMap = []
        weightsColumn = []
        
        for pos in range(len(text)):
            if Jam[l] == text[pos]:
                letterMap.append(pos)
                weightsColumn.append(0)
                
        phraseMap.append(letterMap)
        weights.append(weightsColumn)
        if l == len(Jam) - 1:
            for i in range(len(weightsColumn)):
                weights[l][i] = 1 
            
    l = len(Jam) - 1
    while l > 0:
        for gathereeIndex in range(len(phraseMap[l-1])):
            for groupIndex in range(len(phraseMap[l])):
                if phraseMap[l][groupIndex] > phraseMap[l-1][gathereeIndex]:
                        weights[l-1][gathereeIndex] += weights[l][groupIndex]
        l -= 1
    
    print 'Case #' + str(case) + ': ',  str(sum(weights[0])+10000)[-4:]
        
f.close()
            
            












