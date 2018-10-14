
nTest = int(raw_input())

status = {0:"O won",1:"X won",2:"Draw",3:"Game has not completed"}

def checkRow(board,sym):
    for iRow in range(4):
        flag = True
        for iCol in range(4):
            actChar =  board[iRow][iCol]
            if (actChar != 'T') and (actChar != sym):
                flag = False
                break

        if flag:
            return True
    
    return False

def isEmpty(board):
    isEmp = False
    for iRow in range(4):
        for iCol in range(4):
            actChar =  board[iRow][iCol]
            if (actChar == '.'):
                isEmp = True
                return isEmp

    return isEmp

def checkCol(board,sym):
    for iCol in range(4):
        flag = True
        for iRow in range(4):
            actChar =  board[iRow][iCol]
            if (actChar != 'T') and (actChar != sym):
                flag = False
                break

        if flag:
            return True
    
    return False
        
def checkLeftDiag(board,sym):
    flag = True
    for iRowCol in range(4):
        actChar =  board[iRowCol][iRowCol]
        if (actChar != 'T') and (actChar != sym):
            flag = False
            break
    
    return flag


def checkRightDiag(board,sym):
    flag = True
    for iRowCol in range(4):
        actChar =  board[iRowCol][3-iRowCol]
        if (actChar != 'T') and (actChar != sym):
            flag = False
            break
    
    return flag
        
def isWon(board,symbol='X'):
    if checkRow(board,symbol):
        return True
    elif checkCol(board,symbol):
        return True
    elif checkLeftDiag(board,symbol):
        return True
    elif checkRightDiag(board,symbol):
        return True
    
    return False
    

def getStatus(board):
    if isWon(board,symbol='X'):
        return 1
    elif isWon(board,symbol='O'):
        return 0
    elif isEmpty(board):
        return 3
    else:
        return 2



for iTest in range(nTest):
    board = []
    for iRow in range(4):
        board.append(raw_input()) 
    
    #if iTest != nTest-1:
    raw_input()
    #print board
    print "Case #"+str(iTest+1) + ": " + status[getStatus(board)]