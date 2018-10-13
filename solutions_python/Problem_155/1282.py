#!/usr/local/bin/python3
# encoding: utf-8
#
# README:
# please put the input file in './01 2015-Round0/'

#####################################################################
# imports 

from time import clock

#####################################################################
# InputErrorException

class InputErrorException(Exception):
    pass

#####################################################################
# class CodeJamProblem

class CodeJamTestcase:
    def __init__(self, inputLine):
        self._inputLine = inputLine
        self._solution = None
                
    def _initTestcase(self):
        self._solution = None
        pass
        
    def _strSolution(self):
        return str(self._solution)
    
    def run(self):
        self._initTestcase()
        self._runTestcase()
        res = self._strSolution()
        return res
    
    def __str__(self):
        return self._strSolution()


#####################################################################
# class AlienNumbers

# class AlienNumbers:
#     def __init__(self, alienNumber, srcLang, destLang):
#         self._alienNum = alienNumber
#         self._srcLang = srcLang
#         self._destLang = destLang
#     
#     def src2int(self):
#         base = len(self._srcLang)
#         
#         self._i = 0
#         for c in list(self._alienNum):
#             idx = self._srcLang.find(c)
#             self._i = self._i * base + idx
#         
#     def int2dest(self):
#         i = self._i
#         base = len(self._destLang)
#         
#         res = ""
#         while i > 0:
#             i, r = divmod(i, base)
#             c = self._destLang[r]
#             res = c + res
#         
#         self._result = res

            
#####################################################################
# problem1

# class AlienNumbersTestcase(CodeJamTestcase):
#     def _initTestcase(self):
#         CodeJamTestcase._initTestcase(self)
#         alienNumber, srcLang, destLang = self._inputLine.split()
#         self.alienNumber = AlienNumbers(alienNumber, srcLang, destLang)
# 
#     def _runTestcase(self):
#         self.alienNumber.src2int()
#         self.alienNumber.int2dest()
#         self._solution = self.alienNumber._result
    

#####################################################################
# StandingOvations

class StandingOvationsTestcase(CodeJamTestcase):
    def _initTestcase(self):
        CodeJamTestcase._initTestcase(self)
        print(self._inputLine)
        len1, digits = self._inputLine.split()
        self._digits = [int(i) for i in list(digits)]

    def _runTestcase(self):
#         self.alienNumber.src2int()
#         self.alienNumber.int2dest()
        addPeople = 0
        while True:
            if self._tryRun():
                break
            self._digits[0] += 1
            addPeople += 1
        
        self._solution = addPeople
        
    def _tryRun(self):
        standing = 0
        for i in range(0, len(self._digits)):
            if standing < i:
                return False
            standing += self._digits[i]
        return True

#####################################################################
# problem1

def TestCase(inputLine):
    return StandingOvationsTestcase(inputLine)
    
def readInput(inFile, outFile):
    i = open(inFile, "r")
    o = open(outFile, "w")
    numOfCases = int(i.readline().strip())
    for caseNum in range(1, numOfCases+1):
        line = i.readline().strip()
        tc = TestCase(line)
        res = tc.run()
        print('Case #{}: {}'.format(caseNum, res), file = o)
#         #print('### reading problem', caseNum+1)
#         problem = Problem1(caseNum+1, i, o)
#         problem.readProblem()
#         problem.run()
#         print(problem)
#         problem.writeSolution()
#         #break

#####################################################################
# problem1

def problem1():
#    base="01 2015-Round-0/01-0-sample"
#    base="01 2015-Round-0/A-small-attempt0"
    base="01 2015-Round-0/A-large"
#    base="00 Practice/A-small-practice"
#    base="00 Practice/A-large-practice"
    inFile = base + '.in'
    outFile = base + '.out'
    readInput(inFile, outFile)
# def problem1():
#     base="GoogleInputFiles/A-large-Practice"
#     inFile = base + '.in'
#     outFile = base + '.out'
#     readInput(inFile, outFile)
    
#####################################################################
# main

clock()
problem1()

#print(clock())

#####################################################################
# eof
