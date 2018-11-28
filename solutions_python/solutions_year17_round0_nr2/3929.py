#!/usr/bin/env python
# -*- coding: utf-8 -*-
#sabu
def tidy(x,y):
    if len(x)<2:
        return x+y
    si = 0
    for i in range(1,len(x)):
        if x[i-1]>x[i]:
            si = i
            break
    if (si>0):
        return tidy(str(int(x[:si])-1),'9'*(len(y)+len(x)-si))
    return x+y

if __name__ == "__main__":
    testcases = int(input())                    #get number of tests
    ntos = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    for caseNr in range(1, testcases+1):        #for each testcase
        s = input().strip()
        t = str(int(tidy(s,'')))
        print("Case #%i: %s" % (caseNr, t))
        
        