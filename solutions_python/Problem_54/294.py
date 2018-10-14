#!/usr/local/bin/python3.0

import sys
import fractions
import functools

firstLine = next(sys.stdin)

numbers = [ int(s) for s in firstLine.split() ]
if len(numbers) != 1:
    sys.exit('Invalid input')

C = numbers[0]
if C < 0:
    sys.exit('Invalid input')

for caseNumber in range(1, C+1):
    thisLine = next(sys.stdin)

    numbers = [ int(s) for s in thisLine.split() ]
    if len(numbers) == 0:
        sys.exit('Invalid input')
    N = numbers[0]
    if N < 2:
        sys.exit('Invalid input')

    tArray = numbers[1:]
    if len(tArray) != N:
        sys.exit('Invalid input')
    if not all(t > 0 for t in tArray):
        sys.exit('Invalid input')
    
    firstT = tArray[0]
    differences = [ abs(t - firstT) for t in tArray[1:] ]
    T = functools.reduce(fractions.gcd, differences)
    
    result = (-firstT) % T
    
    print( 'Case #{0}: {1}'.format(caseNumber, result) )
