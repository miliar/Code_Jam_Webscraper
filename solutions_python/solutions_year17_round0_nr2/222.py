from __future__ import print_function
import sys

# print to stderr for debugging
enableDebug = False 
def printe(*stuff):
    if enableDebug:
        print(*stuff, file=sys.stderr) 


# Open file for processing
filename = sys.argv[1]
inputFile = open(filename, 'r')
lines = [l.rstrip('\n') for l in inputFile]
linesIter = iter(lines)
nCases = int(linesIter.next())


# Process each case
for iCase in range(1,nCases+1):
    printe("\nProcessing case " + str(iCase))

    # Solve problem
    numStr = linesIter.next().strip()
    numArr = [int(x) for x in numStr]

    done = False
    while not done:
            
        if(len(numArr) == 1):
            done = True

        for iDig in range(len(numArr)-1):

            if(numArr[iDig] > numArr[iDig+1]):

                numArr[iDig] -= 1
                for jDig in range(iDig+1, len(numArr)):
                    numArr[jDig] = 9
    
                printe("Decresing to {}".format(int("".join([str(x) for x in numArr]))))
        
                break
            
            if(iDig == len(numArr) - 2):
                done = True

    val = int("".join([str(x) for x in numArr]))

    print("Case #{}: {}".format(iCase, val))
