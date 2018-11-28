#!/usr/bin/env python3
#
# Tic-Tac-Toe-Tomek
#
# written by mark grandi
# 04/12/2013
#

import sys


def solveProblem(filePath):
    ''' solves the problem'''

    output = open("tttt_output.txt", "w", encoding="utf=8")
    # open the input file
    first = True
    with open(filePath, "r", encoding="utf-8") as f:

        numberOfTests = f.readline()

        # for each test
        for tmp in range(0, int(numberOfTests)):

            output.write("Case #{}: ".format(tmp + 1))
            if first:
                first = False
            else:
                f.readline() # get rid of empty line between tests

            # make the game board
            gameBoardArray = []
            for num in range(0, 4):
                x = f.readline().strip()
                gameBoardArray.append(x)

            
            # we have the gameboard now
            # check for horizontal or veritical matches
            exit = False # whether or not we should go to next test
            horResult = None
            verResult = None
            hasEmptySpace = False
            for i in range(0, 4):
                if exit:
                    break
                for j in range(0, 4):

                    # character to see if has 3+T or 4 in a row
                    startingChar = gameBoardArray[i][j]

                    # skip it if its a T, not a piece that someone placed
                    if startingChar == "T":
                        continue
                    if startingChar == ".":
                        hasEmptySpace = True
                        continue

                  
                    horResult = isMatch(startingChar, gameBoardArray[i][0], gameBoardArray[i][1], gameBoardArray[i][2], gameBoardArray[i][3])
                    verResult = isMatch(startingChar, gameBoardArray[0][j],  gameBoardArray[1][j],  gameBoardArray[2][j],  gameBoardArray[3][j] )
                    if horResult or verResult:
                        output.write("{} won\n".format(startingChar))
                        exit = True
                        break

            if exit: # found a result, go to next test
                continue
            # check top left -> bottom right diagonal
            # find valid starting character
            startingChar = None
            for diagIter in range(0,4):
                if gameBoardArray[diagIter][diagIter] != "." and gameBoardArray[diagIter][diagIter] != "T":
                    startingChar = gameBoardArray[diagIter][diagIter]
                    break

            if startingChar != None:
                diagResult = isMatch(startingChar, gameBoardArray[0][0],  gameBoardArray[1][1],  gameBoardArray[2][2],  gameBoardArray[3][3])
                if diagResult:
                    output.write("{} won\n".format(startingChar))
                    continue

            # check top right -> bottom left diagonal
            # find valid starting character
            startingChar = None
            tmpCounter = 3
            for diagIter in range(0,4):
                if gameBoardArray[diagIter][tmpCounter] != "." and gameBoardArray[diagIter][tmpCounter] != "T":
                    startingChar = gameBoardArray[diagIter][tmpCounter]
                    break
                tmpCounter -= 1

            if startingChar != None:
                diagResult = isMatch(startingChar, gameBoardArray[0][3],  gameBoardArray[1][2],  gameBoardArray[2][1],  gameBoardArray[3][0])
                if diagResult:
                    output.write("{} won\n".format(startingChar))
                    continue

            # if we get here, we didn't get a match, its either a tie or not completed based upon hasEmptySpace
            if hasEmptySpace:
                output.write("Game has not completed\n")
            else:
                output.write("Draw\n")

def isMatch(charWeWant, one, two, three, four):
    ''' sees if the 4 arguments are either all X's and T's, or all O's and T's'''

    return (one == charWeWant or one == 'T') and (two == charWeWant or two == 'T') and (three == charWeWant or three == 'T') and  (four == charWeWant or four == 'T')   


solveProblem(sys.argv[1])
