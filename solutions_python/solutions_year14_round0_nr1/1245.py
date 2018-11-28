import sys

def compare(firstLine, secondLine):
    global nTime
    nTime += 1
    result = []
    for ele in secondLine:
        if ele in firstLine:
            result.append(ele)

    length = len(result)
    if length == 1:
        sys.stdout.write('Case #' + str(nTime) + ': ' + str(result[0]) + '\n')
    elif length == 0:
        sys.stdout.write('Case #' + str(nTime) + ': ' + "Volunteer cheated!" '\n')
    else:
        sys.stdout.write('Case #' + str(nTime) + ': ' + "Bad magician!" '\n')

def readLine(inputFile):
    for line in inputFile:
        yield line.strip()

def main():
    global nTime
    nTime = 0
    data = readLine(sys.stdin)

    ifFirstLine = True
    line = 0 # line = 0, 1, ..., 9
    firstNumber = -1
    secondNumber = -1
    firstLine = []
    secondLine = []
    for dataLine in data:
        if ifFirstLine:
            ifFirstLine = False
        else:
            if line == 0:
                firstNumber = int(dataLine)
            if line == firstNumber:
                firstLine = dataLine.split(' ')
                firstNumber = -1
            if line == 5:
                secondNumber = int(dataLine) + 5
            if line == secondNumber:
                secondLine = dataLine.split(' ')
                secondNumber = -1
            if line == 9:
                compare(firstLine, secondLine)
                firstLine = []
                secondLine = []
            line += 1
            if line == 10:
                line = 0





if __name__ == '__main__':
    main()