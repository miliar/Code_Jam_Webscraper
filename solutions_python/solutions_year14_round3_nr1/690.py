from fractions import gcd
from math import log
import sys

def parseFraction(strFrac):
    
    return (int(nums[0]),int(nums[1]))

def simplifyFrac(num,denom):
    g = gcd(num, denom)
    return (num/g,denom/g)

def log2(x):
    return log(x)/log(2)

def findMinDenom(num, denom):
    tmpExp = 2
    while num%(denom/tmpExp) >= denom/tmpExp:
        tmpExp = tmpExp + 1
    return denom/tmpExp

def decomposeFrac(num, denom):
    possibilites = [(num - 2*x,x) for x in range(1,denom/2)]
    possibilites = filter(lambda x: x[0] >= 0,possibilites)
    if len(possibilites) == 0:
        return ((-1,1),(-1,1))
    lastPossible = possibilites[-1]
    return ((lastPossible[0],denom), (lastPossible[1],denom/2))

#    minNum = num%minDenom
#    return ((minNum,denom),((minNum*minDenom-num)%minDenom,minDenom))



def findMaxElf(num,denom):
    num, denom = simplifyFrac(num, denom)
    if num < 0:
        return -1
    if denom == 1:
        if num == 1:
            return 0
        else:
            return 100
    if num == 1:
        return int(log2(denom))
    f1, f2 = decomposeFrac(num, denom)
    return min(findMaxElf(f1[0],f1[1]), findMaxElf(f2[0],f2[1]))

def findMaxElfStr(strFrac):
    nums =  strFrac.split("/")
    if len(nums) != 2:
        return "impossible"
    num, denom = int(nums[0]),int(nums[1])
#    print denom
    num, denom = simplifyFrac(num, denom)
    if int(log2(denom)) != log2(denom):
        return "impossible"
    res=  findMaxElf(num, denom)
    if res < 0:
        return "impossible"
    return res

def main(fileName):
    f = open(fileName, 'r+')
    lines = [line for line in f]
    nCases = int(lines[0])
    for i in range(1,nCases+1):
        print "Case #"+str(i)+": "+str(findMaxElfStr(lines[i]))

if __name__ == "__main__":
    main(sys.argv[1])
