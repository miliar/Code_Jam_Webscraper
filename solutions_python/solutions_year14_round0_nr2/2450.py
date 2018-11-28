# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 15:13:35 2014

@author: shek
"""
def solve(cipher):
    Cost=cipher[0]
    F=cipher[1]
    X=cipher[2]
    i=2.0
    leastTime=X/i
    totalTime=0.0
    timeTOc=0.0
    while(1):
        timeTOc=timeTOc + Cost/i
        i=i+F
        timeTOx=X/i
        totalTime=timeTOc + timeTOx
        if(totalTime<leastTime):
            leastTime=totalTime
        else:
            return leastTime
        
    return 1

if __name__ == "__main__":
    testcases = int(input())
     
    for caseNr in xrange(1, testcases+1):
        cipher = map(float, raw_input().split())
        print("Case #%i: %0.7f" % (caseNr, solve(cipher)))