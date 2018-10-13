#!/usr/bin/env python

import os
import sys
import math

if len(sys.argv) < 2:
    sys.exit(0)
    
fin = open(sys.argv[1], "rb")
lines = fin.readlines()
fin.close()

numtest = int(lines[0])

def CheckSqrt(num):
    sq = math.sqrt(num)
    if sq % 1 == 0:
        return True
    return False

def CheckPalin(num, sub):
    numstr = str(int(num))
        
    if len(numstr) % 2 == 0:
        pad = 0
    else:
        pad = 1
       
    cheklen = len(numstr) / 2
    #print "checking: %d, %d" % (num, cheklen)
    chekstr = ""
    for i in range(cheklen):
        chekstr += numstr[i]
    
    chekstr = chekstr[::-1]
 
    bBroke = False
    for i in range(cheklen):
        #print "chekstr[i] = %s vs %s numstr[part2]" % (chekstr[i], numstr[cheklen+pad+i])
        if chekstr[i] != numstr[cheklen+pad+i]:
            return False
    if sub == False:
        #print "It is palindromic: %d, checking for sqrtd" % (num)
        pass
    else:
        #print "it is palin (sub) true"
        return True
        
    sq = math.sqrt(num)
    #print "sqrt: %f" % sq
    if sq % 1 == 0 and CheckPalin(sq, True):
        #print "FOUND IT: %d" % num
        return True
        
    return False
        
def CheckPalinRange(beg, end):
    ptr = int(beg)
    end = int(end)
    palins = []
    while ptr <= end:
        if CheckPalin(ptr, False):
            palins.append(ptr)
        ptr += 1
    return len(palins)

ptr = 1
tests = []
for i in range(numtest):
    line = lines[1+i].strip()
    twonums = line.split()
    beg = twonums[0]
    end = twonums[1]
    
    count = CheckPalinRange(beg, end)
    print "Case #%d: %d" % (i+1, count)
