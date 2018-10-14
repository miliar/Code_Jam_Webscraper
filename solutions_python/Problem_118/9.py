#!/usr/bin/python3.2
# I found all the square and fair numbers from 0 to 10^100 and cached them. The cache script runs in ~3 minutes.

import math as m
N = 100

def isPalindrome(x): return str(x) == str(x)[::-1]

def twosOdds(x):
    rList = []
    k = 0
    while 1:
        for i in ['0','1']:
            c = int('2' + '0'*k + i + '0'*k + '2')
            c2 = c*c
            if c2 > x:
                return rList
            else:
                rList.append(c2)
        k += 1

def twosEvens(x):
    rList = []
    k = 0
    while 1:
        c = int('2' + '0'*k + '2')
        c2 = c*c
        if c2 > x:
            return rList
        else:
            rList.append(c2)
            k += 2


rList = [0,1,4,9] + twosOdds(10**N) + twosEvens(10**N)
i = 1
MAX = 10**(N//2)
while 1:
    s = bin(i)[2:]
    c = int(s + s[::-1])
    if c > MAX:
        break
    else:
        if isPalindrome(c**2):
            rList.append(c**2)

            c = int(s + '0' + s[::-1])
            if isPalindrome(c**2):
                rList.append(c**2)

                c = int(s + '1' + s[::-1])
                rList.append(c**2)

                c = int(s + '2' + s[::-1])
                if isPalindrome(c**2):
                    rList.append(c**2)

        i += 1

rList.sort()
print(len(rList))
for elem in rList:
    print(elem)