# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 14:16:00 2017

@author: elon
"""

cases = int(raw_input())
for i in xrange(1, cases+1):
    maxNum = raw_input()
    prevNum = 0
    samePrevNum = 0
    anw = maxNum
    for j in xrange(0, len(maxNum)):
        cur = int(maxNum[j])
        if cur > prevNum:
            prevNum = cur
            samePrevNum = 0
        elif cur == prevNum:
            samePrevNum += 1
        else:
            if samePrevNum > 0:
                anw = maxNum[:j-samePrevNum-1]+str(prevNum-1)+"9" * len(maxNum[j-samePrevNum:])
            else:
                anw = maxNum[:j-1]+str(prevNum-1)+ "9" * len(maxNum[j:])
            break
    
    while anw[0] == "0":
        anw = anw[1:]
    print "Case #"+str(i)+": "+anw