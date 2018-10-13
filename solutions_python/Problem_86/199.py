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
            self.lowest = int(line[1])
            self.highest = int(line[2])
            self.otherNotes = f.readline().strip().split()
            self.caseOutput = self.solveProblem()
            self.output.append([caseNumber,self.caseOutput])
        f.close()

        
    def solveProblem(self):
        for y in range(self.lowest,self.highest+1):
            found =0
            for xx in self.otherNotes:
                x = int(xx)
                if x > y:
                    if x%y != 0:
                        found = 1
                        break
                else:
                    if y%x != 0:
                        found = 1
                        break
            if not found:
                return y
        return -1 
 
         

    def writeOutput(self):
        f = open(self.outputFilename,"w")
        for case in self.output:
            if case[1] == -1:
                f.write("Case #"+str(case[0])+": NO\n")
            else:
                f.write("Case #"+str(case[0])+": "+str(case[1])+"\n")
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
 
