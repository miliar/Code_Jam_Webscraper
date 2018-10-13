import sys

def readData(fileName):
    f = open(fileName, 'r')
    numOfCases = int(f.readline())
    gameLines = f.read().splitlines()
    f.close()
    games = []
    for i in range(numOfCases):
        game = gameLines[0:4]
        games.append(game)
        gameLines = gameLines[5:]
        
    return games

def solveGames(listOfGames):
    listOfStates = [];
    for game in listOfGames:
        listOfStates.append(solveGame(game))
        
    return listOfStates

def solveGame(game):
    victoryByLines = checkByLines(game)
    victoryByColumns = checkByColumns(game)
    victoryByDiagonal = checkByDiagonal(game)
    victory = victoryByLines or victoryByColumns or victoryByDiagonal
    if victory:
        return victory + ' won' 
    if checkDraw(game):
        return 'Draw' 
    return 'Game has not completed'

def checkDraw(game):
    for line in game:
        for ch in line:
            if ch == '.':
                return False
            
    return True
            
def checkByLines(game):
    for line in game:
        groupResult = checkGroup(line)
        if groupResult != False:
            return groupResult 
        
    return False

def checkByColumns(game):
    columns = []
    for i in range(len(game)):
        columns.append('')
        for j in range(len(game)):
            columns[i] += game[j][i] 
        
    for column in columns:
        groupResult = checkGroup(column)
        if groupResult != False:
            return groupResult 
        
    return False

def checkByDiagonal(game):
    diagonals = ['', '']
    for i in range(len(game)):
        diagonals[0] += game[i][i]
    for i in range(len(game)):
        diagonals[1] += game[len(game) - i - 1][i]    
        
    for diagonal in diagonals:
        groupResult = checkGroup(diagonal)
        if groupResult != False:
            return groupResult 
        
    return False

def checkGroup(line):
    if '.' in line:
        return False
    if line == 'X' * len(line):
        return 'X'
    if line == 'O' * len(line):
        return 'O'
    if 'T' in line:
        lineWithoutT = ''.join(line.split('T'))
        if lineWithoutT == 'X' * (len(line) - 1):
            return 'X'
        if lineWithoutT == 'O' * (len(line) - 1):
            return 'O'
    return False

def writeStates(listOfStates):
    f = open('output.txt', 'w')
    for ind, state in enumerate(listOfStates):
        print('Case #' + str(ind + 1) + ': ' + state, file = f)

if __name__ == '__main__':
    listOfGames = readData(sys.argv[1])
    listOfStates = solveGames(listOfGames)
    writeStates(listOfStates)