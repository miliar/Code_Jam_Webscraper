def tidyTest(num):
    string = str(num)
    for i in range(len(string) - 1):
        if int(string[i]) > int(string[i+1]):
            return False
    return True

def getFirstUntidyLocation(num):
    string = str(num)
    lastIncreaseLocation = -1
    for i in range(len(string)-1):
        if int(string[i]) > int(string[i+1]):
            return [i, lastIncreaseLocation]
        if int(string[i]) < int(string[i+1]):
            lastIncreaseLocation = i
    return [-1, lastIncreaseLocation]

def solve(n):
    firstUntidyLocation = getFirstUntidyLocation(n)
    print(firstUntidyLocation)

    if firstUntidyLocation[0] == -1:
        return n

    string = str(n)
    result = ''

    if firstUntidyLocation[1] != -1:
        result += string[:firstUntidyLocation[1] + 1]
        temp = int( string[firstUntidyLocation[1] + 1] ) - 1
        result += str(temp) + '9' * ( len(string) - len(result) -1 )
        return result

    firstDigit = string[0]
    if int(firstDigit) != 1:
        result += str( int(firstDigit) - 1 )
        result += '9' * ( len(string) - 1 )
        return result

    return '9' * ( len(string) - 1 )

fileLocation = 'B-large.in'
myFile = open(fileLocation)
lines = myFile.read().split('\n')
myFile.close()

caseNum = int( lines.pop(0) )

outputFile = open('output.txt', 'w')

for i in range(caseNum):
    outputFile.write('Case #' + str(i+1) + ': ')
    myN = int( lines.pop(0) )
    result = solve(myN)
    outputFile.write( str(result) + '\n')
