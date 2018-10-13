# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 17:23:02 2013

@author: Tautvydas
"""

import math

def digits(number):
    digits = []
    while number > 0:
        d = number%10
        number = (number - d)/10
        digits.append(d)
    return digits

def isPalindromic(number):
    dig = digits(number)
    n = 0
    for i in range(len(dig)):
        n = n*10 + dig[i]
    if number == n:
        return True
    return False
    


class Cache:
    
    cache = []
    cFrom = 0
    cTo = 0
    
    def __init__(self, upto):
        for n in xrange(1, upto+1):
            if isPalindromic(n):
                if isPalindromic(n*n):
                    self.cache.append(n)
        self.cache.sort()
        print "cache size:", len(self.cache)
    
    def calculate(self, nuo, iki):
        count = 0
        for x in self.cache:
            if x >= nuo:
                if x <= iki:
                    count += 1
                else: break
        return count;
        
    
        

cache = Cache(10000000)
filename = 'C-large-1'

with open(filename + '.in', 'r+') as filein:
    casesCount = int(filein.readline())
    
    
    with open(filename + '.out', 'w') as fileout:
        
        for caseNr in range(1, casesCount + 1):
            answer = 0
            nuo2, iki2 = (int(x) for x in filein.readline().split())
            nuo = int(math.ceil(math.sqrt(nuo2)))
            iki = int(math.floor(math.sqrt(iki2)))
            #print 'from',nuo2, nuo
            #print 'to', iki2, iki
            
            answer = cache.calculate(nuo, iki)
                        
            
            print "Case #", caseNr, " - ", answer
            
            fileout.write("Case #%s: " %caseNr)
            fileout.write('%s\n' %answer)