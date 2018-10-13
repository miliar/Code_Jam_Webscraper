import os
import sys

BOARD_SIZE = 4
RANGE = range(BOARD_SIZE)
SET_T = set('T')
SET_O = set('O')
SET_X = set('X')
EMPTY = '.'

class Status:
    O_WON = 'O won'
    X_WON = 'X won'
    NOT_COMPLETED = 'Game has not completed'
    DRAW = 'Draw'

class FoundStatusException(Exception):
    def __init__(self, status):
        self.status = status
        
def checkSet(aSet):
    fSet = aSet - SET_T
    if fSet == SET_O:
        raise FoundStatusException(Status.O_WON)
    if fSet == SET_X:
        raise FoundStatusException(Status.X_WON)

def checkLines(board):
    for line in board:
        checkSet(set(line))
        
def checkColumns(board):
    tBoard = [[board[x][y] for x in RANGE] for y in RANGE]
    checkLines(tBoard)
    
def checkDiagonals(board):
    diagonalSet = set([board[x][x] for x in RANGE])
    checkSet(diagonalSet)
    diagonalSet = set([board[x][BOARD_SIZE - 1 - x] for x in RANGE])
    checkSet(diagonalSet)
    
    
def checkNotCompleted(board):
    for line in board:
        for item in line:
            if item == EMPTY:
                raise FoundStatusException(Status.NOT_COMPLETED)

def getState(board):
    print(board)
    try:
        checkLines(board);
        checkDiagonals(board);
        checkColumns(board);
        checkNotCompleted(board)
        return Status.DRAW
    
    except FoundStatusException as e:
        return e.status
    

def run(inputFilePath):
    with open(inputFilePath, 'r') as inputFile:
        with open(inputFilePath+'-output.txt', 'w') as outputFile:
            T = int(inputFile.readline())
            print("The input file contains", T, "test cases")
            for t in range (1, T+1):
                print("Processing case #" + str(t))
                board = [[y for y in inputFile.readline()][0:BOARD_SIZE]
                            for x in RANGE]
                state = getState(board)
                output = "Case #" + str(t) + ": " + state + "\n"
                print(output)
                outputFile.write(output)
                inputFile.readline() #Consuming the empty line
                

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("Usage: ", sys.argv[0], "input-file")
        exit(0)
    inputFilePath = sys.argv[1]
    print("Working on input file: [", inputFilePath, "].")
    if not os.path.isfile(inputFilePath):
        print ("Error: the input file is not a valid file")
        exit(1)
    run(inputFilePath)
    print('End.')
    