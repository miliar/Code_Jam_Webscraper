'''
Created on 08/05/2011

@author: Admin
'''


def runTest(testCaseInput):
    splitInput = testCaseInput.split()
    
    numCombos = int(splitInput.pop(0))
    print "We have {0} combos".format(numCombos)
    inputCombos = [list(combo) for combo in splitInput[:numCombos]]
    print "All combos: {0}".format(inputCombos)
    del splitInput[:numCombos]
    
    numCancels = int(splitInput.pop(0))
    print "We have {0} cancels".format(numCancels)
    inputCancels = [list(cancel) for cancel in splitInput[:numCancels]]
    print "All cancels: {0}".format(inputCancels)
    del splitInput[:numCancels]
    
    numInputs = int(splitInput.pop(0))
    print "We have {0} input chars".format(numInputs)
    inputChars = splitInput[0]
    print "All input chars: {0}".format(inputChars)
    del splitInput[:]
    
    def checkCombos(elList):
        lastTwo = elList[-2:]
        lastTwoReversed = [lastTwo[1], lastTwo[0]]
        for combo in inputCombos:
            if combo[:2] == lastTwo or combo[:2] == lastTwoReversed:
                print "Collapsing, matched combo {0}".format(combo)
                elList[-2:] = combo[-1:]
                return True
        return False
        
    elementList = []
    for inputChar in inputChars:
        elementList.append(inputChar)
        print "*{0}".format(elementList)
        
        #check for combos first
        while len(elementList) >= 2 and checkCombos(elementList):
            pass
            
        #then check for cancels
        if len(elementList) >= 2:
            lastOne = elementList[-1]
            for element in elementList[:-1]:
                checkAgainst = [element, lastOne]
                checkAgainstReversed = [checkAgainst[1], checkAgainst[0]]
                for cancel in inputCancels:
                    if cancel == checkAgainst or cancel == checkAgainstReversed:
                        print "Cancelled by {0}".format(cancel)
                        del elementList[:]
                        break 
                if len(elementList) == 0:
                    break
        
        
    
    #format output nicely
    output = "["
    for item in elementList:
        if len(output) > 1:
            output += ", "
        output += item
    output += "]"
    
    return output

if __name__ == '__main__':
    fInput = open('input.txt')
    fOutput = open('output.txt', 'w')
    
    numCases = int(fInput.readline().strip());
    for num in range(1, numCases + 1):
        testCaseInput = fInput.readline().strip();
        print "Running test {0}/{2} on '{1}'".format(num, testCaseInput, numCases)
        result = runTest(testCaseInput)
        toWrite = "Case #{0}: {1}\n".format(num, result)
        print toWrite
        fOutput.write(toWrite)
        
    print "All done!"
