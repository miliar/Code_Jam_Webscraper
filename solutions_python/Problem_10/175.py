# -*- coding: cp949 -*-
import math
fin = open('D:/Users/정강식/Documents/A-large.in')
fout = open('D:/Users/정강식/Documents/A-large.out', 'w')
numCase = int(fin.readline())
print 'num of case: ' + str(numCase)
for i in range(numCase):
    print 'Case #' + str(i+1)
    nums = fin.readline().split()
    maxLettersOnKey = int(nums[0])
    numKey = int(nums[1])
    numLetter = int(nums[2])
    #print maxLettersOnKey, numKey, numLetter
    letterFreq = []
    letterFreqStr = fin.readline().split(' ')
    for j in range(numLetter):
        letterFreq.append(int(letterFreqStr[j]))
    letterFreq.sort()
    letterFreq.reverse()
    #print 'letterFreq: ', letterFreq
    keyPressed = 0
    for j in range(1, math.ceil(float(numLetter)/numKey)+1):
        curFreq = letterFreq[0:numKey]
        #print 'pressing ', j, curFreq
        letterFreq = letterFreq[numKey:]
        for k in range(numKey):
            if k >= len(curFreq):
                break
            keyPressed += j * curFreq[k]
    #print keyPressed
    print 'Case #' + str(i+1) + ': ' + str(keyPressed)
    fout.write('Case #' + str(i+1) + ': ' + str(keyPressed) + '\n')
fout.close()
    
    
            
