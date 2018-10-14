inFile = open("C-small-attempt0.in", "r")
outFile = open("C-small-out.out", "w")

cases = int(inFile.readline())

for caseNum in range(cases):
    deckSize = int(inFile.readline())
    position = 0
    indexList = range(1, deckSize+1)

    returnList = inFile.readline().split(" ")
    returnList = map(int, returnList)
    returnSize = returnList.pop(0)
    

##    print deckSize
##    print returnList
    

    perfectDeck = {}

    for i in range(1, deckSize+1):
        position = (position + i - 1) % len(indexList)
        deckNum = indexList.pop(position)
        perfectDeck[deckNum] = i

##    print perfectDeck
    

    outputString = "Case #" + str(caseNum + 1) + ":"
    
    for index in returnList:
        outputString = outputString + " " + str(perfectDeck[index])

    print outputString


    

    outputString = outputString + "\n"

    outFile.write(outputString)

    
    



inFile.close()
outFile.close()
