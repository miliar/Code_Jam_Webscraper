'''
Created on May 7, 2011

@author: michael
'''
baseElements = set(['Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'])

def readInputFile(fname):
    print 'Opening File %s' % fname
    inputFile = open(fname,'r')
    numOfCases = int(inputFile.readline().strip())
    cases = []
    for i in range(numOfCases):
        lineStr = inputFile.readline().strip()
        lineArr = lineStr.split(' ')
        curIndex = 0
        nOfCombinations = int(lineArr[curIndex])
        curIndex += 1
        combinations = []
        for j in range(curIndex,nOfCombinations+curIndex):
            combinations.append(list(lineArr[j]))
            curIndex += 1
        nOfOpposings = int(lineArr[curIndex])
        curIndex += 1
        opposings = []
        for j in range(curIndex,curIndex+nOfOpposings):
            opposings.append(list(lineArr[j]))
            curIndex += 1
        inputInvokation = lineArr[-1]
        cases.append([combinations,opposings,inputInvokation])
    return cases

def writeOutputFile(fname,outputs):
    print 'Saving File %s' % fname
    outputFile = open(fname,'w')
    for i,output in enumerate(outputs):
        if len(output) == 0:
            txtStr = '[]'
        else:
            txtArr = ['[']
            for char in output:
                txtArr.append(char)
                txtArr.append(', ')
            txtArr[-1] = ']'
            txtStr = ''.join(txtArr)
        if i != len(outputs)-1:
            outputFile.write( 'Case #%i: %s\n' % (i+1,txtStr) )
        else:
            outputFile.write( 'Case #%i: %s' % (i+1,txtStr) )
    outputFile.close()

def processCase(case):
    combinations,opposings,inputInvokation = case
    elementList = []
    for element in inputInvokation:
        elementList.append(element)
        skipOpposingCheck = False
        #Check combin
        if len(elementList) > 1:
            for combination in combinations:
                if (elementList[-1] == combination[0] and elementList[-2] == combination[1]) or (elementList[-2] == combination[0] and elementList[-1] == combination[1]):
                    elementList.pop()
                    elementList.pop()
                    elementList.append(combination[2])
                    skipOpposingCheck = True
                    break 
        #Check Opposing
        if not skipOpposingCheck:
            for opposing in opposings:
                if elementList[-1] == opposing[0]:
                    if opposing[1] in elementList:
                        elementList = []
                        break
                elif elementList[-1] == opposing [1]:
                    if opposing[0] in elementList:
                        elementList = []
                        break
    return elementList
cases = readInputFile('B-large.in')
outputs = []
for case in cases:
    outputs.append(processCase(case))
writeOutputFile('B-large.out',outputs)