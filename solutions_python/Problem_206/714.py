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
        # D ... distance for Annie's horse to go
        # N ... number of other horses
        [D, N] = map(int, lineText.strip().split(" "))
        longestTime = -1
        for j in range(N):
            lineNr = lineNr + 1
            try:
                lineText = fileobject.readline()
            except:
                print("Failed to read line ", lineNr)
                sys.exit()
            # K ... start position of horse j
            # S ... maximum speed of horse j
            [Kj, Sj] = map(int, lineText.strip().split(" "))
            longestTime = max(longestTime, (D - Kj) / Sj)
        cruiseSpeed = D / longestTime
        if i == 0:
            startCharacter = ""
        else:
            startCharacter = "\n"
        print(startCharacter, "Case #", i+1, ": ", '{0:.6f}'.format(cruiseSpeed), end="", sep="")
