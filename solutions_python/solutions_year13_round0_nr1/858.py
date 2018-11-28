import sys

       
def solveCase(n, case):

    resultStr = 'Case #%i: %s'
    boardFull = True

    
    # Check rows
    for i in range(4):
        if case[i].replace('T', 'X') == 'XXXX':
            return resultStr % (n, 'X won')
        elif case[i].replace('T', 'O') == 'OOOO':
            return resultStr % (n, 'O won')
        elif case[i].find('.') >= 0:
            boardFull = False

    # Check columns
    for i in range(4):
        col = ''
        for j in range(4):
            col = col + case[j][i]
            
        if col.replace('T', 'X') == 'XXXX':
            return resultStr % (n, 'X won')
        elif col.replace('T', 'O') == 'OOOO':
            return resultStr % (n, 'O won')

    # Check diagonals
    d1 = ''
    d2 = ''
    for i in range(4):
        d1 = d1 + case[i][i]
        d2 = d2 + case[-1-i][i]
    
    if d1.replace('T', 'X') == 'XXXX' or d2.replace('T', 'X') == 'XXXX':
        return resultStr % (n, 'X won')
    elif d1.replace('T', 'O') == 'OOOO' or d2.replace('T', 'O') == 'OOOO':
        return resultStr % (n, 'O won')

    if boardFull:
        return resultStr % (n, 'Draw')
    else:
        return resultStr % (n, 'Game has not completed')
    


def processFile(inputFile, outputFile):
    fileIn = open(inputFile, 'rU')
    fileOut = open(outputFile, 'w')

    cases = int(fileIn.readline().strip())
    C = 0
    while C < cases:
        C += 1
        case = []
        for i in range(4):
            case.append(fileIn.readline().strip())
        fileIn.readline()


        result = solveCase(C, case)
        fileOut.write(result + '\n')

    fileIn.close()
    fileOut.close()
            


processFile('A-large.in', 'A-large.out')
