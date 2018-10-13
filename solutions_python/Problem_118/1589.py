import string
import sys

fileName = sys.argv[1]

inPipe = open(fileName, "r")
initValue = inPipe.readline()
numberOfDatasets = int(initValue)
finalString = ""

def isPalindrome(string):
    for i in range(0, len(string)/2):
        if string[i] != string[len(string)-i-1]:
            return False
    return True

fairsquares = []
for i in range(1, 3163):
    testStringBase = str(i)
    test1 = int(testStringBase + testStringBase[::-1])**2
    test2 = int(testStringBase + testStringBase[0:-1][::-1])**2
    if isPalindrome(str(test1)):
        fairsquares.append(test1)
    if isPalindrome(str(test2)):
        fairsquares.append(test2)
    
outstring = ""    
for i in range(0, numberOfDatasets):
    thisSet = inPipe.readline().split()
    thisTestNum = 0
    for j in fairsquares:
        if j >= int(thisSet[0]) and j <= int(thisSet[1]):
            thisTestNum += 1
    outstring += "Case #" + str(i + 1) + ": " + str(thisTestNum) + "\n"

outstring = outstring[:-1]
outPipe = open("fairsquare.txt", "w")
outPipe.write(outstring)
outPipe.close()
