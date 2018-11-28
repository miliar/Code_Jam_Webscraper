#!/usr/bin/python
import sys,math
import numpy as np

solutiondict = {0:'.',1:'*',2:'c',9:'$'}

def printmines(array,k,M):
  array[0,0] = 0
  if np.sum(array)!=M:
    print "INCONSISTENCY"
    sys.exit(1)
  solution=""
  if array.shape[0]!= k: array=array.transpose()
  array[0,0] = 2
  for i in range(0,array.shape[0]):
    for j in range(0,array.shape[1]):
      solution+=solutiondict[array[i,j]]
    solution+="\n"
  print solution.strip()

T = int(sys.stdin.readline())
for case in range(1,T+1):
  print "Case #%i:" % (case)
  R0,C0,M=map(int,sys.stdin.readline().strip().split())
  array = np.ones( (R0,C0) )
  transpose = False
  if R0<C0:
    transpose=True
    array = array.transpose()
  R,C=array.shape
  freespace = R*C-M
# DEBUG print R,C,M,freespace

  # no mines: always OK anywhere
  if (M==0):
    array[:,:]=0
    printmines(array,R0,M)
    continue

  # one free space: click there!  # 1x1
  if freespace == 1:
    printmines(array,R0,M)
    continue  

  # 1xn: with at least n>2 (otherwise should be 0 mine or 1 free space
  # let's use this pattern: c....*****, rotate if necessary
  if C==1:
      array[:freespace,:]=0
      printmines(array,R0,M)
      continue

  # ok, we have at least 2x2 sizes
  # there is no way to solve these: 2,3,5,7 "non-mined" fields
  if freespace == 2 or freespace == 3 or freespace == 5 or freespace == 7: 
      print "Impossible"
      continue
  
  # let's kill the rest of the nx2 cells:
  if (C==2):
    if freespace%2 == 1: # odd free space (and odd mines) -> impossible
      print "Impossible"
      continue
    array[0:freespace/2,:]=0
    printmines(array,R0,M)
    continue

  if freespace == 4: # at least 2x2
    array[0:2,0:2] = 0
    printmines(array,R0,M)
    continue

  if freespace == 6: # at least 3x2, and we know which is the shorter side, because we transposed
    array[0:3,0:2] = 0
    printmines(array,R0,M)
    continue

  if freespace==8: # 4x2 is already solved, so this must be: (n>=3) x (m>=3)
    array[0:3,0:3]=0
    array[2,2]=1
    printmines(array,R0,M)
    continue

# bigger than 3x3 and at least 9 free spaces:
  if freespace==9:
    array[0:3,0:3]=0
    printmines(array,R0,M)
    continue

  if freespace==10:
    array[0:2,0:3]=0
    array[2:4,0:2]=0
    printmines(array,R0,M)
    continue

  if freespace==11:
    array[0:4,0:3]=0
    array[3,2]=1
    printmines(array,R0,M)
    continue

  if freespace==12:
    array[0:4,0:3]=0
    printmines(array,R0,M)
    continue


  if freespace % 2 == 0 and freespace <= 2*C:
    f2 = freespace/2
    array[0,:f2] = 0
    array[1,:f2] = 0
    printmines(array,R0,M)
    continue

  if freespace % 2 == 1 and freespace <= 2*C+1:
    f2 = (freespace - 1)/2
    array[0:3,0:3]=0
    array[0,3:f2] = 0
    array[1,3:f2] = 0
    printmines(array,R0,M)
    continue    

  array = array.flatten()
  array[:freespace]=0
  array = array.reshape(R,C)
  
  if freespace % C !=1:
    printmines(array,R0,M)
    continue

  H = freespace / C
  h = 2
  array[0:H,0:C]=0
  array[H,0:h]=0
  if H>2:
      array[H,0:h]=0
      array[H-1,C-1]=1
  else:
      array[H,0:h+1]=0
      array[H-1,C-1]=1
      array[H-2,C-1]=1
  printmines(array,R0,M)
  continue    

  print "THIS CANNOT HAPPEN!"
  sys.exit(1)
