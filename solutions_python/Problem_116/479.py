#! /usr/bin/env python3

SIZE = 4

def readField():
  result = []
  for i in range(SIZE):
    line = input()
    result.append(line)
  return result

def checkRow(row):
  isX = False
  isO = False
  isEmpty = False
  for i in range(SIZE):
    cell = row[i]
    isX = isX or cell == 'X'
    isO = isO or cell == 'O'
    isEmpty = isEmpty or cell == '.'
  if isEmpty:
    return '.'
  if isX and not isO:
    return 'X'
  if isO and not isX:
    return 'O'  
  return '~'

def getColumn(field, column):
  row = ''
  for i in range(SIZE):
    row += field[i][column]
  return row

def getLeftDiagonal(field):
  row = ''
  for i in range(SIZE):
    row += field[i][i]
  return row

def getRightDiagonal(field):
  row = ''
  for i in range(SIZE):
    row += field[i][SIZE - 1 - i]
  return row

def processCase(i):
  field = readField()
  rows = []
  for row in range(SIZE):
    rows.append(field[row])
  for column in range(SIZE):
    rows.append(getColumn(field, column))
  rows.append(getLeftDiagonal(field))
  rows.append(getRightDiagonal(field))

  print("Case #" + str(i) + ": ", end='')
  isEmpty = False
  for row in rows:
    result = checkRow(row)
    isEmpty = isEmpty or result == '.'
    if result == 'X':
      print("X won")
      return
    if result == 'O':
      print("O won")
      return
  if isEmpty:
    print("Game has not completed")
  else:
    print("Draw")

def main():
  line = input()
  if line:
    number = int(line)
    for i in range(number):
      processCase(i + 1)
      input()

main()
