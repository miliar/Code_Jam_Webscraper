#-*- coding:utf-8 -*-
'''
Created on 2009. 09. 03
@author: nakada
'''

wordList = [] # alien word list
testList = [] # alien testCase list

class Alien:
    def __init__(self):
#        self.f = open('data/A-small-attempt0.in','r')
        self.f = open('data/A-large.in','r')
#        self.f = open('data/AlienSmall','r')
        self.out = open('data/AlienSmallOut','w')
        self.wordLength = 0;
        self.wordCount = 0;
        self.caseCount = 0;
        self.finalDic = {} # 최종 결과 리스트
        self.dicList = []
        self.caseLine = []
        self.caseList = []
        
    def fileRead(self):
        lines = self.f.readlines()
        for index, line in enumerate(lines):
            if index==0:
                splitStr = line.replace("\n","").split(" ")
                self.wordLength = int(splitStr[0]);
                self.wordCount = int(splitStr[1]);
                self.caseCount = int(splitStr[2]);
            elif index <= self.wordCount:
                self.dicList.append(line.replace("\n",""))
            elif index <= (self.caseCount + self.wordCount):
                self.caseLine.append(line.replace("\n",""))
    def main(self):
        self.fileRead()
        self.makeCaseWordSplit()
        self.initFinalDic()
        self.iterDicList()
        self.printOut()
        self.f.close()
        self.out.close()
    def printOut(self):
        format = "Case #%(caseIndex)d: %(matchCount)d\n"
        for key, dic in self.finalDic.items():
            self.out.write(format % {"caseIndex":key+1,"matchCount":dic})
    def initFinalDic(self):
        for i in xrange(self.caseCount):
            self.finalDic[i] = 0
    def iterDicList(self):
        for dic in self.dicList:
            for caseIndex, case in enumerate(self.caseList):
                self.procCount(dic, case, caseIndex)
    def procCount(self, dic, case, caseIndex):
        condition = True
        for i in xrange(self.wordLength):
            if case[i].count(dic[i]) == 0:
                condition = False
                break
        if condition:
            self.finalDic[caseIndex] = self.finalDic[caseIndex] + 1
    def makeCaseWordSplit(self):
        for case in self.caseLine:
            self.caseList.append(self.splitWord(case))
    def splitWord(self, input):
        openP = False
        closeP = False
        resultWordList = []
        innerWordList = []
        for item in input:
            if item == "(":
                openP = True
                continue
            elif item == ")":
                closeP = True
            
            if openP and not closeP:
                innerWordList.append(item)
            elif closeP:
                resultWordList.append(innerWordList)
                innerWordList = []
                closeP = False
                openP = False
            else:
                resultWordList.append(item)
        return resultWordList
        
        
if __name__ == '__main__':
    alien = Alien()
    alien.main()