# -*- coding: utf-8 -*-
'''
Created on 13. apr. 2013

@author: null
'''


'''
0 ma .
1 x zmaga
2 o zmaga
3 nihče ne zmaga
'''
def checkString(string):
    if type(string) == list:
        string = "".join(string)
        
    if string == "XXXX":
        return 1
    if string == "OOOO":
        return 2
    if '.' in string:
        return 0
    if 'T' in string:
        stringX = string.replace('T','X')
        xRet = checkString(stringX)
        if xRet == 1:
            return 1
        stringO = string.replace('T','O')
        oRet = checkString(stringO)
        if oRet == 2:
            return 2
    return 3

def checkRows(game):
    ret = 3
    hasEmpty = False
    for i in xrange(4):
        temp = checkString(game[i])
        if temp == 0:
            hasEmpty = True
        elif temp == 1:
            ret = 1
            break
        elif temp == 2:
            ret = 2
            break
    if ret == 3 and hasEmpty:
        return 0
    return ret

def checkCols(game):
    ret = 3
    hasEmpty = False
    for i in xrange(4):
        string = [x[i] for x in game]
        temp = checkString(string)
        if temp == 0:
            hasEmpty = True
        elif temp == 1:
            ret = 1
            break
        elif temp == 2:
            ret = 2
            break
    if ret == 3 and hasEmpty:
        return 0
    return ret
    
def checkGame(game):    
    hasEmpty = False
    rows = checkRows(game)
    if rows == 0:
        hasEmpty = True
    elif rows == 1:
        return 1
    elif rows == 2:
        return 2
    
    cols = checkCols(game)
    if cols == 1:
        return 1
    elif cols == 2:
        return 2
    
    #\
    diag1 = checkString([game[i][i] for i in range(4)])
    if diag1 == 1:
        return 1
    elif diag1 == 2:
        return 2
    
    #/
    diag2 = checkString([game[i][3-i] for i in range(4)])
    if diag2 == 1:
        return 1
    elif diag2 == 2:
        return 2
    
    if hasEmpty:
        return 0
    return 3
        
if __name__ == '__main__':
    f = open("ttt1.txt")
    t = int(f.readline().strip())
    
    for i in xrange(t):
        game = []
        game.append(f.readline().strip())
        game.append(f.readline().strip())
        game.append(f.readline().strip())
        game.append(f.readline().strip())
        f.readline() #empty line
        result = checkGame(game)
        resultString = "Case #"+ str(i+1) +": " 
        if result == 0:
            resultString += "Game has not completed"
        elif result == 1: 
            resultString += "X won"
        elif result == 2: 
            resultString += "O won"
        elif result == 3:
            resultString += "Draw"
        print resultString
    
    f.close()