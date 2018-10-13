#! /usr/bin/env python3

def readField(N):
  field = []
  for i in range(N):
    line = input()
    cells = line.split()
    row = list(map(int, cells))
    field.append(row)
  return field

def getColumn(field, N, M, j):
  for i in range(N):
    yield field[i][j]

def getColumns(field, N, M):
  for j in range(M):
    yield getColumn(field, N, M, j)

def checkField(field, N, M):
  rowMax = list(map(max, field))
  colMax = list(map(max, getColumns(field, N, M)))
  for i in range(N):
    for j in range(M):
      cell = field[i][j]
      if cell < rowMax[i] and cell < colMax[j]:
        return False
  return True  

def processCase(i):
  line = input()
  dimensions = line.split()
  N = int(dimensions[0])
  M = int(dimensions[1])
  field = readField(N)
  print("Case #" + str(i) + ": ", end='')
  if checkField(field, N, M):
    print("YES")
  else:
    print("NO")

def main():
  line = input()
  if line:
    number = int(line)
    for i in range(number):
      processCase(i + 1)

main()
