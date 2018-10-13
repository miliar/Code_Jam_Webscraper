#CodeJam pancake problem
import csv

def findMaxStalls(arrayVals):
            maxVal = 0
            maxInd = 0
            for i in range(0,len(arrayVals)):
                if arrayVals[i] > maxVal:
                    maxVal = arrayVals[i]
                    maxInd = i
            return maxVal,maxInd

#import data from test file in the form [[[],[]],[[],[]].... with [[],[]] being one test case
with open('three-small.in') as csvfile:
    testCase = csv.reader(csvfile, delimiter = ' ', quotechar='|')
    rowNum = 0
    inputText = []
    
    #swapCount = []
    
    for row in testCase:
        #row = [str(i) for i in row]
        if rowNum == 0:
            numTestCases = int(row[0])
        else:
            inputText.append(row)
        rowNum = rowNum + 1

    #find the minimum time to eat pancakes
    for caseNum in range(0,numTestCases):
        NumStalls = []
        stallsInd = 0
        NumStalls.append(int(inputText[caseNum][0]))
        numPeople = int(inputText[caseNum][1])
        for i in range(0,numPeople):
            nextStallVal = findMaxStalls(NumStalls)
            numStallsVal = nextStallVal[0]-1
            numStallsInd = nextStallVal[1]
            #print numStallsVal,numStallsInd, NumStalls
            if numStallsVal % 2 == 1:
                stallsInd = stallsInd + 1
                maxStall = numStallsVal/2+1
                minStall = numStallsVal/2
                NumStalls[numStallsInd] = numStallsVal/2+1
                NumStalls.append(numStallsVal/2)
            else:
                stallsInd = stallsInd + 1
                maxStall = numStallsVal/2
                minStall = numStallsVal/2
                NumStalls[numStallsInd] = numStallsVal/2
                NumStalls.append(numStallsVal/2)
        #    else:
        #        rightNumStalls = rightNumStalls - 1
        #        if rightNumStalls % 2 == 1:
        #            maxStall = rightNumStalls/2+1
        #            minStall = rightNumStalls/2
        #            rightNumStalls = rightNumStalls/2+1
        #        else:
        #            maxStall = rightNumStalls/2
        #            minStall = rightNumStalls/2
        #            rightNumStalls = rightNumStalls/2
        
        print "Case #" + str(caseNum+1) + ": " + str(maxStall) + " " + str(minStall)
        
    
    