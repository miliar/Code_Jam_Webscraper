# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 08:37:15 2014

@author: shek
"""

def solve(n):
    no=0
    for i in xrange(n[0]):
        for j in xrange(n[1]):
            if i&j in range(n[2]):
                no+=1
                
                    
    
    return no
if __name__ == "__main__":
    testcases = int(input())
     
    for caseNr in xrange(1, testcases+1):
        cipher =map(int, raw_input().split())
        print("Case #%i: %d" % (caseNr, solve(cipher)))