#!/usr/bin/python2.6 -tt
def openFile(path, right):
    file = open(path, right)
    return file
    
def closeFile(file):
    file.close()

def parseFile(file):
    firstLine = next(file)
    matrice = {}
    case = 1
    while case <= int(firstLine[:-1]):
        tttLine = 0
        matrice[case] = {}
        while tttLine < 4:
            line = next(file)
            line = line[:-1]
            tmp = {}
            tmp[tttLine] = line
            matrice[case].update(tmp)
            tttLine += 1
        case += 1
        next(file, "EOF")
    return matrice
    
def parseGrille(tab):
    result = ""
    thereIsAWinner = False
    for v in tab:
        if v.count('X') == 4 or (v.count('X') == 3 and v.count('T') == 1):
            result  = "X won"
            thereIsAWinner = True
        if v.count('O') == 4 or (v.count('O') == 3 and v.count('T') == 1):
            result  = "O won"
            thereIsAWinner = True
    return [result, thereIsAWinner]    
    
def defineWinner(tab):
    thereIsAWinner = False
    gameIsOn = False
    # horizontal check
    horizon = parseGrille(tab)
    if horizon[1] == False:
        #vertical check
        vertical = parseGrille(findVerticalResult(tab))
        if vertical[1] == False:
            # diagonal check
            diagonal = parseGrille(findDiagonalResult(tab))
            if diagonal[1] == False:
                thereIsAWinner = False
            else:
                thereIsAWinner = True
                result = diagonal[0]
        else:
            thereIsAWinner = True
            result = vertical[0]
    else:
        thereIsAWinner = True  
        result = horizon[0] 
            
    if thereIsAWinner == False:
        for v in tab:
            if v.count('.') > 0:
                result = "Game has not completed"
                gameIsOn = True
    
    if  thereIsAWinner == False and gameIsOn == False:
        result = "Draw" 
    
    return result  
        
def findVerticalResult(tab):
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''
    for l in tab:
        line1 += l[0]
        line2 += l[1]
        line3 += l[2]
        line4 += l[3]
    newArray = [line1, line2, line3, line4]
    
    return newArray    
    
def findDiagonalResult(tab):
    line1 = ''
    line2 = ''
    i = 0
    for v in tab:
        if i == 0:
            line1 += v[0]
            line2 += v[3]
        if i == 1:
            line1 += v[1]
            line2 += v[2]
        if i == 2:
            line1 += v[2]
            line2 += v[1]
        if i == 3:
            line1 += v[3]
            line2 += v[0]
        i += 1
    newArray = [line1, line2]
    return newArray

def main():
    path = "A-large.in"
    output = "A-large"
    file = openFile(path, "rU")
    outputFile = openFile(output, "wb")
    
    cases = parseFile(file)
    i = 1
    for case in cases.values():
        outputFile.write("Case #" + str(i) + ": " + defineWinner(case.values())+"\n") 
        i += 1
    
    closeFile(file)
    closeFile(outputFile)
	
#launch the main function
if __name__ == '__main__':
	main()