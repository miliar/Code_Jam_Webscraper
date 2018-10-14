#!/usr/bin/python


def isFair(inputNum):
    inputStr = str(inputNum)
    loopCount = len(inputStr) / 2
    for count in range(loopCount):
        if inputStr[count] != inputStr[-(count+1)]:
            return False
    return True

def getSquareNumbers(minNum, maxNum):
    results = []
    number = 1
    squareNum = 0
    while True:
        if isFair(number):
            squareNum = number * number
            if minNum <= squareNum and squareNum <= maxNum:
                results.append(squareNum)

            if squareNum >= maxNum:
                break

        number += 1
        if maxNum < number:
            break

    return results

def fairAndSquareNumbers(minNum, maxNum):
    result = []
    squareNums = getSquareNumbers(minNum, maxNum)
    for num in squareNums:
        if isFair(num):
            result.append(num)
    return result

def main():
    inputFile = open("C-small-attempt0.in", 'r')
    outputFile = open("C-small-attempt0.out", 'w')

    gameTimes = int(inputFile.readline())
    for case in range(gameTimes):
        line = inputFile.readline().strip().partition(' ')
        minNum = int(line[0])
        maxNum = int(line[2])
        result = fairAndSquareNumbers(minNum, maxNum)
        outputFile.write('Case #' + str(case + 1) + ': ' + str(len(result)) + '\n')

    inputFile.close()
    outputFile.close()

if __name__ == "__main__":
    main()

