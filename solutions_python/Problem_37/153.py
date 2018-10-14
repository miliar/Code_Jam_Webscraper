#!/usr/bin/env python
import sys
import pdb

def base10toN(num, n):
    s = ''
    while 1:
        remainder = num % n
        s = str(remainder) + s
        num = num / n
        if num == 0:
            break
    return s

def happytest(num, base, numlist=[]):
    if num == 1:
        return True
    else:
        if num in numlist:
            return False
        numlist.append(num)
        string = base10toN(num, base)
        next = sum([int(char)**2 for char in string])
        return happytest(next, base, numlist)

def printer(result, num):
    print 'Case #%d: %d' % (num, result)
    
f = open (sys.argv[1], 'r')
T = int(f.readline())

for i in range(T):
    bases = f.readline().split()
    inte = 2
    while True:
        happy = True
        for base in bases:
            happy &= happytest(inte, int(base), [])
        if happy:
            printer(inte, i + 1)
            break
        inte += 1

