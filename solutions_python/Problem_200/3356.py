def is_list_tidy(numberList):
    return all(numberList[i] <= numberList[i+1] for i in range(len(numberList)-1))

def get_max_number(numberList):
    if is_list_tidy(numberList):
        return int(''.join(map(str,numberList)))
    previousDigit = numberList[0]
    maxNumber = [previousDigit]
    noDigits = len(numberList)
    currentPos = 1
    while True:
        if numberList:
            if numberList[currentPos] >= previousDigit:
                previousDigit = numberList[currentPos]
                maxNumber.append(previousDigit)
                currentPos += 1
            else:
                numberList = []
        else:
            currentPos -= 1
            previousDigit = maxNumber.pop()
            maxNumber.append(previousDigit - 1)
            tmpMaxNumber = maxNumber + [9] * (noDigits - currentPos - 1)
            if is_list_tidy(tmpMaxNumber):
                return int(''.join(map(str,tmpMaxNumber)))
            else:
                maxNumber.pop()

import sys, os
numberDigits = []
inputFilename = sys.argv[1]
outputFilename = os.path.splitext(inputFilename)[0] + '.out'

with open(inputFilename,'r') as f:
    next(f)
    for line in f:
        numberDigits.append([int(c) for c in line[:-1]])

solutions = [get_max_number(N) for N in numberDigits]
for i,sol in enumerate(solutions):
    print("Case #%d: %d" % ((i+1),sol))
