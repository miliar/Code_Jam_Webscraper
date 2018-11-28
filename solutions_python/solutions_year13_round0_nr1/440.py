#!/usr/bin/python

import os,sys,string


def findwinner(line):
  nx=0
  no=0
  winner=[1,""]
  for j in range(len(line)):
    if line[j]==".":
      winner[0]=0
    elif line[j]=="X":
      nx+=1
    elif line[j]=="O":
      no+=1
    elif line[j]=="T":
      nx+=1
      no+=1
  if nx==4:
    winner[1]+="X"
  elif no==4:
    winner[1]+="O"
  return winner

def solvepuzzle(n,puzzle):
  puzzle_winner=[1,""]
  prefix="Case #"+str(n)+": "
  for i in range(4):
    # row
    temp_winner=findwinner(puzzle[i])
    puzzle_winner[0]*=temp_winner[0]
    puzzle_winner[1]+=temp_winner[1]

    # column
    temp_winner=findwinner("".join([l[i] for l in puzzle]))
    puzzle_winner[0]*=temp_winner[0]
    puzzle_winner[1]+=temp_winner[1]

  # diagonals
  temp_winner=findwinner("".join([puzzle[i][i] for i in range(4)]))
  puzzle_winner[0]*=temp_winner[0]
  puzzle_winner[1]+=temp_winner[1]

  temp_winner=findwinner("".join([puzzle[i][3-i] for i in range(4)]))
  puzzle_winner[0]*=temp_winner[0]
  puzzle_winner[1]+=temp_winner[1]

  if len(puzzle_winner[1])==0 and puzzle_winner[0]==1:
    print prefix+"Draw" 
  elif len(puzzle_winner[1])==1:
    print prefix+puzzle_winner[1]+" won"
  elif len(puzzle_winner[1])>1:
    same=1
    for j in range(len(puzzle_winner[1])):
      same*=(puzzle_winner[1][j]==puzzle_winner[1][0])
    if not(same):
      print prefix+"Error"
      return 0
    else:
      print prefix+puzzle_winner[1][0]+" won"
  elif puzzle_winner[0]==0 and len(puzzle_winner[1])==0:
    print prefix+"Game has not completed"
  else:
    print prefix+"Error, "+puzzle_winner[1]+" won"
    return 0
  return 1
  
fname=sys.argv[1]

fhandle=open(fname,"r")
flines=fhandle.readlines()
fhandle.close()

npuzzles=int(flines[0])

for i in range(npuzzles):
  solvepuzzle(i+1,flines[5*i+1:5*i+5])


