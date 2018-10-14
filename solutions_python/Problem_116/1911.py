'''
Created on Apr 12, 2013
Google Code Jam Qualification Round 2013
Problem A

@author: Jared Feldman
'''

def getResult(rowOne, rowTwo, rowThree, rowFour):
    
    xGood = ['X','T']
    oGood = ['O','T']
    rows = [rowOne, rowTwo, rowThree, rowFour]
    
    # Check columns for x win
    x = 0
    while x < 4:
        if (rowOne[x] in xGood) and (rowTwo[x] in xGood) and (rowThree[x] in xGood) and (rowFour[x] in xGood):
            return "X won"
        x += 1
    
    # Check columns for o win
    o = 0
    while o < 4:
        if (rowOne[o] in oGood) and (rowTwo[o] in oGood) and (rowThree[o] in oGood) and (rowFour[o] in oGood):
            return "O won"
        o += 1
    
    # Check rows for x win
    for row in rows:
        if (row[0] in xGood) and (row[1] in xGood) and (row[2] in xGood) and (row[3] in xGood):
            return "X won"
        
    # Check rows for o win
    for row in rows:
        if (row[0] in oGood) and (row[1] in oGood) and (row[2] in oGood) and (row[3] in oGood):
            return "O won"
        
    # Check diagonal for x win
    if (rowOne[0] in xGood) and (rowTwo[1] in xGood) and (rowThree[2] in xGood) and (rowFour[3] in xGood):
        return "X won"
    if (rowOne[3] in xGood) and (rowTwo[2] in xGood) and (rowThree[1] in xGood) and (rowFour[0] in xGood):
        return "X won"
    
    # Check diagonal for o win
    if (rowOne[0] in oGood) and (rowTwo[1] in oGood) and (rowThree[2] in oGood) and (rowFour[3] in oGood):
        return "O won"
    if (rowOne[3] in oGood) and (rowTwo[2] in oGood) and (rowThree[1] in oGood) and (rowFour[0] in oGood):
        return "O won"
    
    # If no winner has been detected and there is still places to be filled then game isn't finished
    for row in rows:
        if "." in row:
            return "Game has not completed"
        
    # Game is a draw
    return "Draw";

if __name__ == '__main__':
    # I/O Files
    readFile = open("A-large.in.txt","r+")
    writeFile = open("A-large.out.txt","w+")
    
    numberOfCases = int(readFile.readline())
    currentCase = 0
        
    # Loop through all cases
    while (currentCase < numberOfCases):
        
        # Increment case number
        currentCase += 1
        
        # Read the 4x4 grid
        rowOne = str.strip(readFile.readline())
        rowTwo = str.strip(readFile.readline())
        rowThree = str.strip(readFile.readline())
        rowFour = str.strip(readFile.readline())
        
        # Read the blank line
        readFile.readline()
        
        print "Case #%s: %s" %(currentCase, getResult(rowOne, rowTwo, rowThree, rowFour))
        writeFile.write("Case #%s: %s\n" %(currentCase, getResult(rowOne, rowTwo, rowThree, rowFour)))