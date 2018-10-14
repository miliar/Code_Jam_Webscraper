#!/usr/bin python

def printOutput(idCase, tabAnswers):
    nbAnswers = len(tabAnswers)
    if (nbAnswers == 1):
        answer = str(tabAnswers[0])
    elif (nbAnswers == 0):
        answer = "Volunteer cheated!"
    else:
        answer = "Bad magician!"
    print("Case #" + str(idCase + 1) + ": " + answer)

def getAnswers(firstRow, secondRow):
    tabAnswers = []

    for card in firstRow:
        if (secondRow.count(card) == 1):
            tabAnswers.append(card)
    return tabAnswers

def main():
    inputFile = open("sample.txt", "r")
    nbTestCases = int(inputFile.readline())

    for idCase in range(nbTestCases):
        firstRow = []
        secondRow = []

        idRow1 = int(inputFile.readline()) -1
        for numRow in range(4):
            cards = inputFile.readline()
            if (numRow == idRow1):
                rowData = cards.split()
                firstRow = (int(rowData[0]), int(rowData[1]),
                            int(rowData[2]), int(rowData[3]))
        idRow2 = int(inputFile.readline()) -1
        for numRow in range(4):
            cards = inputFile.readline()
            if (numRow == idRow2):
                rowData = cards.split()
                secondRow = (int(rowData[0]), int(rowData[1]),
                             int(rowData[2]), int(rowData[3]))
        tabAnswers = getAnswers(firstRow, secondRow)
        printOutput(idCase, tabAnswers)

    inputFile.close();

main()
