'''
Created on Mar 31, 2013

@author: kinsp1
https://code.google.com/codejam/contest/90101/dashboard#s=p0
'''











class Block:
    '''iterator that yields numbers in the Fibonacci sequence'''

    def __init__(self, rows):
        self.rows = rows
        
        
    def CharWins(self, char):
        #check verticals
        for r in range(4):
            win=True
            for row in self.rows:
                entry = row[r]
                if not (entry == 'T' or entry == char):
                    win = False
   
            if win:
                return True
            
        #check horizontals
        for row in self.rows:
            win=True
            for entry in row:
                if not (entry == 'T' or entry == char):
                    win = False   
            if win:
                return True
            
        #check diagonals 1
        win = True
        for r in range(4):
            entry = self.rows[r][r]
            if not (entry == 'T' or entry == char):
                win = False
        if win:
            return True
        
        #check diagonals 2
        win = True
        for r in range(4):
            entry = self.rows[3-r][r]
            if not (entry == 'T' or entry == char):
                win = False 
        if win:
            return True
        
        return False              
            
    def isGameOver(self):
        for row in self.rows:
            for char in row:
                if char == '.':
                    return False
        return True

def handleBlock(inputFile):
    rowList = []
    for r in range(4):
        theStr=inputFile.readline()
        rowList.append(list(theStr)[:-1])
        
    block=Block(rowList)
    
    if block.CharWins('X'):
        return  "X won"
    
    
    if block.CharWins('O'):
        return  "O won"
    
    if block.isGameOver():
        return "Draw"
    else:
        return "Game has not completed"


    

if __name__ == '__main__':
        
    inputFile = open('A-large.in', 'r')
    outputFile = open('outputFile', 'w')
    outputFile.truncate()
    
    testCount = int(inputFile.readline())

    for i in range(testCount):
        print("Case #{0}: {1}".format(1+i, handleBlock(inputFile)), file=outputFile)
        
        inputFile.readline()
    
    
    
    
    
    
    