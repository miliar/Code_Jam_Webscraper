import math
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
        if lineText[-1] == "\n":
            textToParse = lineText[0:-1]
        else:
            textToParse = lineText
        inputParams = textToParse.split("/") # A/B part elf
        #  (A / B + C / D) / 2s
        A = int(inputParams[0]) # 
        B = int(inputParams[1]) #
        j = 2
        while j <= A:
            while A % j == 0 and B % j == 0:
                A = A // j
                B = B // j
            j += 1
        if A / B == 1:
            output = "0"
        elif (2 ** 40) % B != 0:
            output = "impossible"
        else:
            output = str(math.ceil(math.log(A / B) / math.log(1 / 2)))
        if i == 0:
            startCharacter = ""
        else:
            startCharacter = "\n"
        print(startCharacter, "Case #", i+1, ": ", output, end="", sep="")