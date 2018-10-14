'''
Created on 13-Apr-2013

@author: PANKAJ JAKHAR
'''
answer = ''
from _pyio import open
def TicTacToeTomek():
    f = open("input.txt")
    T = int(f.readline())
    print T
    
    for i in range(T):
#        print 'Test Case: ' + str(i)
        status = solveTic(f)
        global answer
        answer = ''
        print 'Case #' + str(i + 1) + ': ' + status 
    

def solveTic(f):
    matrix = [['-' for _ in range(4)] for _ in range(4)]
    #print matrix
    for i in range(4):
        s = str(f.readline())
        for j in range(4):
            matrix[i][j] = s[j]
    
    for i in range(4):
        for j in range(4):
            if i == 0 and i == j or i == 0 and j - i == 3:
                if diagonalCheck(matrix, i, j):
                    f.readline()
                    global answer
                    return answer
                
            if i < j or i == j:
                if verticalCheck(matrix, i, j):
                    f.readline()
                    global answer
                    return answer
                
            if i > j or i == j:
                if horizontalCheck(matrix, i, j):
                    f.readline()
                    global answer
                    return answer
                
    answer = checkIfDrawOrNotFinished(matrix)
    f.readline()
    
#    print matrix
    return answer
    

def verticalCheck(matrix, i, j):
    XCount = 0
    OCount = 0
    TCount = 0
    
    for i in range(4):
        if matrix[i][j] == 'X':
            XCount += 1
        elif matrix[i][j] == 'O':
            OCount += 1
        elif matrix[i][j] == 'T':
            TCount += 1
            
    status = checkForAnwerValidation(XCount, OCount, TCount)
    return status

def horizontalCheck(matrix, i, j):
    XCount = 0
    OCount = 0
    TCount = 0
    
    for j in range(4):
        if matrix[i][j] == 'X':
            XCount += 1
        elif matrix[i][j] == 'O':
            OCount += 1
        elif matrix[i][j] == 'T':
            TCount += 1
    
    status = checkForAnwerValidation(XCount, OCount, TCount)
    return status
    
def diagonalCheck(matrix, i, j):
    XCount = 0
    OCount = 0
    TCount = 0
    if j > 0:
        i = 0
        for j in range(3, -1, -1):
            if matrix[i][j] == 'X':
                XCount += 1
            elif matrix[i][j] == 'O':
                OCount += 1
            elif matrix[i][j] == 'T':
                TCount += 1
            i += 1
    else:    
        for j in range(4):
            if matrix[j][j] == 'X':
                XCount += 1
            elif matrix[j][j] == 'O':
                OCount += 1
            elif matrix[j][j] == 'T':
                TCount += 1
    
#    print 'XCount' + str(XCount)
#    print 'OCount' + str(OCount)
#    print 'TCount' + str(TCount)
    status = checkForAnwerValidation(XCount, OCount, TCount)
    return status
    
def checkForAnwerValidation(XCount, OCount, TCount):
    if XCount == 4:
        global answer
        answer = 'X won'
        return True
    elif OCount == 4:
        global answer
        answer = 'O won'
        return True
    elif TCount == 1:
        if XCount == 3:
            global answer
            answer = 'X won'
            return True
        elif OCount == 3:
            global answer
            answer = 'O won'
            return True
        
    return False


def checkIfDrawOrNotFinished(matrix):
    
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == '.':
                return 'Game has not completed'
            
    return 'Draw'
    




TicTacToeTomek()
    