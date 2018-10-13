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
        aNumber = list(map(int, inputParams[0])) # number
        for pos in range(len(aNumber) - 1):
            if aNumber[pos] > aNumber[pos + 1]:
                aNumber[pos] -= 1
                aNumber[pos + 1:] = [9] * (len(aNumber) - (pos + 1))
                for revPos in range(pos - 1, -1, -1):
                    if aNumber[revPos] > aNumber[revPos + 1]:
                        aNumber[revPos] -= 1
                        aNumber[revPos + 1] = 9
                    else:
                        break
                break
        # remove leading 0
        output = str(int("".join(map(str, aNumber)), 10))
        if i == 0:
            startCharacter = ""
        else:
            startCharacter = "\n"
        print(startCharacter, "Case #", i+1, ": ", output, end="", sep="")