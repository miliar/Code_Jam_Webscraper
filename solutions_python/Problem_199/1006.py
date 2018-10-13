def flip(string, k, location):
    target = string[location : location + k]
    result = ""
    for i in range( len(target) ):
        if target[i] == '+':
            result += '-'
        else:
            result += '+'
    return string[:location] + result + string[location + k:]

def solve(string, k):
    index = string.find('-')
    counter = 0
    while index != -1:
        if index > len(string) - k:
            return -1

        string = flip(string, k, index)
        counter += 1
        index = string.find('-')
    return counter

fileLocation = "A-large.in"
myFile = open(fileLocation)
lines = myFile.read().split('\n')
myFile.close()

outputFile = open("output.txt", 'w')

caseNum = int( lines.pop(0) )
for i in range(caseNum):
    outputFile.write('Case #' + str(i+1) + ": ")
    line = lines.pop(0)
    elements = line.split(' ')

    myString = elements[0]
    myK = int( elements[1] )

    result = solve(myString, myK)
    if result == -1:
        outputFile.write('IMPOSSIBLE')
    else:
        outputFile.write( str(result) )
    outputFile.write('\n')
