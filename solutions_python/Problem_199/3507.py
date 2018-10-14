
# Name: Kavita Bhagavatula

import sys
import math

currCaseNum = 1

def main():
    global currCaseNum

    numCases = int(raw_input())
    for eachCase in range(0,numCases):
        global currCaseNum
        sys.stdout.write('Case #'+str(currCaseNum)+': ')
        wholeRaw = raw_input() # string int

        S,K = wholeRaw.split()
        process(S, int(K)) #strip off /n at end of string
        sys.stdout.write('\n')
        currCaseNum = currCaseNum +1

def process(rowOfPancakes, sizeOfFlipper):

    numPancakes = len(rowOfPancakes)
    pancakeIndex = 0
    numTimesFlipped = 0

    while pancakeIndex < numPancakes:
            if(rowOfPancakes[pancakeIndex]=='+'):
                pancakeIndex = pancakeIndex +1;
                continue
            else:
                if((numPancakes - pancakeIndex)<sizeOfFlipper):
                    sys.stdout.write("IMPOSSIBLE")
                    return
                else:
                    for p in range (pancakeIndex, pancakeIndex+sizeOfFlipper):
                        if(rowOfPancakes[p]=='+'):
                            rowOfPancakes = rowOfPancakes[:p] + '-'+rowOfPancakes[p+1:]
                        else:
                            rowOfPancakes = rowOfPancakes[:p] + '+'+rowOfPancakes[p+1:]
                    numTimesFlipped= numTimesFlipped+1
                    pancakeIndex = pancakeIndex +1

    sys.stdout.write(str(numTimesFlipped))



if __name__=='__main__':
    main()
