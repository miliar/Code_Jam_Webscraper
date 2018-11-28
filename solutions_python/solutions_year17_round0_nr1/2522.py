import sys
import re

T = 0   #Number of tests
T_Count = 0
S = []  #Input strings
FlipperSize = []
line = ""
S_numberic = {}
i = 0
caseCount = 0
inputFile = ""
outputFile = ""
reportString = ""
Report = []
countFlag = False

inputFile = sys.argv[1]
outputFile = sys.argv[2]

print "inputFile: " + inputFile
print "outputFile: " + outputFile

# Read in input file
fp = open(inputFile, 'r')

try:
    for line in fp:
        if (countFlag == False):
            countFlag = True
            T = int(line)
            continue

        line = line.strip()
        tempVar = line.split()
        S.append(tempVar[0])
        FlipperSize.append(tempVar[1])

finally:
    fp.close()

print T
print S
print FlipperSize

while (T_Count < T):
    S_numberic = list(S[T_Count])
    i = 0
    caseCount = 0
    flipCount = 0

    print "length: " + str(len(S_numberic)) + "    " + str(FlipperSize[T_Count])
    loopCount1 = int(len(S_numberic)) - int(FlipperSize[T_Count]) + 1
    while (i < loopCount1):
        if (S_numberic[i] == '-'):
            flipCount = flipCount + 1
            j = 0
            loopCount2 = int(FlipperSize[T_Count])
            while(j < loopCount2):
                if (S_numberic[i+j] == '-'):
                    S_numberic[i+j] = '+'
                else:
                    S_numberic[i+j] = '-'
                j = j + 1

        caseCount = caseCount + 1
        i = i + 1

    testResult = True
    j = 0
    while(j < len(S_numberic)):
        if (S_numberic[j] == '-'):
            testResult = False
            break
        j = j + 1

    print str(S_numberic) + " ------ " + str(testResult)

    T_Count = T_Count + 1
    if testResult == True:
        reportString = "Case #" + str(T_Count) + ": " + str(flipCount) + "\n"
    else:
        reportString = "Case #" + str(T_Count) + ": IMPOSSIBLE\n"

    Report.append(reportString)

# print Report


fp = open(outputFile, 'w')
try:
    for line in Report:
        fp.write(line)

finally:
    fp.close()
