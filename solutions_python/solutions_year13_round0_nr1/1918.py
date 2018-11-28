#!/usr/bin/python

def isWin(line, who):
    for point in line:
        if point == who or point == 'T':
            continue
        else:
            return False
    return True

def isXWin(line):
    return isWin(line, 'X')

def isOWin(line):
    return isWin(line, 'O')

def whoWin(line):
    if isXWin(line) == True:
        return 'X'
    elif isOWin(line) == True:
        return 'O'
    else:
        return '.'

def checkWin(board):
    for line in board:
        result = whoWin(line)
        if result == 'X':
            return 'X'
        elif result == 'O':
            return 'O'

def spreadBoard(board):
    allLines = []
    allLines.extend(board)

    for line in zip(*board):
        allLines.append(list(line))
    
    firstCross = []
    firstCross.append(board[0][0])
    firstCross.append(board[1][1])
    firstCross.append(board[2][2])
    firstCross.append(board[3][3])
    allLines.append(firstCross)

    secondCross = []
    secondCross.append(board[0][3])
    secondCross.append(board[1][2])
    secondCross.append(board[2][1])
    secondCross.append(board[3][0])
    allLines.append(secondCross)

    return allLines
            
def hasEmpty(board):
    for line in board:
        for point in line:
            if point == '.':
                return True

    return False

def getResult(board):
    spreaded = spreadBoard(board)
    result = checkWin(spreaded) 
    if result == 'X':
        return 'X won'
    elif result == 'O':
        return 'O won'

    if hasEmpty(board) == True:
        return 'Game has not completed'
    else: 
        return 'Draw'

def makeList(instr):
    result = []
    for char in instr:
        result.append(char)

    return result

def main():

    inputFile = open("A-large.in", 'r')
    outputFile = open("A-large.out", 'w')

    gameTimes = int(inputFile.readline())
    for case in range(gameTimes):
        board = []
        board.append(makeList(inputFile.readline().strip()))
        board.append(makeList(inputFile.readline().strip()))
        board.append(makeList(inputFile.readline().strip()))
        board.append(makeList(inputFile.readline().strip()))

        outputFile.write('Case #' + str(case + 1) + ': ' + getResult(board) + '\n')
        board.append(inputFile.readline())


    inputFile.close()
    outputFile.close()

if __name__ == "__main__":
    main()
