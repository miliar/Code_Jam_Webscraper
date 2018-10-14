#!/usr/bin/env python
import math

T = int(raw_input())            #number of real tests

for t in range(1,T+1):
    A,B = raw_input().split()             #read a test case, splot out the needed numbers
    A = int(A)
    B = int(B)
    myxi = B + 1                #to abort the next loop if no squares found
    for z in range(A,B+1):
        x = math.sqrt(z)         #find a perfect root between A and B
        myxi = int(x + .5)
        if (myxi**2) >= A:
            break       #we found our starting point
        
    NumDrones = 0           #count the palindromes
    while B >= myxi**2:
        #test whther the base is a square
        newst = ""
        st = "{0}".format(myxi)
        for i in range(1,len(st)+1):
            newst = newst + st[-i]
        if newst == st:
            newst = ""
            st = "{0}".format(myxi**2)
            for i in range(1,len(st)+1):
                newst = newst + st[-i]
            if newst == st:
                NumDrones = NumDrones + 1
                #print "Palindrome?" ,st, myxi,"start=",A,"end=",B
        myxi = myxi +1
            
    #print "Case #%d: %d start=%d end=%d"%(t,NumDrones,A,B)
    print "Case #%d: %d"%(t,NumDrones)
    
    