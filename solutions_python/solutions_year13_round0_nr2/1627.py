#!/usr/bin/python
import sys
import math
import time

if __name__ == "__main__":
  #start = time.time()
  inputFile = file("B-small-attempt0.in", 'r')
  cases = (int)(inputFile.readline())
  output = []
  temp = cases
  while(cases > 0):
    flag = 0
    line = inputFile.readline()
    row = int(line.split()[0])
    col = int(line.split()[1])
    matrix = []
    for i in range(0, row):
      line = inputFile.readline()
      matrix.append([])
      matrix[i] = line.split()

    maxrow = []
    for i in range(0, row):
      maxr = -100
      for j in range(0, col):
        if maxr < matrix[i][j]:
	  maxr = matrix[i][j]
      maxrow.append(maxr)
    
    maxcol = []
    for i in range(0, col):
      maxc = -100
      for j in range(0, row):
        if maxc < matrix[j][i]:
	  maxc = matrix[j][i]
      maxcol.append(maxc)

    for i in range(0, row):
      for j in range(0, col):
        if matrix[i][j] < maxrow[i] and matrix[i][j] < maxcol[j] and flag != 1:
	  data = "Case #"+str(temp-cases+1)+": NO"
	  output.append(data)
	  flag = 1
	  break

    if flag != 1:
      data = "Case #"+str(temp-cases+1)+": YES"
      output.append(data)
    
    cases = cases - 1

  for i in output:
    print i
