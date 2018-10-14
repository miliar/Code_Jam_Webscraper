import os
import sys
import string 


def calcTime( cost, addRate, target ): 
    curRate = 2.0
    
    accumTime = 0 

    curEstimate = target / curRate 

    decisionPoint = cost / curRate
    nextRate = curRate + addRate 
    nextEstimate = accumTime + decisionPoint + ( target / nextRate )
    
    while curEstimate > nextEstimate:  
        curEstimate = nextEstimate 
        curRate = nextRate 
        accumTime = accumTime + decisionPoint
        decisionPoint = cost / curRate
        nextRate = curRate + addRate 
        nextEstimate = accumTime + decisionPoint + ( target / nextRate )
    
         
    return curEstimate

        
    

tests = [ [30.0, 1.0, 2.0],
          [30.0, 2.0, 100.0],
          [30.50000, 3.14159, 1999.19990],
          [500.0, 4.0, 2000.0] ]

v = sys.stdin.readline()
i = 1

for line in sys.stdin: 
    w = [ float(x) for x in string.split( line )] 
    print ( "Case #{0}: {1}".format( i , calcTime( *w ) ) ) 
    i = i + 1

#for a in tests:
#    print calcTime( *a)