import os
import math

# Create Output file
f = open('dataOut.txt', "w")
f.close()

# Read Input file
f = open('A-large.in', "rb")
numOfTestCases = f.readline()

for i in range(0,int(numOfTestCases)):
    O = [1,0,'false']
    B = [1,0,'false']
    moves = f.readline()
    moves = moves.split()
    numOfButtons = moves[0]
    moves.remove(numOfButtons)
    numOfButtons = int(numOfButtons)

    nextColor = moves[0]
    seconds = 0
    
    try:
        indexOfO = moves.index("O")
        O[1] = moves[indexOfO + 1]
        O[1] = int(O[1])
    except ValueError:
        O[2]= 'true'
    try:
        indexOfB = moves.index("B")
        B[1] = moves[indexOfB + 1]
        B[1] = int(B[1])
    except ValueError:
        B[2] = 'true'
 
    while(numOfButtons != 0):
        if (B[2] == 'false'):
            if(B[0] == B[1] and nextColor == 'B'):
                numOfButtons = numOfButtons - 1
                moves.remove(moves[0])
                moves.remove(moves[0])
                try:
                    indexOfB = moves.index("B")
                    B[1] = moves[indexOfB + 1]
                    B[1] = int(B[1])
                except ValueError:
                    B[2]= 'true'
            elif (B[0] < B[1]):
                B[0] = B[0] + 1
            elif (B[0] > B[1]):
                B[0] = B[0] -1
        if (O[2] == 'false'):
            if(O[0] == O[1] and nextColor == 'O'):
                numOfButtons = numOfButtons - 1
                moves.remove(moves[0])
                moves.remove(moves[0])
                try:
                    indexOfO = moves.index("O")
                    O[1] = moves[indexOfO + 1]
                    O[1] = int(O[1])
                except ValueError:
                    O[2]= 'true'
            elif (O[0] < O[1]):
                O[0] = O[0] + 1
            elif (O[0] > O[1]):
                O[0] = O[0] -1
        seconds = seconds + 1
        if (numOfButtons != 0):
            nextColor = moves[0]
    
    g = open('dataOut.txt', "a")
    caseNum =  i + 1
    g.write("Case #" + repr(caseNum) + ": " + repr(seconds) + "\n")
    g.close()
f.close()
