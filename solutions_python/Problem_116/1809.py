#!/usr/bin/python
import sys
import time

def find(matrix,sym):
  symList = []
  for i in range(0, 4):
    for j in range(0, 4):
        if (row[i][j] == sym or row[i][j] == 'T'):
          symList.append((i, j))
  return symList

def print_result(output, flag, testcase):
  testcase = str(testcase)
  if flag == 1:
    data = "Case #"+testcase+': X won'
    output.append(data)
  elif flag == 2:
    data = "Case #"+testcase+': O won'
    output.append(data)
  elif flag == 3:
    data = "Case #"+testcase+': Draw'
    output.append(data)
  elif flag == 4:
    data = "Case #"+testcase+': Game has not completed'
    output.append(data)

if __name__ == "__main__":
#  start = time.time()
  inputFile = file("A-large.in", 'r')
  cases = (int)(inputFile.readline())
  temp = cases
  flag = 0
  output = []
  while(cases > 0):
    flag = 0
    row = [[],[],[],[]]
    row[0] = inputFile.readline()
    row[1] = inputFile.readline()
    row[2] = inputFile.readline()
    row[3] = inputFile.readline()
    blankLine = inputFile.readline()
    Tposition = find(row, 'T')
    j = 0
    for i in range(0, 4):
      j = 0
      while j<4 and (flag==0 or flag == 100):
        if row[i][j] == 'X':
          j += 1
	  flag = 100
        elif [(i,j)]==Tposition:
          flag = 100
          j += 1
        else:
          flag = 0
          break
      if flag == 100:
        flag = 1
    for i in range(0, 4):
      j = 0
      while j<4 and (flag == 0 or flag == 100):
        if row[i][j] == 'O':
          j += 1
          flag = 100
        elif [(i,j)]==Tposition:
          j += 1
          flag = 100
        else:
          flag = 0
          break
      if flag == 100:
        flag = 2
    for j in range(0, 4):
      i = 0
      while i<4 and (flag == 0 or flag == 100):
        if row[i][j] == 'X':
          flag = 100
          i += 1
        elif [(i,j)]==Tposition:
          flag = 100
          i += 1
        else:
          flag = 0
          break
      if flag == 100:
        flag = 1
    for j in range(0, 4):
      i = 0
      while i<4 and (flag == 0 or flag == 100):
        if row[i][j] == 'O':
          flag = 100
          i += 1
        elif [(i,j)]==Tposition:
          flag = 100
          i += 1
        else:
          flag = 0
          break
      if flag == 100:
        flag = 2

    i = 0
    while i<4 and (flag == 0 or flag == 100):
      if row[i][i] == 'X' or row[i][i] == 'T':
        i = i+1
        flag = 100
      else:
        flag = 0
        break
    if flag == 100:
      flag = 1

    i = 0
    while i<4 and (flag == 0 or flag == 100):
      if row[i][i] == 'O' or row[i][i] == 'T':
        i = i+1
        flag = 100
      else:
        flag = 0
        break
    if flag == 100:
      flag = 2

    i = 3
    j = 0
    while i>=0 and j<4 and (flag == 0 or flag == 100):
      if row[j][i] == 'X' or row[j][i] == 'T':
        i = i-1
        j = j+1
        flag = 100
      else:
        flag = 0
        break
    if flag == 100:
      flag = 1

    i = 3
    j = 0
    while i>=0 and j<4 and (flag == 0 or flag == 100):
      if row[j][i] == 'O' or row[j][i] == 'T':
        i = i-1
        j = j+1
        flag = 100
      else:
        flag = 0
        break
    if flag == 100:
      flag = 2

    IncompleteGame = find(row, '.')
    if Tposition != [] and IncompleteGame != None:
      IncompleteGame.remove(Tposition[0])
    if flag == 0 and IncompleteGame == []:
      flag = 3
    elif flag == 0 and IncompleteGame != []:
      flag = 4

    print_result(output, flag, temp-cases+1)
    cases = cases - 1

  for i in output:
    print i

#print time.time()-start
