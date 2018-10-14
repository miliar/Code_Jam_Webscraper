import itertools
import math
import operator

class TTTT:
        
    def tic_tac_toe_tomek(self):
        inputFile = open('input.txt','r')
        outputFile = open('output.txt','w')
        numTestCases = int(inputFile.readline())
        for tc in range(0,numTestCases):

            game = []
            allMovesCompleted = True
            winnerFound = False
            resultString = ''

            for row in range(0,4):
                line = inputFile.readline()
                moves = []
                for char in line:
                    if char != '\n':
                        moves.append(char)
                    if char == '.':
                        allMovesCompleted = False
                game.append(moves)
            line = inputFile.readline()

            # DETERMINE ROWS
            if not winnerFound:
                for row in range(0,4):
                    numX = 0
                    numO = 0
                    numT = 0
                    for column in range(0,4):
                        char = game[row][column]
                        if char == 'X':
                            numX += 1
                        elif char == 'O':
                            numO += 1
                        elif char == 'T':
                            numT += 1
                    if (numX + numT) == 4:
                        winnerFound = True
                        resultString = 'X won'
                        break
                    elif (numO + numT) == 4:
                        winnerFound = True
                        resultString = 'O won'
                        break

            # DETERMINE COLUMNS
            if not winnerFound:
                for row in range(0,4):
                    numX = 0
                    numO = 0
                    numT = 0
                    for column in range(0,4):
                        char = game[column][row]
                        if char == 'X':
                            numX += 1
                        elif char == 'O':
                            numO += 1
                        elif char == 'T':
                            numT += 1
                    if (numX + numT) == 4:
                        winnerFound = True
                        resultString = 'X won'
                        break
                    elif (numO + numT) == 4:
                        winnerFound = True
                        resultString = 'O won'
                        break

            # DETERMINE DIAGS
            if not winnerFound:
                i = 0
                numX = 0
                numO = 0
                numT = 0
                for num in range(0,4):
                    char = game[i][i]
                    if char == 'X':
                        numX += 1
                    elif char == 'O':
                        numO += 1
                    elif char == 'T':
                        numT += 1
                    i += 1
                if (numX + numT) == 4:
                    winnerFound = True
                    resultString = 'X won'
                elif (numO + numT) == 4:
                    winnerFound = True
                    resultString = 'O won'

            if not winnerFound:
                i = 0
                numX = 0
                numO = 0
                numT = 0
                for num in range(4,0,-1):
                    char = game[i][num-1]
                    if char == 'X':
                        numX += 1
                    elif char == 'O':
                        numO += 1
                    elif char == 'T':
                        numT += 1
                    i += 1                        
                if (numX + numT) == 4:
                    winnerFound = True
                    resultString = 'X won'
                elif (numO + numT) == 4:
                    winnerFound = True
                    resultString = 'O won'

            # DETERMINE DRAW
            if not winnerFound and allMovesCompleted:
                resultString = 'Draw'

            # DETERMINE GAME NOT OVER
            if not winnerFound and not allMovesCompleted:
                resultString = 'Game has not completed'
           
            outputString = 'Case #%d: %s\n'%(tc+1,resultString)
            outputFile.write(outputString)
            print outputString
            
if __name__ == '__main__':
    tttt = TTTT()
    tttt.tic_tac_toe_tomek()