#/usr/bin/python3

import sys
import pyprimes
import time
        
inputFile = open("input", "r")
outputFile = open("output", "w")
caseNb = 1

inputLine = inputFile.readline()
T = int(inputLine)
inputLine = inputFile.readline()
N = int(inputLine.split(' ')[0])
J = int(inputLine.split(' ')[1])
maxProofTurn = 100

outputFile.write("Case #1:\n");

result = 0

x = '1'
for i in range(N-2):
    x += '0'
x += '1'

while result < J :
    isJamCoin = True
    
    for base in range(2,11) :
            isJamCoin = isJamCoin and not(pyprimes.isprime(int(x,base)))
            
    if isJamCoin :
        turn2Proof = 0
        proof = []
        for base in range(2,11) :
            y = int(x,base)
            
            primesGenerator = pyprimes.primes()
            p = 2
            turn2Proof = 0
            while y % p > 0 and turn2Proof < maxProofTurn :
                turn2Proof += 1
                p = next(primesGenerator)

            if turn2Proof == maxProofTurn :
                isJamCoin = False
                
            proof.append(p)

        if isJamCoin :
            resultStr = ''+str(x)
            for z in proof:
                resultStr += ' '+str(z)
            outputFile.write(resultStr+"\n")
            result += 1
        else :
            print("too long to proof {0}".format(x), file=sys.stderr)

    pos = -2
    r=1
    while r == 1 :
        if x[pos] == '0' :
            x = x[:pos]+'1'+x[pos+1:]
            r=0
        else:
            x = x[:pos]+'0'+x[pos+1:]
        pos -= 1

inputFile.close()
outputFile.close()
