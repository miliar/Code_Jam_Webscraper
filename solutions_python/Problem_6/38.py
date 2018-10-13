import string
from decimal import * 
import math
import sys

getcontext().prec = 85


def getline(f):
    return string.split(f.readline(), "\n")[0]
    
    
def factorial(num):
    fac = 1
    if num <= 1: 
        return 1
        
    for i in xrange(num, 1, -1):
        fac *= i
    return fac
    
    
    
def nCk(n, k):
    return (factorial(n)) / (factorial(k) * factorial(n-k))
    
infile = open("C-small-attempt4.in",'r')

numCases = int(getline(infile))

for case in xrange(numCases):
    num  = int(getline(infile))
    
    coeffecients = []
    threeArray = []
    fiveArray = []
    for i in xrange(num + 1):
        coeffecients.append(nCk(num, i))
        threeArray.append( 3 ** (num - i))
        fiveArray.append(5 ** (i / 2))
    
    sum = Decimal(0)
    rootCounter = 0
    for i in xrange(len(coeffecients)):
        if i % 2 == 1:
            rootCounter += coeffecients[i] * threeArray[i] * fiveArray[i]
        else:
            sum += coeffecients[i] * threeArray[i] * fiveArray[i]
       

    tempSum = Decimal(0)
    sum += Decimal(5).sqrt() * Decimal(rootCounter)
    
 
    

    res = int(sum) % 1000
    print "Case #%d:" % (case + 1),
    
    if res == 0:
        print "000"
    elif res < 10:
        print "00%1d" % res
    elif res < 100:
        print "0%2d" % res
    else:
        print "%3d" % res
        
        