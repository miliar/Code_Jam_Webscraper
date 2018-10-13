"""
    Code Jam 2011 Qualification Round, Problem B

    gaz@bitplane.net

"""

with open('input.txt') as inputFile:
    testCount = int(inputFile.readline())
    
    for testNumber in range(testCount):

        # parse test data
        testData = inputFile.readline()[:-1].split(' ')
        readPos = 0 # ugly read pointer, not very pythonic but I've a party to get to by 5pm

        # create combine dict for lookups
        combineDict = {}
        combineCount = int(testData[readPos])
        for i in range(readPos + 1, readPos + combineCount + 1):
            combineDict[testData[i][0] + testData[i][1]] = testData[i][2]
            combineDict[testData[i][1] + testData[i][0]] = testData[i][2]

        readPos = readPos + combineCount + 1

        # and the oppose dict
        opposeDict = {}
        opposeCount = int(testData[readPos])
        for i in range(readPos + 1, readPos + opposeCount + 1):
            a = testData[i][0]
            b = testData[i][1]

            if a in opposeDict:
                opposeDict[a].append(b)
            else:
                opposeDict[a] = [b]
            
            if b in opposeDict:
                opposeDict[b].append(a)
            else:
                opposeDict[b] = [a]


        readPos = readPos + opposeCount + 2
        invokeList = list(testData[readPos])
        outStack = []

        # now we invoke each one...
        for c in invokeList:
            if not len(outStack):
                outStack.append(c)
            else:
                # do combines
                top = outStack[-1]
                if top + c in combineDict:
                    outStack.pop()
                    outStack.append(combineDict[top + c])
                else:
                    # do opposes
                    if len(outStack):
                        if c in opposeDict:
                            if any([x == y for x in opposeDict[c] for y in outStack]): # argh, bad use of zip cost me :(
                                outStack = []
                            else:
                                outStack.append(c)
                        else:
                            outStack.append(c)
                    else:
                        outStack.append(c)


        print("Case #{case}: [{output}]".format(case=testNumber+1, output=", ".join(outStack)))
