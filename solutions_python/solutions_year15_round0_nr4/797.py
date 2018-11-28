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
        inputParams = textToParse.split(" ")
        X = int(inputParams[0]) # size of omino
        R = int(inputParams[1]) # one dimension of rectangle to fill with ominos
        C = int(inputParams[2]) # other dimension of rectangle to fill with ominos
        rShort = min(R, C)
        rLong = max(R, C)
        if X == 1:
            richCanWin = False
        if X < rShort:
            # Can be filled up easily.
            richCanWin = False
        if X >= 7:
            # For ominos of size 7 and more, Richard can always win by choosing
            # the following omino:
            # XXX
            # X X
            # XX
            richCanWin = True
        elif X > rLong:
            # An omino of 1 x X doesn't fit into the rectangle.
            richCanWin = True
        elif (R * C) % X > 0:
            # The rectangle to be filled has a size which would require an
            # overlap of ominos.
            richCanWin = True
        elif X <= 2 and rShort == 1:
            # No L-shaped ominos.
            # Only one line, Gabriel can place the omino at one end.
            richCanWin = False
        elif X > rShort + rShort - 1: # -1 for overlap of L-shaped omino
            # The given omino has to fit into the dimensions of the omino.
            richCanWin = True
        else:
            # If the given omino splits the rectangle into compartments and these
            # can't be filled properly, Richard also wins.
            # We need to build a line from one to the other side of the rectangle.
            # This can only be the shorter side, because for the longer side
            # a) X == max(R, C) would be an omino 1 x X and the rectangle could be
            #    filled with similar ominos.
            # b) X > max(R, C) would allow an omino 1 x X which doesn't fit.
            xRemain = X - rShort
            # X <= 6, the maximum of xRemain is 3
            if xRemain == 0:
                # X == rShort, could be filled 1 x X ominos
                richCanWin = False
            elif xRemain == 1:
                # Dimensions of omino would be 2 x rShort with one line 1 x rShort
                # which could be placed on an edge of the rectangle and the
                # remaining rectangle could be easily filled-
                richCanWin = False
            elif xRemain >= 2:
                # One part has to be added on each side of the line, else the same
                # like for xRemain would apply.
                solutionFound = False
                for partWidth in range(1, rLong - 2 + 1):
                    if ((partWidth * rShort - 1) % X == 0 and
                        ((rLong - partWidth - 1)* rShort - (xRemain - 1)) % X == 0):
                        richCanWin = False
                        solutionFound = True
                        break
                if not solutionFound:
                    richCanWin = True
        output = ""
        if richCanWin:
            output += "RICHARD"
        else:
            output += "GABRIEL"
        if i == 0:
            startCharacter = ""
        else:
            startCharacter = "\n"
        print(startCharacter, "Case #", i+1, ": ", output, end="", sep="")