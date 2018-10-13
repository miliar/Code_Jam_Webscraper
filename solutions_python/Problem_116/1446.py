# Google Codejam 
# 2013 Qual: Tick-Tac-Toe-Tomek

import os

def main():

    os.chdir('/Users/Shane/Documents/codeJam Qual 2013')

    f = open('A-large.in.txt')
    #f = open('A-small-attempt1.in.txt')
    #f = open('TTTTtest.in')
    o = open('output.txt','w')

    N = int(f.readline())
    
    for i in range(N):

        # Solve problem
        numRead,answer = solveProblem(f)
        for j in range(4-numRead):
            junk = f.readline()

        # Write output
        o.write("Case #" + str(i+1) + ": " + answer + "\n")

    o.close()
    f.close()


def solveProblem(fHandle):

    colSum = [0,0,0,0]
    diagSum = [0,0]
    playedCount = 0
    notFinished = False

    for i in range(4):
        inputString = fHandle.readline()
        rowTotal = 0
        for j in range(4):
            char = inputString[j]
            if char == ".":
                number = 0
                notFinished = True
            elif char == "X":
                number = 1
            elif char == "O":
                number = -1
            else:
                number = 10

            rowTotal += number
            if i == j:
                diagSum[0] += number
            elif i == (3-j):
                diagSum[1] += number
    
            colSum[j] += number

        if rowTotal == 4 or rowTotal == 13:
            return i,"X won"
        elif rowTotal == -4 or rowTotal == 7:
            return i,"O won"


    X_win = max([(x == 4 or x == 13) for x in colSum])
    X_win2 = max([(x == 4 or x == 13) for x in diagSum])
    O_win = max([(x == -4 or x == 7) for x in colSum])
    O_win2 = max([(x == -4 or x == 7) for x in diagSum])
    
    if X_win or X_win2:
        return i, "X won"
    elif O_win or O_win2:
        return i,"O won"
    if notFinished:
        return i,"Game has not completed"
    else:
        return i,"Draw"




main()
