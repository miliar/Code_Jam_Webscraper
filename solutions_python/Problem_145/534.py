# -*- coding: utf-8 -*-
"""
Created on Sun May 11 10:20:26 2014

@author: Melissa
"""
from __future__ import division
#import math
from fractions import gcd

f = open("A-large.in")
answer = open("A-large-answer.txt", 'w')

def powerof2(p):
    return 2**p

def getpowers2(p):
    return map(powerof2, range(1, p+1))
    
denall = getpowers2(40) # denominators allowed

# get all prime numbers smaller than sqrt(denall[-1])
#m = int(math.sqrt(denall[-1]))

#def getprimes(m):
#    primes = [2]
#    for nr in xrange(3, m+1):
#        isprime = True
#        for prime in primes:
#            if prime <= math.sqrt(nr):
#                r = nr % prime # work out remainder
#                if r == 0: # if it is divisible
#                    isprime = False # it is not a prime
#                    break # carry on with next number
#            else:
#                break
#        if isprime == True:
#            primes.append(nr)
#    
#    return primes
#
#primelist = getprimes(m)

T = int(f.readline())

for i in xrange(T):
    line = f.readline()
    [P, Q] = line.split("/")
    [P, Q] = map(int, [P, Q])
    
    # take out all common factors of P and Q
    GCD = gcd(P, Q)
    while gcd(P, Q) > 1:
        P /= GCD
        Q /= GCD
        GCD = gcd(P, Q)
    
    # logic
    # if the denominator is not possible
    if Q not in denall:
        result = "impossible"
    # if the fraction is too small
    elif (P / Q) < (1 / denall[-1]):
        result = "impossible"
    else:
        x = P / Q
        gen = 1
        while x < 0.5:
            gen += 1
            x *= 2
        result = gen

    answer.write("Case #%d: %s\n" % (i+1, result))
    
f.close()
answer.close()