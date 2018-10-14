'''
Created on Apr 30, 2011

@author: Marius Dorin Moraru
'''
import math

#filename without extension
#fileName = raw_input("Enter a name:")
fileName = "c:/learn/a"

inFile = open(fileName + ".in", "rU")
outFile = open(fileName + ".out", "w")

nrOfTestCases = long(inFile.readline());        
print "nrOfTestCases " + str(nrOfTestCases)









def readTestCase():   
    n = int(inFile.readline().replace("\n","").replace("\r",""))
    v = inFile.readline().replace("\n","").replace("\r","").split(" ")
    for i in xrange(n):
        v[i] = int(v[i])
    return n, v

#resolve testCase
def resolve(data):
#    print dummySum(5, 4)
#    print dummySum(7, 9)
#    print dummySum(50, 10)
    n = data[0]
    v = data[1]
    p=[]
    for i in xrange(n):
        p.append(toBinary(v[i]))
    
    x=-1;
    maxSum=0
    hasSolution = 0
    solution=""
    
    while (x < n):
        x = x + 1
        backtracking = toBinary(int(math.pow(2, x)));
        while len(backtracking) < n:
            backtracking = "0" + backtracking
#        print backtracking

        
        dummySumA=""
        dummySumB=""
        sumA=0
        sumB=0
        for i in xrange(n):
            if backtracking[i] == '0':
                dummySumA = dummySum(dummySumA, p[i])
                sumA = sumA + v[i]
            else:
                dummySumB = dummySum(dummySumB, p[i])
                sumB = sumB + v[i]
        if dummySumA == dummySumB:
            hasSolution = 1
            if (maxSum < sumA):
                maxSum = sumA
                solution = backtracking
            if (maxSum < sumB):
                maxSum = sumB
                solution = backtracking
            #print "hasSol: ", hasSolution, "maxSum: ", maxSum
    #end while

    v = data[1]
    v.sort()
    v = v[::-1]
#    print v    
    if hasSolution == 1:
        return maxSum
    return "NO"


def dummySum(a, b):
#    a = toBinary(a)
#    b = toBinary(b)
    s="";
    maxLen = max(len(a), len(b))
    while len(a) < maxLen:
        a = "0" + a;
    while len(b) < maxLen:
        b = "0" + b;
    for i in xrange(maxLen):
        if (a[i] == b[i]):
            s = s + '0'
        else:
            s = s + "1"
    while len(s)>0 and s[0]=='0':
        s = s[1:]
    
    return s

def fromBinary(s):
    n=0;
    p=1;
    s = s[::-1]
    for i in xrange(len(s)):
        if (s[i]=='1'):
            n = n + p;
        p = p * 2;        
    return n;
def toBinary(n):
    '''convert denary integer n to binary string bStr'''
    bStr = ''
    if n < 0:  raise ValueError, "must be a positive integer"
    if n == 0: return '0'
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n >> 1
    return bStr





for i in range(nrOfTestCases):
    print "resolving testCase " + str(i + 1)
    out = resolve(readTestCase())
    outFile.writelines("Case #" + str(i + 1)+": " + str(out) + "\n")
outFile.close()


    
        