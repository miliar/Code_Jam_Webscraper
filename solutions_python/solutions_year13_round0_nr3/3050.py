import math

##p = 10**14
##print math.sqrt(p)

def FairAndSquare(lB,uB):
    sqrtLB = (int)(math.sqrt(lB))
    sqrtUB = (int)(math.sqrt(uB))
    count = 0
    for i in range(sqrtLB,sqrtUB+1):
        if (isPalindrome(i) and isPalindrome(i*i) and i*i >= lB):
            #print i
            count = count + 1
    return count

def isPalindrome(aNumber):
    aList = convertToList(aNumber)
    left = 0
    right = len(aList) - 1
    while (left <= right):
        if (aList[left] != aList[right]):
            return False
        left += 1
        right -= 1
    return True

def convertToList(aNumber):
    aList = []
    temp = aNumber
    divisor = 10
    while (temp >= 10):
        #print 'temp: ', temp
        while(temp/divisor >= 10):
            divisor *= 10
            #print 'divisor: ', divisor
        aList.append(temp/divisor)
        temp = temp - (temp/divisor) * divisor
        if (temp < 10):
            while (divisor != 10):
                aList.append(0)
                divisor /= 10
        #print 'temp: ', temp
        divisor = 10
    aList.append(temp)
    return aList

#print convertToList(1423420)

myInput = open('input.txt','r')
myOutput = open('output.txt','w')

theLine = myInput.readline()
numOfRuns = int(theLine)
for i in range(numOfRuns):
    theLine = myInput.readline()
    arr = theLine.split()
    #print FairAndSquare(int(arr[0]),int(arr[1]))
    myOutput.write('Case #' + str(i+1) + ': ' + str(FairAndSquare(int(arr[0]),int(arr[1])))+'\n')
myInput.close()
myOutput.close()
#print FairAndSquare(1,10**14)
