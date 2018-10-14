

fileName = "A-large.in"
#fileName = "testFile.txt"

def bringFriends(caseNum, line):
    counter = 0
    numPpl = 0
    missingFriends = 0
    for c in line:
        if numPpl < counter:
            friendsToAdd = (counter-numPpl)
            missingFriends += friendsToAdd
            numPpl+=friendsToAdd
        numPpl += int(c)
        counter+=1
        
    print ("Case #{0}: {1}".format(caseNum, missingFriends))

with open(fileName) as f:
    firstLine = True
    testNum = 1
    for line in f:
        if firstLine:
            firstLine = False
        else:
            splittedLine = line.strip("\n").split(" ")
            bringFriends(testNum, splittedLine[1])
            testNum+=1