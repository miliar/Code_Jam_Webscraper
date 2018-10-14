import sys

googToEng = { 'y' : 'a', 'n' : 'b', 'f' : 'c', 'i' : 'd', 'c' : 'e', 'w' : 'f', 'l' : 'g', 'b' : 'h', 'k' : 'i', 'u' : 'j', 'o' : 'k', 'm' : 'l', 'x' : 'm', 's' : 'n', 'e' : 'o', 'v' : 'p', 'z' : 'q', 'p' : 'r', 'd' : 's', 'r' : 't', 'j' : 'u', 'g' : 'v', 't' : 'w', 'h' : 'x', 'a' : 'y', 'q' : 'z' }

with open( sys.argv[1] ) as dataFile:
    currentCase = 1
    numCases = dataFile.readline()
    for unsplitLine in dataFile:
        currentCaseString = "Case #%s: " % currentCase
        for word in unsplitLine.split():
            for character in word:
                currentCaseString += googToEng[ character ]
            currentCaseString += " "
        print currentCaseString    
        currentCase += 1
