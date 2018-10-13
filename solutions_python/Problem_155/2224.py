#CodeJam Practice
import csv
import numpy
with open('A-large.in') as csvfile:
    testCase = csv.reader(csvfile, delimiter = ' ', quotechar='|')
    rowNum = 0
    inputText = []
    
    for row in testCase:
        inputText.append(row)
        rowNum = rowNum + 1

    for caseNum in range(1,int(inputText[0][0])+1):
        if int(inputText[caseNum][0]) == 0:
            print "Case #" + str(caseNum) + ": " + "0"
        else:
            numFriend = 0
            numCrowd = 0

            if int(inputText[caseNum][0]) == 0:
                numFriend = 1
            else:
                numCrowd = int(inputText[caseNum][1][0])

            for shyNum in range(1,int(inputText[caseNum][0])+1):
                tempNum = 0
                if numCrowd < shyNum:
                    if int(inputText[caseNum][1][shyNum]) != 0:
                        tempNum = shyNum - numCrowd
                        numFriend = numFriend + tempNum

                numCrowd = numCrowd + int(inputText[caseNum][1][shyNum]) + tempNum
            print "Case #" + str(caseNum) + ": " + str(numFriend)
                
