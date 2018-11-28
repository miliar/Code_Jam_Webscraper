import sys


def tidyNum(inputNumString):
    for i in range(len(inputNumString) - 1, 1):
        while inputNumString[i] > inputNumString[i - 1]:
            if inputNumString[i] == 0:
                inputNumString[i] = 9
                inputNumString[i - 1] = inputNumString[i - 1] - 1
            if inputNumString[i] < 0:
                inputNumString[i] = 9
            else:
                inputNumString[i] = inputNumString[i] - 1


inputFile = open('tidyNums.input', 'r')

numLines = int(inputFile.readline())

for i in range(0, numLines):
    num = int(inputFile.readline())
    if num < 10:
        print(num)
        continue
    input = str(num)
    print(tidyNum(input))
