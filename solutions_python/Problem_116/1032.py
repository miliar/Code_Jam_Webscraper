FILE_NAME = 'A-large.txt'


def checkWin(string):
    '''string: 4 letter sequence
    Returns True if O or X wins.'''
    if 'T' in string:
        if string.count('X') >= 3 or string.count('O') >= 3:
            return True
    return string.count('X') == 4 or string.count('O') == 4


    
def checkBoard(board):
    '''board: A list of 4 strings each length of 4.
    checks wether: X won, O won, Draw, or Not complete.'''
    # firsthorizontal board[0][0], board[0][1], board[0][2], board[0][3]
    # firstvertical board[0][0], board[1][0], board[2][0], board[3][0]
    # diagonal board[0][0], board[1][1], board[2][2], board[3][3]
    # diagonal board[0][3], board[1][2], board[2][1], board[3][0]


    #Check Horizonals
    for row in board:
        if checkWin(row):
            if row.count('X') > 2:
                return 'X won'
            else:
                return 'O won'
    #Check Vertical
    for column in xrange(4):
        test = board[0][column]+board[1][column]+board[2][column]+board[3][column]
        if checkWin(test):
            if test.count('X') > 2:
                return 'X won'
            else:
                return 'O won'
    #Check Diagonals
    diagonals = [board[0][0] + board[1][1] + board[2][2] + board[3][3],\
                 board[0][3] + board[1][2] + board[2][1] + board[3][0]]
    for diagonal in diagonals:
        if checkWin(diagonal):
            if diagonal.count('X') > 2:
                return 'X won'
            else:
                return 'O won'

    #Check Completed
    for row in board:
        if '.' in row:
            return 'Game has not completed'

    return 'Draw'






numberTestCases = 0
testCases = []
with open(FILE_NAME,'r') as file:
    numberTestCases = int(file.readline())
    for line in file:
        if line == '\n':
            testCases.append('BREAK')
        testCases.append(line[:-1])


caseNum = 1
prevBreak = 0
with open('results.txt','w') as file:
    
    for board in xrange(numberTestCases):
        
        file.write('Case #{}: {}\n'.format\
                   (caseNum,checkBoard(testCases[prevBreak:testCases.index('BREAK',prevBreak)])))
        caseNum += 1
        prevBreak = testCases.index('BREAK',prevBreak) + 2
                                          
    
    
                
            
            
    

        
        
