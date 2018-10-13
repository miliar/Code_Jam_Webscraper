import sys

DEBUG = False
import re

def solveCase(intString):
    intString = intString.strip()
    
    if len(intString)==1:
        return intString
    intNumArray = [int(char) for char in intString]
    if DEBUG:
        print(intNumArray)

    outIntArray = list()

    for i in range( len(intNumArray)-1 ):
        currNum = intNumArray[i]
        nextNum = intNumArray[i+1]

        if DEBUG:
            print("i=%s, Checking %s followed by %s" %(i,currNum,nextNum))

        if nextNum >= currNum: #Therefor localy tidy
            #Can output the current number
            outIntArray.append(currNum)

            #If at the end, we should output the last number also         
            if i == len(intNumArray)-2:
                outIntArray.append(nextNum)

        else: # nextNum < currNum:
            #Needs reducing at i
            outIntArray.append(currNum) #stick it on and then we reduce
            if DEBUG:
                print("Ready to reduce at %s"%(i,))
                
            nNinesToPrint = len(intNumArray) - i - 1#TODO: Check

            hasSuccessfullyReduced = False
            while not hasSuccessfullyReduced:
                if DEBUG:
                    print("Checking reduction: %s" % (outIntArray,))
                canReduce = (
                    len(outIntArray) == 1 or \
                    outIntArray[-1]-1 >= outIntArray[-2]
                )
                if DEBUG:
                    print("Checking reduction: Result %s" % canReduce)
                
                if not canReduce:
                    outIntArray.pop()
                    nNinesToPrint += 1
                    continue
                    
                else:
                    outIntArray[-1] -= 1

                    for n in range(nNinesToPrint):
                        outIntArray.append(9)
                    hasSuccessfullyReduced = True
                    break
            if hasSuccessfullyReduced:
                break #Again out of the looping through numbers

                
    nonZeroOutputArray = list()
    nonZeroFound = False
    for i in range( len(outIntArray) ):
        currNum = outIntArray[i]
        if currNum != 0:
            nonZeroFound = True

        if nonZeroFound:
            nonZeroOutputArray.append(currNum)
    #Done
    return(''.join([str(d) for d in nonZeroOutputArray]))

        
    
    

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: tidy.py inputfile outputfile", file=sys.stderr)
        sys.exit()

    with open(sys.argv[1], 'r') as fin:
        nCases = int(fin.readline().strip())

        with open(sys.argv[2], 'w') as fout:
            for caseNumMinusOne in range(nCases):
                line = fin.readline().strip()

                print(
                    'Case #%s: %s' % (
                        caseNumMinusOne + 1,
                        solveCase(line),
                    ),
                    file = fout,
                )
                



sys.stdin
