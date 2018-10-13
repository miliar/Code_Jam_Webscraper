def moveNumbersToFront(howMany, number):
    numberList = list(str(number))
    numberSlice = numberList[len(numberList) - howMany:]
    numberList.reverse()
    numberList.append(numberSlice)
    numberList.reverse()

    while howMany > 0:
        numberList.pop(len(numberList) - 1)
        howMany -= 1

    numberList[0] = ''.join(numberList[0])
    
    return int(''.join(numberList))
    

def listNumbersBetweenValues(minimum, maximum):
    returnVal = []
    currentVal = minimum
    while currentVal < maximum + 1:
        returnVal.append(currentVal)
        currentVal += 1
    return returnVal

def challengeC():
    output = ''
    #read file
    fileString = open('/Users/Lenny/Desktop/CodeJam-2012/C-large.in', 'r').read()
    fileArray = fileString.split('\n')
    #ignore # of cases
    fileArray.pop(0)
    fileArray.pop(len(fileArray) - 1)
    caseNumb = 1
    for line in fileArray:
        values = []
        parseLine = line.split()
        A = int(parseLine[0])
        B = int(parseLine[1])
        possibilities = listNumbersBetweenValues(A, B)
        #print(possibilities)
        for possibility in possibilities:
            digitCount = len(str(possibility))
            while digitCount > 0:
                n = possibility
                m = moveNumbersToFront(digitCount, n)
                if n < m and m <= B and len(str(n)) == len(str(m)) and str(m)[0] != '0' and str(n)[0] != '0' and n != m and (n, m) not in values:
                    values.append((n, m))
                digitCount -= 1

        print(len(values))
        output = output + 'Case #' + str(caseNumb) + ': ' + str(len(values)) + '\n'
        caseNumb += 1
    outputFile = open('/Users/Lenny/Desktop/CodeJam-2012/C-large.out', 'w')
    outputFile.write(output)
        
challengeC()
