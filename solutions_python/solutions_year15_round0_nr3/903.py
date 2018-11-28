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
    def __init__(self, inputLine, inputLine2=None):
        self._inputLine = inputLine
        self._inputLine2 = inputLine2
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
# HouseOfPancakes

multTable = {
    ('1', '1'): '1',
    ('1', 'i'): 'i',
    ('1', 'j'): 'j',
    ('1', 'k'): 'k',
    ('i', '1'): 'i',
    ('i', 'i'): '1', 
    ('i', 'j'): 'k',
    ('i', 'k'): 'j', 
    ('j', '1'): 'j',
    ('j', 'i'): 'k', 
    ('j', 'j'): '1', 
    ('j', 'k'): 'i',
    ('k', '1'): 'k',
    ('k', 'i'): 'j',
    ('k', 'j'): 'i', 
    ('k', 'k'): '1', 
    }

signTable = {
    ('1', '1'): 1,
    ('1', 'i'): 1,
    ('1', 'j'): 1,
    ('1', 'k'): 1,
    ('i', '1'): 1,
    ('i', 'i'): -1,
    ('i', 'j'): 1,
    ('i', 'k'): -1,
    ('j', '1'): 1,
    ('j', 'i'): -1,
    ('j', 'j'): -1,
    ('j', 'k'): 1,
    ('k', '1'): 1,
    ('k', 'i'): 1,
    ('k', 'j'): -1,
    ('k', 'k'): -1,
    }

class HouseOfPancacesTestcase(CodeJamTestcase):
    def _initTestcase(self):
        CodeJamTestcase._initTestcase(self)
        print(self._inputLine)
        # prepare input for test run
        _, mult = self._inputLine.split()
        mult = int(mult)
        
        self._inStr = self._inputLine2 * mult

    def _findStr(self, search, aStr, start='1'):
        aStr = list(aStr)
        res = start
        mult = 1
#        print('F', aStr, 'find', search)
        while len(aStr) > 0:
            i = aStr.pop(0)
            mult *= signTable[res, i]
            res = multTable[res, i]
#            print('F', aStr, i, res, mult)
            if mult == 1 and res == search:
#                print('F', 'found!')
                return (True, ''.join(aStr))
        return (False, '')
    
    def _pass1(self):
        res = False
        aStr = self._inStr[:]
        start = '1'
        print('pass1', aStr)
        
        while res != True and aStr != "":
            (res, aStr) = self._findStr('i', aStr, start)
#            print('pass1 after findStr', aStr)
            if aStr == '':
                break
            #break
            start = 'i'
            if res == False:
                return False
            res = self._pass2(aStr)
            if res:
                return True
        
        return False
        
    def _pass2(self, aStr):
        if len(aStr) < 2:
            return False
        if 'j' not in aStr and 'k' not in aStr:
            return False
        (mult, res) = self._calc(aStr)
#        print('pass3', mult, res)
        return mult == 1 and res == 'i'

#     def _pass2(self, aStr):
#         res = False
#         aStr = aStr[:]
#         start = '1'
# #        print('pass2', len(aStr), repr(aStr))
#         
#         while res != True and aStr != "":
#             (res, aStr) = self._findStr('j', aStr, start)
#             if aStr == '':
#                 break
#             start = 'j'
#             if res == False:
#                 return False
#             res = self._pass3(aStr)
#             if res:
#                 return True
#         
#         return False

    def _pass3(self, aStr):
        (mult, res) = self._calc(aStr)
#        print('pass3', mult, res)
        return mult == 1 and res == 'k'

    def _calc(self, aStr):
        res = '1'
        mult = 1
#        print('pass3', aStr)
        for i in aStr:
            mult *= signTable[res, i]
            res = multTable[res, i]

#        print('pass3', mult, res)
        return (mult, res)
    
    def _runTestcase(self):
        (m, r) = self._calc(self._inStr)
        if not (m == -1 and r == '1'):
            self._solution = 'NO'
            return
        res = self._pass1()
        print('testcase gelaufen', res)
        if res:
            self._solution = 'YES'
        else:
            self._solution = 'NO'
            
#####################################################################
# problem1

def TestCase(inputLine, inputLine2 = None):
    return HouseOfPancacesTestcase(inputLine, inputLine2)
    
def readInput(inFile, outFile):
    i = open(inFile, "r")
    o = open(outFile, "w")
    numOfCases = int(i.readline().strip())
    for caseNum in range(1, numOfCases+1):
        line = i.readline().strip()
        line2 = i.readline().strip()
        tc = TestCase(line, line2)
        res = tc.run()
        print('Case #{}: {}'.format(caseNum, res), file = o)
#        if caseNum == 2:
#            return
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
#    base="01 2015-Round-0/A-large"
#    base="01 2015-Round-0/B-Sample"

#    base="01 2015-Round-0/C-sample"
#    base="01 2015-Round-0/C-small-attempt0"
#    base="01 2015-Round-0/C-small-attempt1"
    base="01 2015-Round-0/C-small-attempt2"

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
