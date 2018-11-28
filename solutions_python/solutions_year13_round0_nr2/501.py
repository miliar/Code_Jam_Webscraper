import sys

def checkPossibility(inputData):
  # print('\n-----')
  while 1:
    # print(inputData)
    if not inputData:
      return 'YES'
    n = len(inputData)
    m = len(inputData[0])
    minX, minY, minVal = 0, 0, 101
    for x in range(n):
      for y in range(m):
        if minVal > inputData[x][y]:
          minVal = inputData[x][y]
          minX = x
          minY = y
    
    fullRow, fullColumn = True, True

    num=0
    for i in range(n):
      if inputData[i][minY] == minVal:
        num += 1
    if num != n:
      fullColumn = False
    
    num = 0
    for i in range(m):
      if inputData[minX][i] == minVal:
        num += 1
    if num != m:
      fullRow = False
    
    if fullRow == False and fullColumn == False:
      return 'NO'

    if fullRow:
      del inputData[minX]
    elif fullColumn:
      for i in range(n):
        del inputData[i][minY]
  return 'YES'

def main():
  inputFile = open('B-large.in','r')
  outputFile = open('B-large.txt','w')
  i = 0
  for inputLine in inputFile:
    if i == 0:
      T = int(inputLine)
      readN = True
      caseNum = 0
    elif readN == True:
      readN = False
      caseNum += 1
      x = 0
      [n,m] = inputLine.split()
      n,m = int(n), int(m)
      inputData = [[]*m for z in range(n)]
    else:
      inputData[x] = [int(z) for z in (inputLine.split())[:m]]
      x += 1
      if x == n:
        readN = True
        result = checkPossibility(inputData)
        outputStr = 'Case #' + str(caseNum) + ': ' + result + '\n'
        outputFile.write(outputStr)
    i += 1
  inputFile.close()
  outputFile.close()

if __name__ == '__main__':
  main()