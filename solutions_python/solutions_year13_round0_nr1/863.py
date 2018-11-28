'''
Created on Apr 12, 2013

@author: kai
'''
from scipy import *
import sys
T = 3
X = 2
O = 1
EMPTY = 0
if __name__ == '__main__':
    hndlin = open(sys.argv[1],'rt')
    hndlout = open(sys.argv[2],'w')
    
    numberCases = int(hndlin.readline())
    
    for index in range(0,numberCases):
        
        '''fill the board '''
        board = zeros([4,4])
        for index2 in range(0,4):
            line = hndlin.readline().rstrip('\n')
            for index3 in range(0,4):
                if line[index3] == 'T':
                    board[index2][index3] = T
                elif line[index3] == 'X':
                    board[index2][index3] = X
                elif line[index3] == 'O':
                    board[index2][index3] = O
                else:
                    board[index2][index3] = EMPTY
        
        XWin = False
        OWin = False
        HasEmpty = False
        
        for row in range(0,4):
            xNumber = 0
            oNumber = 0
            for column in range(0,4):
                if board[row][column] == X:
                    xNumber += 1
                elif board[row][column] == O:
                    oNumber += 1
                elif board[row][column] == T:
                    xNumber += 1 
                    oNumber += 1
                elif board[row][column] == EMPTY:
                    HasEmpty = True
            if xNumber == 4:
                XWin = True
                break
            elif oNumber == 4:
                OWin = True
                break
            
            
            
        for column in range(0,4):
            xNumber = 0
            oNumber = 0
            for row in range(0,4):
                if board[row][column] == X:
                    xNumber += 1
                elif board[row][column] == O:
                    oNumber += 1
                elif board[row][column] == T:
                    xNumber += 1 
                    oNumber += 1
                elif board[row][column] == EMPTY:
                    HasEmpty = True
            if xNumber == 4:
                XWin = True
                break
            elif oNumber == 4:
                OWin = True
                break
            
        for diagonal in range(0,2):
            xNumber = 0
            oNumber = 0
            if diagonal == 0:
                for diagonalIndex in range(0,4):
                    if board[diagonalIndex][diagonalIndex] == X:
                        xNumber += 1
                    elif board[diagonalIndex][diagonalIndex] == O:
                        oNumber += 1
                    elif board[diagonalIndex][diagonalIndex] == T:
                        xNumber += 1 
                        oNumber += 1
                    elif board[diagonalIndex][diagonalIndex] == EMPTY:
                        HasEmpty = True                
                if xNumber == 4:
                    XWin = True
                    break
                elif oNumber == 4:
                    OWin = True
                    break

            if diagonal == 1:
                for diagonalIndex in range(0,4):
                    if board[3-diagonalIndex][diagonalIndex] == X:
                        xNumber += 1
                    elif board[3-diagonalIndex][diagonalIndex] == O:
                        oNumber += 1
                    elif board[3-diagonalIndex][diagonalIndex] == T:
                        xNumber += 1 
                        oNumber += 1
                    elif board[3-diagonalIndex][diagonalIndex] == EMPTY:
                        HasEmpty = True                
                if xNumber == 4:
                    XWin = True
                    break
                elif oNumber == 4:
                    OWin = True
                    break
        if XWin:
            output = "Case #"+str(index+1)+": "+ "X won" + '\n'
        elif OWin:
            output = "Case #"+str(index+1)+": "+ "O won" + '\n'
        elif XWin == False and OWin == False and HasEmpty == False:
            output = "Case #"+str(index+1)+": "+ "Draw" + '\n'
        elif XWin == False and OWin == False and HasEmpty == True:
            output = "Case #"+str(index+1)+": "+ "Game has not completed" + '\n'
        
        ''' take out the extra line between cases'''
            
        line = hndlin.readline().rstrip('\n') 
        
        hndlout.write(output)
        
    hndlin.close()
    hndlout.close()