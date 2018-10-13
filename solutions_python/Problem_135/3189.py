#!/usr/bin/python
# -*- coding: utf-8 -*- 
import time
import sys 
import gcjtemplate

### solve it! ###
def solveIt(row1,board1,row2,board2):
#  time.sleep(1)
#  print ""
#  print row1
#  gcjtemplate.printBoard (board1,"1")
#  print row2
#  gcjtemplate.printBoard (board2,"1")
#  time.sleep(5)

  res=[]
  for i in board2[row2-1]:
    if i in board1[row1-1]:
      res.append(i)

  return res

if __name__=='__main__':
  # Open input and output files
  inputFile=open(sys.argv[1],'r')
  outputFile=open(sys.argv[2],'w')

  # Get number of cases
  NoC=int(gcjtemplate.getValue(inputFile))

  # for each case
  for i in range(NoC):
    # get case data
    row1=gcjtemplate.getValue(inputFile,"integer")
    board1=gcjtemplate.getBoard(inputFile,4,4,"integer","space")
    row2=gcjtemplate.getValue(inputFile,"integer")
    board2=gcjtemplate.getBoard(inputFile,4,4,"integer","space")
    # solve problem
    res=solveIt(row1, board1, row2, board2)

    # write data    
    if len(res)==0:
      outputFile.write("Case #"+str(i+1)+": Volunteer cheated!\n")
      print ("Case #"+str(i+1)+": Volunteer cheated!")
    elif len(res)==1:
      outputFile.write("Case #"+str(i+1)+": "+str(res[0])+"\n")
      print ("Case #"+str(i+1)+": "+str(res[0]))
    elif len(res)>1:
      outputFile.write("Case #"+str(i+1)+": Bad magician!\n")
      print ("Case #"+str(i+1)+": Bad magician!")
    else:
      time.sleep(5)
      print "HELP, HELP!"


  # Close input and output files
  inputFile.close()
  outputFile.close()
