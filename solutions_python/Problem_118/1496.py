from math import log
from math import log10
from math import atan, pi

def intToList(n):
    maxDigitSeat = int(log10(n))
    list = []
    for i in xrange(0,maxDigitSeat+1):
        list.append(int(n/pow(10,(maxDigitSeat-i)))%10)
    return list

def listToInt(list):
    l = len(list)
    num = 0
    for i in xrange(l):
        num += list[i]*pow(10,(l-1-i))
    return num

def isPalindrome(n):
    base = 10
    length = int(log10(n))
    for i in xrange(int((length+1)/2)):
        if ((n/pow(base,i))%base) != ((n/pow(base,length-i))%base):
            return False
    return True



import copy


def digitsToNum(digits,lenNum):
    if lenNum % 2 == 0:
        return sum([digits[i]*10**i for i in xrange(len(digits))]) + sum([digits[i]*10**(lenNum-i) for i in xrange(len(digits)-1)])
    else:
        return sum([digits[i]*10**i for i in xrange(len(digits))]) + sum([digits[i]*10**(lenNum-i) for i in xrange(len(digits))])

def shouldContinue(palDigits,n):
    if len(palDigits) <= 11:
        if len(palDigits) > 3:
            c = [0]*(n+1)
            for i in xrange(len(c)):
                c[i] = sum(palDigits[min(k,n-k)]*palDigits[min(i-k,n-i+k)] for k in xrange(i+1))
            num = digitsToNum(c, n*2)
            if int(log10(num)) == n*2:
                p = 10**(n*2-len(palDigits)+4) 
                if isPalindrome((num/p)*p + (num % 10**(len(palDigits)-3))):
                    return True
            elif int(log10(num)) == (n*2)+1:
                p = 10**(n*2-len(palDigits)+4) 
                if isPalindrome((num/p)*p + (num % 10**(len(palDigits)-2))):
                    return True
            else:
                assert False

    elif len(palDigits) >= 12:
        c = [0]*(n+1)
        for i in xrange(len(c)):
            c[i] = sum(palDigits[min(k,n-k)]*palDigits[min(i-k,n-i+k)] for k in xrange(i+1))
        num = digitsToNum(c, n*2)
        if int(log10(num)) == n*2:
            p = 10**(n*2-len(palDigits)+5)
            if isPalindrome((num/p)*p + (num % 10**(len(palDigits)-4))):
                return True
            #print (num/p)*p + (num % 10**(len(palDigits)-4))
        elif int(log10(num)) == (n*2)+1:
            p = 10**(n*2-len(palDigits)+5) 
            if isPalindrome((num/p)*p + (num % 10**(len(palDigits)-3))):
                return True
        else:
            assert False
    else:
        return True

#shouldContinue([1,1,2,3,4,5,6,7,8,9,1,2], 23)
#print digitsToNum([1], 0)
    
count = 0

def genFairSquare(palDigits,n,lb,ub):
    global count
    num = digitsToNum(palDigits,n)
  #  print num
    if num < lb:
      #  print "a"
        if n % 2 == 0:
            genFairSquare(palDigits,n+1,lb,ub)
        else:
            for i in xrange(10):
                newPD = copy.copy(palDigits)
                newPD.append(i)
                if shouldContinue(newPD, n+1): 
                    genFairSquare(newPD, n+1, lb, ub)
    #else if number is over or equal lowerbound:
    else:
        #if number is above upper bound: 
        if num > ub:
    #        print "c"
            return
        else:
     #       print "b"
            #check fair square stuff
            if (isPalindrome(num) and isPalindrome(num*num)):
                count += 1
            if n % 2 == 0:
                genFairSquare(palDigits,n+1,lb,ub)
            else:
                for i in xrange(10):
                    newPD = copy.copy(palDigits)
                    newPD.append(i)
                    if shouldContinue(newPD, n+1): 
                        genFairSquare(newPD, n+1, lb, ub)


import sys

from math import ceil,floor,sqrt

inp = sys.stdin

T = int(inp.readline())

for testCase in xrange(1,T+1):
    count = 0
    A,B = map(lambda x: int(x), inp.readline().split(" "))
    for i in xrange(1,10):
        genFairSquare([i],0,int(ceil(sqrt(A))),int(floor(sqrt(B))))
    print "Case #{}: {}".format(testCase, count)
