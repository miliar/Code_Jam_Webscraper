#!/usr/local/bin/python3.0

# Given the state of the N snappers, convert it to an N-digit binary number
# by ON=1 and OFF=0, and let the snapper connected to the socket be the least
# significant digit.
# Then each snap increase the number by one, modulo 2**N.

import sys

firstLine = next(sys.stdin)

numbers = [ int(s) for s in firstLine.split() ]
if len(numbers) != 1:
    sys.exit('Syntax Error')

T = numbers[0]

for caseNumber in range(1, T+1):
    thisLine = next(sys.stdin)

    numbers = [ int(s) for s in thisLine.split() ]
    if len(numbers) != 2:
        sys.exit('Syntax Error')

    N = numbers[0]
    K = numbers[1]
    
    result = (K+1) % (2**N) == 0
    
    print( 'Case #{0}: {1}'.format(caseNumber, 'ON' if result else 'OFF') )

