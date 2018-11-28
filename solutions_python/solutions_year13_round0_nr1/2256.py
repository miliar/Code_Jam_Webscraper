# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 03:37:45 2013

@author: guvenis
"""
#!/usr/bin/python

global lines, output

def printStatus(case, status):
    if status == 1:
        output.write(("Case #{}: Game has not completed\n").format(case))
    elif status == 2:
        output.write(("Case #{}: X won\n").format(case))
    elif status == 3:
        output.write(("Case #{}: O won\n").format(case))
    elif status == 4:
        output.write(("Case #{}: Draw\n").format(case))

def status(start):
    case = lines[start: start + 4]    
    
    dots = False
    if any([line.find('.')!=-1 for line in case]):
        dots = True
        
    xFound = map(lambda l:l.count('X') + l.count('T'), case)
    oFound = map(lambda l:l.count('O') + l.count('T'), case)
    
    xWon = len( [1 for i in range(4) if xFound[i] == 4] ) > 0
    oWon = len( [1 for i in range(4) if oFound[i] == 4] ) > 0
    
    if xWon:
        return 2
    if oWon:
        return 3
        
    tr =[[j[i] for j in case] for i in range(len(case))]
    
    xFound = map(lambda l:l.count('X') + l.count('T'), tr)
    oFound = map(lambda l:l.count('O') + l.count('T'), tr)
    
    xWon = len( [1 for i in range(4) if xFound[i] == 4] ) > 0
    oWon = len( [1 for i in range(4) if oFound[i] == 4] ) > 0
    
    if xWon:
        return 2
    if oWon:
        return 3
        
    diag1 = [case[i][3-i] for i in range(4)]
    
    xFound = diag1.count('X') + diag1.count('T')
    oFound = diag1.count('O') + diag1.count('T')
    
    xWon = xFound == 4
    oWon = oFound == 4
    
    if xWon:
        return 2
    if oWon:
        return 3
        
    diag2 = [case[i][i] for i in range(4)]
    
    xFound = diag2.count('X') + diag2.count('T')
    oFound = diag2.count('O') + diag2.count('T')
    
    xWon = xFound == 4
    oWon = oFound == 4
        
    if xWon:
        return 2
    if oWon:
        return 3
        
    if dots:
        return 1
    else:
        return 4

############ main #########

output = open("output","w") 
inp = open("A-large.in", "r")

testCases = int( inp.readline())

lines = [line for line in inp.read().splitlines() if len(line) != 0] 

for i in range(testCases):
    printStatus(i+1,status(i*4))
