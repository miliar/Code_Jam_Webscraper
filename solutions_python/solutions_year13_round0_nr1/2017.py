#!/usr/bin/python
import string
import math



def debug(message):
  print message

def log(message):
  print message


def checkForWin(lines, side):
  if (checkH(lines, side)):
    return True
  if (checkV(lines, side)):
    return True
  if (checkD(lines, side)):
    return True
  return False


def checkH(lines, side):
  for y in xrange(0,len(lines)):
    line=lines[y]
    grapFound=False
    for x in xrange(0,len(line)):
      if (line[x]!=side and line[x]!="T"):
        grapFound=True
    if not grapFound:
      return True
  return False

def checkV(lines, side):
  for x in xrange(0,len(lines[0])):
    grapFound=False
    for y in xrange(0,len(lines)):
      if (lines[y][x]!=side and lines[y][x]!="T"):
        grapFound=True
    if not grapFound:
      return True
  return False

def checkD(lines, side):
  if True:
    grapFound=False
    for x in xrange(0,len(lines)):
      if (lines[x][x]!=side and lines[x][x]!="T"):
        grapFound=True
    if not grapFound:
      return True
  if True:
    grapFound=False
    for x in xrange(0,len(lines)):
      if (lines[3-x][x]!=side and lines[3-x][x]!="T"):
        grapFound=True
    if not grapFound:
      return True
  return False

def gameEnded(lines):
  for y in xrange(0,len(lines)):
    line=lines[y]
    for x in xrange(0,len(line)):
      if (line[x]=="."):
        return False
  return True

log("start")
outfile=open('outTic','w')
infile=open('in','r')
infile.readline()

caseNumber=0

while(True):
  lines=[]
  for n in xrange(0,4):
    lines.append(infile.readline().rstrip('\n'))
    
  if (not infile.readline()):
    break;
  
  caseNumber+=1
  print "case #"+str(caseNumber)
  
  outputLine="Game has not completed"
  
  if gameEnded(lines):
    outputLine="Draw"
  
  if checkForWin(lines, "X"):
    outputLine="X won"
  
  if checkForWin(lines, "O"):
    outputLine="O won"
  
  
  print outputLine
  
  outLine="Case #"+str(caseNumber)+": "+outputLine
  outfile.write(outLine+"\n")




