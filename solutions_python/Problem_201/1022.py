fileLocation = 'C-small-2-attempt0.in'
myFile = open(fileLocation)
lines = myFile.read().split('\n')
myFile.close()

outputFile = open('output.txt', 'w')

caseNum = int( lines.pop(0) )

for i in range(caseNum):
    print(i)
    outputFile.write('Case #' + str(i+1) + ': ')
    myN, myK = map(int, lines.pop(0).split(' '))

    myCounter = {myN : 1}
    arrangedKeyList = [myN]

    for j in range(myK-1):
        largestEmptyLength = arrangedKeyList[-1]
        myCounter[largestEmptyLength] -= 1

        if myCounter[largestEmptyLength] == 0:
            arrangedKeyList.pop()
            myCounter.pop(largestEmptyLength, None)

        if largestEmptyLength % 2 == 0:
            length1 = (largestEmptyLength - 2) // 2
            length2 = largestEmptyLength - 1 - length1
            if length1 in arrangedKeyList:
                myCounter[length1] += 1
            else:
                arrangedKeyList.append(length1)
                arrangedKeyList.sort()
                myCounter[length1] = 1
            if length2 in arrangedKeyList:
                myCounter[length2] += 1
            else:
                arrangedKeyList.append(length2)
                arrangedKeyList.sort()
                myCounter[length2] = 1
        else:
            length = (largestEmptyLength - 1) // 2
            if length in arrangedKeyList:
                myCounter[length] += 2
            else:
                arrangedKeyList.append(length)
                arrangedKeyList.sort()
                myCounter[length] = 2

    largestEmptyLength = arrangedKeyList[-1]

    if largestEmptyLength % 2 == 0:
        length1 = (largestEmptyLength - 2) // 2
        length2 = largestEmptyLength - 1 - length1
        outputFile.write( str(length2) + ' ' + str(length1) + '\n' )
    else:
        length = (largestEmptyLength - 1) // 2
        outputFile.write( str(length) + ' ' + str(length) + '\n' )
