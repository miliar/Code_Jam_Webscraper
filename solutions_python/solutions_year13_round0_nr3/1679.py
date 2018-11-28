#!/usr/bin/python

import sys
import bisect
import math

good = []

def isPalindrome(n):
    mask = 1
    while(n / mask >= 10): mask *= 10
    
    start = 1
    while(start <= mask):
        if((n / start) % 10 != (n / mask) % 10):
            return False
        start *= 10;
        mask /= 10;
    
    return True

def isPalindromeStr(ss):
    s = str(ss)
    i = 0
    j = len(s)-1
    while(i <= j):
        if(s[i] != s[j]):
            return False
        i = i+1
        j = j-1
    return True

def snoob(v):
    t = (v | (v - 1)) + 1
    w = t | ((((t & -t) / (v & -v)) >> 1) - 1)
    return w

def binary(n):
    s = ''
    while n > 0:
        s = str(n % 2) + s
        n /= 2
    return s

def padToLength(s, length):
    while(len(s) < length):
        s = '0' + s
    return s

def processEven(s):
    n = int(s[::-1] + s)
    if(isPalindromeStr(n*n)):
        return process(n)
    return False

def processOdd(mid, s):
    n = int(s[::-1] + mid + s)
    if(isPalindromeStr(n*n)):
        return process(n)
    return False

def process(n):
    good.append(n)
    return True


# main code

for length in range(1, 50+1):
    if(length == 1):
        process(1)
        process(2)
        process(3)
    elif(length % 2 == 0):
        sublength = length / 2
        high = 2**(sublength-1)
        
        processEven(padToLength('1', sublength))
        for i in [1, 3, 7]:
            while(i < high):
                x = padToLength(binary(i), sublength-1)
                processEven(x + '1')
                i = snoob(i)
        
        processEven(padToLength('2', sublength))
    else:
        sublength = (length - 1) / 2
        high = 2**(sublength-1)
        
        for mid in ['0', '1', '2']:
            processOdd(mid, padToLength('1', sublength))
            for i in [1, 3, 7]:
                while(i < high):
                    x = padToLength(binary(i), sublength-1)
                    processOdd(mid, x + '1')
                    i = snoob(i)
            processOdd(mid, padToLength('2', sublength))

good.sort()

#for g in good:
#    print g

cases = int(sys.stdin.readline())
for i in range(cases):
    line = sys.stdin.readline()
    data = line.split()
    a = int(data[0])
    b = int(data[1])
    
    #print a,b,math.sqrt(a), math.sqrt(b)
    
    lower = bisect.bisect_left(good, math.sqrt(a))
    upper = bisect.bisect_right(good, math.sqrt(b))-1
    
    n = (upper - lower + 1)
    if(n < 0): n = 0
    print "Case #" + str(i+1) + ":", n
    
    #print lower, upper
    #print good
    
