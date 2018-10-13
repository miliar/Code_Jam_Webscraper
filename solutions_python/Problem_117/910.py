import time
import sys

class square:

    def __init__(self,height):
        self.height = height
        self.mowed = False

    def isMowed(self):
        return self.mowed
    
class lawn:
    def __init__(self,row,column):
        self.row = row
        self.column = column
        self.patches = list()
        self.initializePatch()

    def initializePatch(self):
        for i in range(self.row):
            self.patches.append([-1]*self.column)
    

    def initialize(self,data):
        for i in range(self.row):
            for j in range(self.column):
                self.patches[i][j]=square(data[i][j])
    def mow(self):
        
        for i in range(self.row):
            #checking left to right lawn
            #mowHeight1 = self.patches[i][0].height
            #mowHeight2 = self.patches[i][self.column-1].height
            mowHeight = max([self.patches[i][j].height for j in range(self.column)])
            #if mowHeight1>=mowHeight2:
            for j in range(self.column):
                if self.patches[i][j].height == mowHeight:
                    self.patches[i][j].mowed = True
            #checking right to left lawn
            
            #else:
             #   for j in range(self.column):
              #      if self.patches[i][j].height == mowHeight2:
               #         self.patches[i][j].mowed = True
        
        
        for j in range(self.column):
            #checking top to bottom lawn
            #mowHeight3 = self.patches[0][j].height
            #mowHeight4 = self.patches[self.row-1][j].height
            mowHeight = max([self.patches[i][j].height for i in range(self.row)])
            #if mowHeight3>=mowHeight4:
            for i in range(self.row):
                if self.patches[i][j].height == mowHeight:
                    self.patches[i][j].mowed = True
        
            #checking botton to top lawn
            
            #else:
             #   for i in range(self.row):
              #      if self.patches[i][j].height == mowHeight4:
               #         self.patches[i][j].mowed = True
               
    def printStatus(self):
        for i in range(self.row):
            for j in range(self.column):
                print self.patches[i][j].isMowed(),
            print
        print
    def isPossible(self):
        for row in self.patches:
            for patch in row:
                if not patch.isMowed():
                    return 'NO'
             
        return 'YES'
                
    
    
def perform(fileLocation):
    inputFile = open(fileLocation,'r')
    outputFile = open(fileLocation.replace('.in','.out'),'w')

    testCases = int(inputFile.readline())
    lineNumber = 1
    while 1:
        firstLine = inputFile.readline()

        if firstLine == '':
            inputFile.close()
            outputFile.close()
            return
        line = map(int,firstLine.split(' '))
        row = line[0]
        column = line[1]
        data = list()
        for i in range(row):
            line = map(int,inputFile.readline().split(' '))
            data.append(line)

        #print row,column
        #print data

        garden = lawn(row,column)
        garden.initialize(data)

        garden.mow()
        garden.printStatus()
        outputFile.write('Case #%d: %s\n'%(lineNumber,garden.isPossible()))
        lineNumber += 1

if __name__ == '__main__':
    startTime = time.time()
    perform(sys.argv[1])
    stopTime = time.time()
    print 'time required ',stopTime - startTime


    
