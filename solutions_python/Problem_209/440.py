import functools
import math
import operator
import sys

def pancakeSort(pancake1, pancake2):
    if pancake1["R"] > pancake2["R"]:
        return 1
    elif pancake1["R"] < pancake2["R"]:
        return -1
    elif pancake1["H"] > pancake2["H"]:
        return 1
    elif pancake1["H"] < pancake2["H"]:
        return -1
    else:
        return 0

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
        [N, K] = map(int, lineText.strip().split(" "))
        # N ... number of pancakes available
        # K ... number of pancakes requested
        pancakes = []
        pancakeAreaOuter = []
        for j in range(N):
            lineNr = lineNr + 1
            try:
                lineText = fileobject.readline()
            except:
                print("Failed to read line ", lineNr)
                sys.exit()
            textToParse = lineText.strip()
            [R, H] = map(int, textToParse.split(" "))
            pancakes.append({"R": R, "H": H, "outerArea": (2 * math.pi * R * H)})
        pancakes.sort(key=functools.cmp_to_key(pancakeSort), reverse=True)
        maxArea = 0
        # print("pancakes:", pancakes)
        for pos in range(N - K + 1):
            area = math.pi * (pancakes[pos]["R"]) ** 2 + pancakes[pos]["outerArea"]
            itemsWithMaxArea = sorted(pancakes[pos + 1:], key=operator.itemgetter("outerArea"), reverse=True)
            # print("itemsWithMaxArea:", itemsWithMaxArea)
            for pos2 in range(K - 1):
                area += itemsWithMaxArea[pos2]["outerArea"]
            if area > maxArea:
                # print("maxArea:", area)
                maxArea = area
        if i == 0:
            startCharacter = ""
        else:
            startCharacter = "\n"
        print(startCharacter, "Case #", i+1, ": ", "{0:.9f}".format(maxArea), end="", sep="")
