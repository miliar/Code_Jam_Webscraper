a_file = open('B-large (1).in')
numcases = int(a_file.readline())

for caseNum in range(numcases):
    
    param = a_file.readline().split()
    numDefs = int(param[0])
    defs = []
    for i in range(numDefs):
        defs.append(param[i + 1])
    numOpposed = int(param[numDefs + 1])
    opposed = []
    for i in range(numOpposed):
        opposed.append(param[i+numDefs+2])
    toInvoke = param[numDefs + numOpposed + 3]

    mainArray = []
    
    for currentLetter in toInvoke:
        combined = False
        if len(mainArray) == 0:
            mainArray.append(currentLetter)
        else:
            for comDef in defs:
                if currentLetter == comDef[0]:
                    if mainArray[-1] == comDef[1]:
                        mainArray.pop()
                        mainArray.append(comDef[2])
                        combined = True
                        break
                elif currentLetter == comDef[1]:
                    if mainArray[-1] == comDef[0]:
                        mainArray.pop()
                        mainArray.append(comDef[2])
                        combined = True
                        break
                
            if not combined:
                mainArray.append(currentLetter)
                if len(opposed) > 0:
                    for opp in opposed:
                        if currentLetter == opp[0]:
                            if mainArray.count(opp[1]) > 0:
                                mainArray = []
                                break
                        elif currentLetter == opp[1]:
                            if mainArray.count(opp[0]) > 0:
                                mainArray = []
                                break
                

    output = ""
    for letter in mainArray:
        if len(output) == 0:
            output = letter
        else:
            output += ", " + letter
    
    print("Case #" + str(caseNum + 1) + ": " + "[" + output + "]")
