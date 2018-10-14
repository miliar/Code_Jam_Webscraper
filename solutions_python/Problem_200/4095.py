
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
        T= int(raw_input())
        process(T)
        sys.stdout.write('\n')
        currCaseNum = currCaseNum +1

def process(lastNumCounted):

    for eachNum in range(lastNumCounted, 0, -1):
        tidyNum=True
        origNum =eachNum
        rightMostDigit = eachNum % 10
        while eachNum:
            eachNum //=10
            nextLeftDigit = eachNum % 10
            if (nextLeftDigit > rightMostDigit):
                tidyNum=False
                break
            rightMostDigit = nextLeftDigit

        if(tidyNum == True):
            sys.stdout.write(str(origNum))
            break



if __name__=='__main__':
    main()
