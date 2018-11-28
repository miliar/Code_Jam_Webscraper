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
        pancakes = list(inputParams[0]) # row of pancakes, + is happy side up
        K = int(inputParams[1]) # length of pancake flipper
        flips = 0
        for pos in range(len(pancakes) - K + 1):
            if pancakes[pos] == "-":
                flips += 1
                for flipPos in range(pos, pos + K):
                    if pancakes[flipPos] == "+":
                        pancakes[flipPos] = "-"
                    else:
                        pancakes[flipPos] = "+"
        impossible = False
        for pos in range(len(pancakes) - K + 1, len(pancakes)):
            if pancakes[pos] == "-":
                impossible = True
                break
        if impossible:
            output = "IMPOSSIBLE"
        else:
            output = str(flips)
        if i == 0:
            startCharacter = ""
        else:
            startCharacter = "\n"
        print(startCharacter, "Case #", i+1, ": ", output, end="", sep="")