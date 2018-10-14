import sys

if len(sys.argv) == 1:
    print("No input file provided.")
    sys.exit()
else:
    filename = sys.argv[1]
    try:
        fileobject = open(filename, 'r')
    except:
        print("Failed to open given file.")
        sys.exit()
    try:
        firstLine = fileobject.readline()
    except:
        print("Failed to read first line.")
        sys.exit()
    datasetSize = int(firstLine)
    if not datasetSize:
        print("Unable to parse dataset size.")
        sys.exit()
    lineNr = 1
    for i in range(datasetSize):
        lineNr = lineNr + 1
        try:
            lineText = fileobject.readline()
        except:
            print("Failed to read line ", lineNr)
            sys.exit()
        textToParse = lineText.strip()
        inputParams = textToParse.split(" ")
        N = int(inputParams[0]) # number of bathroom stalls
        K = int(inputParams[1]) # number of people
        peopleToPos = K
        stallsFree = N
        splitRound = 0
        peoplePosed = 0
        gapMin = N
        gapMax = N
        while peopleToPos > 0:
            splitRound += 1
            peopleToPosThisRound = 2 ** (splitRound - 1)
            peoplePosed += peopleToPosThisRound
            stallsFree -= peopleToPosThisRound
            if peopleToPosThisRound >= peopleToPos:
                if stallsFree < 0:
                    stallsFree = max(stallsFree, 0)
                gapMin = stallsFree // (2 * peopleToPosThisRound)
                gapsPlusOne = stallsFree % (2 * peopleToPosThisRound)
                if gapsPlusOne > peopleToPosThisRound:
                    gapMax = gapMin + 1
                    gapsPlusOne -= peopleToPosThisRound
                    if peopleToPos <= gapsPlusOne:
                        gapMin += 1
                else:
                    if peopleToPos <= gapsPlusOne:
                        gapMax = gapMin + 1
                    else:
                        gapMax = gapMin
                peopleToPos = 0
            else:
                peopleToPos -= peopleToPosThisRound
        if i == 0:
            startCharacter = ""
        else:
            startCharacter = "\n"
        print(startCharacter, "Case #", i+1, ": ", str(gapMax), " ", str(gapMin), end="", sep="")