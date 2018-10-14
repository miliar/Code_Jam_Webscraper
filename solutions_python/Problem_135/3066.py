fin = open('in', 'r')
fout = open('out', 'w')

numberOfCases = int(fin.readline())

def findChosenRow():    
    answer = int(fin.readline())
    for rowNum in range (1,5):
        row = fin.readline()
        if rowNum == answer:
            cosenRow = row.split()
            cosenRow = [int(string) for string in cosenRow]
    return cosenRow

def findCommonCard(firstRow, secondRow):
    numOfCommons = 0
    possibleAnswer = 0
    for card1 in firstRow:
        for card2 in secondRow:
            if card1 == card2:
                possibleAnswer = card1
                numOfCommons += 1
    if numOfCommons == 1:
        return possibleAnswer
    if numOfCommons > 1:
        return 0
    if numOfCommons == 0:
        return -1

for case in range(1,numberOfCases + 1):
    firstRow = findChosenRow()
    secondRow = findChosenRow()
    answer = findCommonCard(firstRow, secondRow)
    if answer > 0:
        fout.write('case #' + str(case) + ': ' + str(answer) + '\n')
    elif answer == 0:
        fout.write('case #' + str(case) + ': Bad magician!\n')
    elif answer == -1:
        fout.write('case #' + str(case) + ': Volunteer cheated!\n')






def method():
    pass




fin.close()
fout.close()
