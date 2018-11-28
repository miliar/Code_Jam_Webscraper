#!/usr/bin/python
# -*- coding: utf-8 -*- 
import sys
import time

def getValue(inputFile,dataType="string"):
  line=""
  value=0
  while len(line) < 1:
    line=inputFile.readline()

  if dataType=="string":
    value=line.split()[0]
  elif dataType=="integer":
    value=int(line.split()[0])
  elif dataType=="float":
    value=float(line.split()[0])

  return value

def getList(inputFile,dataType="string",separator="space"):
  # dataType could be string, integer and float
  # separator can be space or none
  list=[]
  
  line=""
  while len(line) < 1:
    line=inputFile.readline()

    if  separator=="space":
      list=line.split()
    elif separator=="none":
      line=line.rstrip('\n')
      for i in range(len(line)):
        list.append(line[i])


  #if dataType=="string": ... already a string
  if dataType=="integer":
    i=0
    while i<len(list):
      list[i]=int(list[i])
      i=i+1
  elif dataType=="float":
    i=0
    while i<len(list):
      list[i]=float(list[i])
      i=i+1
  return list

def getBoard(inputFile,dimX,dimY,dataType="string",separator="none"):
  line=""
  board=[]
 
  for y in range(dimY):
      board.append(getList(inputFile,dataType,separator))
 
  return board

def printBoard(board,array="0"):
  #print board
  for i in range(len(board)):
    for j in range(len(board[i])):
      if array=="1":
        sys.stdout.write("[\""+str(board[i][j])+"\"]")
      else:
        sys.stdout.write(str(board[i][j]))
        
    print ""
  
### solve it! ###
def solveIt(c,f,x):
  res=0.0

  speed=2
  cookies=0.0
  spentSeconds=0

  finish=0
  while finish==0:
    withoutMoreFarms=x/speed

    secondsToBuyFarm=c/speed
    newSpeed=speed+f
    withOneMoreFarm=secondsToBuyFarm+x/newSpeed

    if withOneMoreFarm<withoutMoreFarms:
      spentSeconds=spentSeconds+secondsToBuyFarm
      speed=newSpeed
    else:
      spentSeconds=spentSeconds+withoutMoreFarms
      finish=1
    
#    print "spentSeconds: "+str(spentSeconds)

  res=spentSeconds
  return res

if __name__=='__main__':
  # Open input and output files
  inputFile=open(sys.argv[1],'r')
  outputFile=open(sys.argv[2],'w')

  # Get number of cases
  NoC=int(getValue(inputFile))

  # for each case
  for i in range(NoC):
    # get case data
    c,f,x=getList(inputFile,"float")
    # solve problem
    res=solveIt(c,f,x)

    # write data    
    outputFile.write("Case #"+str(i+1)+": "+str(round(res,7))+"\n")
    #print "Case #"+str(i+1)+": "+str(round(res,7))

  # Close input and output files
  inputFile.close()
  outputFile.close()
