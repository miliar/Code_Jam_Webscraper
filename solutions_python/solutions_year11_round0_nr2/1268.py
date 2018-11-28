inputFile = open("B-small-attempt0.in")
Tests = inputFile.readlines()
inputFile.close()
numTests = int(Tests.pop(0))
currentTest = 1;
print numTests
outPutFile = open('output.txt', 'w')
for line in Tests:
    elementList = []
    convertElements = {}
    opposedElements = []
    test = line.split()
    #print test
    C = int(test.pop(0))
    #print C
    #print test
    if C >= 1:
        for i in range(1, C+1):
            convertElement = test.pop(i-1)
            convertElements[convertElement[:2]] = convertElement[-1]
            convertElements[convertElement[1::-1]] = convertElement[-1]

    D = int(test.pop(0))
    if D >= 1:
        for i in range(1, D+1):
            opposedElement = test.pop(i-1)
            opposedElements.append(opposedElement)
            #opposedElements.append(opposedElement[::-1])
    N = int(test.pop(0))
    series = list(test.pop(0))

  

    for letter in series:
        elementList.append(letter)
        if len(elementList) >= 2:
            if convertElements.has_key(elementList[-1] + elementList[-2]):
                value = convertElements[elementList[-1] + elementList[-2]]
                elementList.pop()
                elementList.pop()
                elementList.append(value)
            for value in opposedElements:
                if value[0] in elementList:
                    if value[1] in elementList:
                        elementList = []



    #print('convertElements')
    #print convertElements
    #print('opposedElements:')
    #print opposedElements
    #print('Series')
    #print series
    #print('ElementList')
    #print elementList
    if len(elementList) >= 1:
        outPutFile.write('Case #' + str(currentTest) + ': [')
        for i in range(0, len(elementList)-1):
            outPutFile.write(elementList[i] + ', ')
        outPutFile.write(elementList[-1] + ']')
        outPutFile.write('\n')
    else:
        outPutFile.write('Case #' + str(currentTest) + ': []')
        outPutFile.write('\n')
    currentTest += 1




    
    

