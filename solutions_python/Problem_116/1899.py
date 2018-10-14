def check(myList):
    for x in myList:
        
        if '.' not in x:
            
            if ('X' or 'T') and not 'O' in x:
                return 'X'
            if ('O' or 'T') and not 'X' in x:
                
                return 'O'

def gameToRows(game):
    rows = []
    for i in range(0, 4):
        rows.append(game.split()[i][0:4])
    return rows
def checkRows(game):
    rows = gameToRows(game)
    return check(rows)
    
    
    
def gameToColumns(game):
    cols = []
    for i in range(0, 4):
        cols.append(game.split()[0][i] + game.split()[1][i] + game.split()[2][i] + game.split()[3][i])
    return cols

def checkCols(game):
    cols = gameToColumns(game)
    return check(cols)
def gameToDiags(game):
    diags = []
    diags.append(game.split()[0][0] + game.split()[1][1] + game.split()[2][2] + game.split()[3][3])
    diags.append(game.split()[0][3] + game.split()[1][2] + game.split()[2][1] + game.split()[3][0])
    return diags
def checkDiags(game):
    diags = gameToDiags(game)
    return check(diags)

def checkGame(game):
    results = [checkRows(game), checkCols(game), checkDiags(game)]
    if 'X' in results:
        return 'X won'
    if 'O' in results:
        return 'O won'
    if '.' in game:
        return 'Game has not completed'
    return 'Draw'
    


inputfile = open('A-large.in', 'r')
outputfile = open('A-large.out', 'w')
n = int(inputfile.readline())
game = ''
for i in range(0,n):
    for j in range(0, 5):
        game += inputfile.readline()
    
    
    outputfile.write('Case #' + str(i +1) + ': '+ checkGame(game) + '\n')
    
    game = ''
  

