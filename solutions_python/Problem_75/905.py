#!/usr/local/bin/python2.4

import sys,os

class firstProgram:
    def __init__(self,inputFilename = "firstProgramInput.txt", outputFilename="firstProgramOutput.txt"):
        self.inputFilename = inputFilename
        self.outputFilename = outputFilename
        self.combines = []
        self.combinesDict = {}
        self.opposesDict = {}
        self.opposes = []
        self.elements = ""
        self.output = [] 
        self.caseOutput = []
        self.caseOutputDict = {}

    
    def readInputFile(self):
        f = open(self.inputFilename,"r")
        numberOfCases = int(f.readline())
        for caseNumber in range(numberOfCases):
            self.combines = []
            self.combinesDict = {}
            self.opposesDict = {}
            self.opposes = []
            self.caseOutput = [] 
            self.caseOutputDict = {}
            caseNumber = int(caseNumber) + 1
            inputLine = f.readline().split()
            numberOfCombines = int(inputLine[0])
            currentIndex = 0
            for i in range(1,numberOfCombines+1):
                currentIndex += 1
                self.combines.append(inputLine[currentIndex])
            self.createCombinesDict() 
            currentIndex += 1
            numberOfOpposes = int(inputLine[currentIndex])
            for i in range(1,numberOfOpposes+1):
                currentIndex += 1
                self.opposes.append(inputLine[currentIndex])
            self.createOpposesDict() 
            currentIndex += 1
            self.elements = inputLine[currentIndex +1]
            solution = self.solveProblem()
            self.output.append([caseNumber,self.caseOutput])
        f.close()

    def createCombinesDict(self):
        for group in self.combines:
            if not self.combinesDict.has_key(group[0]+group[1]):
                self.combinesDict[group[0]+group[1]] = group[2]
                self.combinesDict[group[1]+group[0]] = group[2]

    def createOpposesDict(self):
        for group in self.opposes:
            if self.opposesDict.has_key(group[0]):
                self.opposesDict[group[0]] += group[1]
            else:
                self.opposesDict[group[0]] = [group[1]]

            if self.opposesDict.has_key(group[1]):
                self.opposesDict[group[1]] += group[0]
            else:
                self.opposesDict[group[1]] = [group[0]]
 

    def canCombine(self,element):
        if len(self.caseOutput) ==0:
            return 0
        if self.combinesDict.has_key(self.caseOutput[len(self.caseOutput)-1]+element):
            return 1
        return 0
    
    def combine(self,element):
        previousElement = self.caseOutput[len(self.caseOutput)-1] 
        self.caseOutput[len(self.caseOutput)-1] = self.combinesDict[self.caseOutput[len(self.caseOutput)-1]+element]
        if self.caseOutputDict[previousElement] == 1:
            del self.caseOutputDict[previousElement]
        else:
            self.caseOutputDict[previousElement] -= 1
        self.caseOutputDict[self.caseOutput[len(self.caseOutput)-1]] = 1

    def isOpposingPairFound(self,element):
        if self.opposesDict.has_key(element):
            for opposingElement in self.opposesDict[element]:
                if self.caseOutputDict.has_key(opposingElement):
                    return 1
        return 0
        
         

    def solveProblem(self):
        for element in self.elements:
            if self.canCombine(element):
                self.combine(element)
            elif self.isOpposingPairFound(element):
                self.caseOutput = []
                self.caseOutputDict = {}
            else:
                self.caseOutput += element
                if self.caseOutputDict.has_key(element):
                    self.caseOutputDict[element] += 1
                else:
                    self.caseOutputDict[element] = 1
                    

    def writeOutput(self):
        f = open(self.outputFilename,"w")
        for case in self.output:
            f.write("Case #"+str(case[0])+": ["+str((", ").join(case[1]))+"]\n")
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
 
