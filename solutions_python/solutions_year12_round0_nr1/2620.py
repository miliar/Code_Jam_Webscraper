'''
Created on Apr 10, 2012

@author: Prashanth
'''
from string import *
if __name__ == '__main__':
 intable =  "abcdefghijklmnopqrstuvwxyz"
 outtable = "yhesocvxduiglbkrztnwjpfmaq"
 transtable = str.maketrans(intable,outtable)
 instr = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
 
 inFile = open('c:\\A-small-attempt0.in','r')
 outFile = open('c:\\A-small-attempt0.out','w')
 testCases = inFile.readline()
 caseNumber = 0
 for line in inFile.readlines():
  caseNumber = caseNumber + 1
  strOut = str.format("Case #%d: %s"%(caseNumber,line.translate(transtable)))
  #strOut = strOut.strip();
  outFile.write(strOut)
  print(strOut)