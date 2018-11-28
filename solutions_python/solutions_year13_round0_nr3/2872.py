import math

def isPalidrome(num):
    numStr = '%.12g' % num
    halfstrlen = len(numStr)/2
    i=0
    result = True
    while i<=halfstrlen:
        if numStr[i] != numStr[-1*i - 1]:
            result = False
            break
        i+=1
    return result

with open('FairSq-A-large-practice.in.txt') as f:
    #with open('TTTT-A-small-practice.in.txt') as f:
    content = f.read().splitlines()

numTests = int(content[0])
fileText = content[1:]
offset = 0
i=1
f = open ('FairSqSmalloutput.txt','w')
while i<=numTests:
    rangeLowerBound,rangeUpperBound = map(int,fileText[offset].split())
    sqrtLower = math.ceil(math.sqrt(rangeLowerBound))
    sqrtUpper = math.floor(math.sqrt(rangeUpperBound))
    print rangeLowerBound,rangeUpperBound,sqrtLower,sqrtUpper
    
    numFairSquare = 0
    
    currNum = sqrtLower
    while currNum <= sqrtUpper:
        if isPalidrome(currNum):
            currNumSq = math.pow(currNum,2)
            if isPalidrome(currNumSq):
                numFairSquare += 1
                print 'currNumSq: '+str(currNumSq)+' is palindrome: '+str(isPalidrome(currNumSq))
        currNum += 1
    
    print numFairSquare
    f.write('Case #'+str(i) + ': ' + str(numFairSquare)+'\n')
    i+=1
    offset += 1