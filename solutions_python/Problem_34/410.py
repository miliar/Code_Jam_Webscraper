import re

inFile = open("../A-large.in", "r")
outFile = open("../A-sol.txt", "w")

line = inFile.readline()
params = line.strip().split(" ")
wordLength = int(params[0])
numWords = int(params[1])
testCases = int(params[2])

words = list()
for i in range(numWords):
    words.append(inFile.readline().strip())
    
tests = list()
for i in range(testCases):
    tests.append(inFile.readline().strip())
    

newTests = list()
for test in tests:
    newTest = list()
    inParen = False
    for char in test:
        if not inParen:
            if char == "(":
                inParen = True
            newTest.append(char)
        else:
            if char == ")":
                inParen = False
                newTest.pop()
                newTest.append(char)
            else:
                newTest.append(char)
                newTest.append("|")
    newTests.append("".join(newTest))
                
tests = newTests
curTest = 1
for test in tests:
    numMatches = 0
    for word in words:
        #print("trying " + test + " against " + word)
        if re.match(test, word):
            numMatches = numMatches + 1
            #print(" -- match!")
    outFile.write("Case #" + str(curTest) + ": " + str(numMatches) + "\n")
    curTest = curTest + 1