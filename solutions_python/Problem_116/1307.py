# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 15:12:41 2013

@author: Tautvydas
"""

def isS(sym, s):
    return s == sym or s == 'T' 
def isEmpty(s):
    return s == '.'
    
def isUnfinished(grid):
    for line in grid:
        for sym in line:
            if isEmpty(sym):
                return True
    return False
    
    
    
def checkHorWin(grid, sym):
    for line in grid:
        win = True
        for point in line:
            win = win and isS(sym, point)
        if win: return win
    return False
    
def checkVerWin(grid, sym):
    for i in range (4):
        win = True
        for j in range(4):
            win = win and isS(sym, grid[j][i])
        if win: return win
    return False
    
def checkDiaWin(grid, sym):
    win = True
    for i in range (4):
        win = win and isS(sym, grid[i][i])
    if win: return win
    win = True
    for i in range (4):
        win = win and isS(sym, grid[3-i][i])
    return win
    
def checkForWin(grid, sym):
    win = checkHorWin(grid, sym)
    if not win:
        win = checkVerWin(grid, sym)
    if not win:
        win = checkDiaWin(grid, sym)
    return win


filename = 'A-large'
grid_size = 4


with open(filename + '.in', 'r+') as filein:
    casesCount = int(filein.readline())
    
    with open(filename + '.out', 'w') as fileout:
        
        for caseNr in range(1, casesCount + 1):
            answer = ""
                
            lines = [filein.readline() for i in xrange(grid_size)]    
            grid = [[symbol for symbol in line.strip()] for line in lines]
#            print grid
            
            if checkForWin(grid, 'O'):
                answer = "O won"
            else:
                if checkForWin(grid, 'X'):
                    answer = "X won"
                else:
                    if isUnfinished(grid):
                        answer = "Game has not completed"
                    else:
                        answer = "Draw"
                                
            
                
            
            print "Case #", caseNr, " - ", answer
            filein.readline() #read empty line
            
            fileout.write("Case #%s: " %caseNr)
            fileout.write('%s\n' %answer)
                  
            
 
        
        
        
    
    

