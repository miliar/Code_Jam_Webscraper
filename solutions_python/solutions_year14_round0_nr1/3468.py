import sys,os
from sys import stdin

testCase = int(stdin.readline())


def process(testCase,firstAns, firstArrangement, secondAns, secondArrangment):
    firstSetAns = firstArrangement[firstAns-1];
    secondSetAns = secondArrangement[secondAns - 1]
    
    mutualElement = list(set(firstSetAns).intersection(set(secondSetAns)))
    testCase = int(testCase +1)
    if len(mutualElement) == 1:
        print "Case #%d: %s" % (testCase, mutualElement[0])
    elif len(mutualElement) > 1:
        print "Case #%d: Bad magician!" % testCase
    else:
        print "Case #%d: Volunteer cheated!"% testCase
#read test case
for i in range(0,testCase):
    #get 1st arrangement
    firstRow = int(stdin.readline())
    firstArrangement = []
    for j in range(0, 4):
        row = stdin.readline()
        firstArrangement.append(row.split())
    #get second arrangment
    secondRow = int(stdin.readline())
    secondArrangement = []
    for k in range(0,4):
        row2 = stdin.readline()
        secondArrangement.append(row2.split())
    process(i,firstRow,firstArrangement,secondRow,secondArrangement)
    