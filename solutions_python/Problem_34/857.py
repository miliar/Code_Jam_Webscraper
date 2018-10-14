#!/usr/bin/env python

import sys

class FileIoInterface:
    def __init__(self, filePath):
        self.filePath=filePath
        self.__dict__['content']=[]
        
    def readFile(self):
        try:
            file=open(self.filePath, 'r')
            for line in file:
                self.__dict__['content'].append(line.strip())
        except OSError:
            print 'missing file', self.filePath
        else:
            file.close()




fileName=sys.argv[1]
inputFile=FileIoInterface(fileName)
inputFile.readFile()

line1=inputFile.content[0].split()
L=int(line1[0])
D=int(line1[1])
N=int(line1[2])


def isEligible(words, match):
    for word in words:
        if word.find(match)==0:
            return True
    return False

def calcPoss(words, line):
    poss=[]
    now=''
    storing=False
    for i in line:
        if i=='(':
            storing=True
            continue
            
        if i==')':
            storing=False
            poss.append(now)
            now=''
            continue
        
        if storing==True:
            now+=i
            continue
        else:
            poss.append(i)
            
    #print 'poss', poss
    
    possGood=['']
    
    for p in poss:
        
        newPossGood=[]
        #print 'now', possGood
        for pg in possGood:
            for p1 in p:
                guess=pg+p1
                #print 'testing', guess,
                if isEligible(words, guess):
                    newPossGood.append(guess)
                    #print 'ok'
                #else:
                    #print 'fail'

        if len(newPossGood)==0:
            #print 'abort'
            return 0
        else:
            possGood=newPossGood[:]
    
    return len(possGood)

#print L, D, N
words=[]

for line in inputFile.content[1:D+1]:
    words.append(line)

caseCtr=1
for line in inputFile.content[D+1:D+N+1]:
    result=calcPoss(words, line)
    print 'Case #'+`caseCtr`+': '+`result`
    caseCtr+=1


