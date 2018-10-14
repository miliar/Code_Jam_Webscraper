#!/usr/bin/python2
import sys

def findGoodRow(aGame):
    for r in aGame:
        countX = 0
        countO = 0

        if 'T' in r :
            countX = countX + 1
            countO = countO + 1

        countX = countX + r.count('X')
        countO = countO + r.count('O')

        if countX == 4 :
            return 'X'
        elif countO == 4 :
            return 'O'

    return 'N'

def findGoodCol(aGame):
    for c in range(4):
        countX = 0
        countO = 0

        for r in range(4):
            if aGame[r][c] == 'X' :
                countX = countX + 1
            elif aGame[r][c] == 'O' :
                countO = countO + 1
            elif aGame[r][c] == 'T' :
                countX = countX + 1
                countO = countO + 1

        if countX == 4 :
            return 'X'
        elif countO == 4 :
            return 'O'

    return 'N'

def findGoodDiag(aGame):
    countX = 0
    countO = 0
    for l in range(4):

        if aGame[l][l] == 'X' :
            countX = countX + 1
        elif aGame[l][l] == 'O' :
            countO = countO + 1
        elif aGame[l][l] == 'T' :
            countX = countX + 1
            countO = countO + 1

        if countX == 4 :
            return 'X'
        elif countO == 4 :
            return 'O'

    countX = 0
    countO = 0
    for r in range(4):
        l = 3 - r

        if aGame[r][l] == 'X' :
            countX = countX + 1
        elif aGame[r][l] == 'O' :
            countO = countO + 1
        elif aGame[r][l] == 'T' :
            countX = countX + 1
            countO = countO + 1

        if countX == 4 :
            return 'X'
        elif countO == 4 :
            return 'O'

    return 'N'

def isDraw(aGame):
    countDot = 0
    for r in aGame:
        countDot = countDot + r.count('.')

    if countDot == 0 :
        return True

    return False

def printRes(case, res):
    if res == 'X' or res == 'O' :
        print "Case #%s: %s won"%(case, res)
        return True
    elif res == 'D' :
        print "Case #%s: Draw"
        return True

    return False
    # Nothing yet!


def printStatus(case, aGame):
    res = findGoodRow(aGame)
    if printRes(case, res) :
        return

    res = findGoodCol(aGame)
    if printRes(case, res) :
        return

    res = findGoodDiag(aGame)
    if printRes(case, res) :
        return

    res = isDraw(aGame)
    if res :
        print "Case #%s: Draw"%case
        return

    print "Case #%s: Game has not completed"%case

def readGames(inputFile):

    f = open(inputFile)
    lines = [ e.strip() for e in f.readlines()]

    test_cases = int(lines[0])

    case = 1
    game = []
    for line in lines[1:] :

        if case > test_cases:
            return

        if line != '':
            game.append(line)

        if len(game) == 4 :
            printStatus(case, game)
            game = []
            case = case + 1

    f.close()

if __name__ == "__main__" :

    if( len(sys.argv) < 2 ) :
        readGames("tc")
    else :
        readGames(sys.argv[1])
