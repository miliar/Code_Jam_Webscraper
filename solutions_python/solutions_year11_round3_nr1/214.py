#!/usr/local/bin/python2.4

import sys,os

class firstProgram:
    def __init__(self,inputFilename = "firstProgramInput.txt", outputFilename="firstProgramOutput.txt"):
        self.inputFilename = inputFilename
        self.outputFilename = outputFilename
        self.output = [] 
        self.caseOutput = []
        self.maxValue = -1 

    
    def readInputFile(self):
        f = open(self.inputFilename,"r")
        numberOfCases = int(f.readline())
        for caseNumber in range(numberOfCases):
            caseNumber = int(caseNumber) + 1
            line = f.readline().strip().split()
            self.numberOfRows = int(line[0])
            self.numberOfColumns = int(line[1])
            self.grid = []
            for row in range(self.numberOfRows):
                self.grid.append([str(x)for x in  f.readline().strip()])
            temp = self.grid 
            self.caseOutput = self.solveProblem(self.grid)
            self.output.append([caseNumber,self.caseOutput])
        f.close()


    def countBlue(self,temp):
        ctr = 0
        for i in range(self.numberOfRows):
            for j in range(self.numberOfColumns):
                if temp[i][j] == '#':
                    ctr += 1
        return ctr
    
    def getTopLeftOfReplacement(self,t,i,j):
        if t[i][j] == '#':
            if i < self.numberOfRows -1 and j < self.numberOfColumns -1:
                if t[i][j] == t[i][j] and  t[i][j] == t[i+1][j] and  t[i][j] == t[i][j+1] and  t[i][j] == t[i+1][j+1]: 
                    return i
                else:
                    return -1
            else:
                return -1
        else:
            return -2
            

        
    def solveProblem(self,t):
        if not self.countBlue(t) %4 ==0 :
            return [[-1]]
        else:
            if self.countBlue(t) ==0:
                return t
            else:
                temp = t
                for i in range(self.numberOfRows-1):
                    for j in range(self.numberOfColumns-1):
                        tl = self.getTopLeftOfReplacement(temp,i,j)
                        if tl == -1:
                            return [[-1]]
                        elif tl == -2:
                            pass
                        else:
                            temp[i][j] = '/'
                            temp[i][j+1] = '\\'
                            temp[i+1][j] = '\\'
                            temp[i+1][j+1] = '/'
                            if self.countBlue(temp) ==0:
                                return temp
     
        return [[-1]]
 
         

    def writeOutput(self):
        f = open(self.outputFilename,"w")
        for case in self.output:
            if case[1][0][0] == -1:
                f.write("Case #"+str(case[0])+":\n"+"Impossible\n")
            else:
                f.write("Case #"+str(case[0])+":\n")#+str(("").join(("\n").join(case[1])))+"\n")
                for row in range(len(case[1])):
                    f.write(str(("").join(case[1][row])))
                    f.write("\n")
        f.close()
 
 

if __name__ == '__main__':
    try:
       inputFilename = sys.argv[1]
    except:
       inputFilename = "firstProgramInput.txt"
    try:
        outputFilename = sys.argv[2]
    except:
       outputFilename = "firstProgramOutput.txt" 


    fp = firstProgram(inputFilename,outputFilename)
    fp.readInputFile()
    #fp.solveProblem()
    fp.writeOutput()
 
