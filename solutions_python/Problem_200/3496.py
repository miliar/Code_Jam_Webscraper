import sys

iMaxStackSize = 20000
sys.setrecursionlimit(iMaxStackSize)

def isSortedNumber(listOfNumbers):
    firstNumber = listOfNumbers[0]
    for number in listOfNumbers[1:]:
        if number < firstNumber:
            return False
        else:
            firstNumber = number
    return True

def getListOfIntegerFromNumber(number):
    string = str(number)
    return list(map(lambda number:int(number), list(string)))

def getIndexOfDecrease(listOfNumber):
    firstNumber = listOfNumber[0]
    for index, number in enumerate(listOfNumber[1:]):
        if number < firstNumber:
            return index+1
        else:
            firstNumber = number

def getLastSortedNumber(listOfNumbers):
    if isSortedNumber(listOfNumbers):
        return listOfNumbers
    else:
        indexOfdecrease = getIndexOfDecrease(listOfNumbers)
        lengthOfNumbers = len(listOfNumbers)
        thisNumber = int(''.join(list(map(lambda number: str(number), listOfNumbers[:indexOfdecrease])))) - 1
        return getLastSortedNumber(getListOfIntegerFromNumber(thisNumber))+[9]*(lengthOfNumbers - indexOfdecrease)

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    listOfNumbers = getListOfIntegerFromNumber(int(input()))  # read a list of integers, 2 in this case
    lastSortedListNumber = getLastSortedNumber(listOfNumbers)
    thisNumberList = getListOfIntegerFromNumber(int(''.join(list(map(lambda number:str(number), lastSortedListNumber)))))
    print("Case #{}: {}".format(i, ''.join(list(map(lambda number: str(number), thisNumberList)))))
  # check out .format's specification for more formatting options
