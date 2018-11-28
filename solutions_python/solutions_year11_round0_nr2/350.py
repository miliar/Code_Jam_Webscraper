import random

class ProblemB():
    def __init__(self):
        self.combinedDef = []
        self.opposedDef = []
        self.mainString = []
        self.strOutput = ''
        self.N = 1
        self.fileInput = open("B-large.in", 'r')
        self.fileToPrint = open("Output3.data", "a")
#        self.combineList = ['qqq','rrr']
#
    def printToFile(self, n):
        i = 0
        self.fileToPrint.write("Case #" + n + ": [")
        if(len(self.strOutput)!=0):
            while (len(self.strOutput)-1>i):
                self.fileToPrint.write(self.strOutput[i] + ", ")
                i += 1
            self.fileToPrint.write(self.strOutput[-1])
        self.fileToPrint.write("] \n")
        
        
    def combine(self, combineList):
        for item in combineList:
#            print "Item = " + item[0:2] + " str = " + self.strOutput
#            print item[1:2]+item[0:1]
#            print item[2]
#            print " Do = " + self.strOutput
            self.strOutput = self.strOutput.replace(item[0:2],item[2])
            self.strOutput = self.strOutput.replace(item[1:2]+item[0:1],item[2])
#            print " posle " + self.strOutput
#            if(str.replace(item[0:2],item[2]) != str):
#                print str
#                self.combine(combineList, str)

    def opposed(self, opposedList):
        for item in opposedList:
            if((self.strOutput.find(item[0]) != -1) and (self.strOutput.find(item[1]) != -1)):
                self.strOutput = ''
                
    def getDef(self, str):
        massLine = str.split(" ")
        
        C = int(massLine[0])
        D = int(massLine[C+1])
        self.N = int(massLine[C+D+2])
        
        self.combinedDef = massLine[1:C+1]
        self.opposedDef = massLine[C+2:C+2+D]
        self.mainString = massLine[C+D+3]
        
#        print self.combinedDef
#        print self.opposedDef
#        print self.mainString

    def algorythm(self):
        case = 1
        T = int(self.fileInput.readline())
        print T
        while (T > 0):
            i = 0
            self.strOutput = ''
            line = self.fileInput.readline()
#            print line
            self.getDef(line)
            
            print self.N
            while (self.N > i):
                self.strOutput += self.mainString[i]
#                print self.strOutput
                self.combine(self.combinedDef)
                self.opposed(self.opposedDef)
                i += 1
                
            print self.strOutput
            self.printToFile(str(case))
            T -= 1
            case += 1

ddff = ProblemB()
ddff.algorythm()