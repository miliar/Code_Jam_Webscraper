import sys
from bisect import bisect_right, bisect_left

def isPalindrome(num):
  numStr = str(num)
  i,j = 0, len(numStr) - 1
  while i < j:
    if numStr[i] != numStr[j]:
      return False
    i += 1
    j -= 1
  return True

def baseThree(num, numerals="012"):
  base = 3
  left_digits = num // base
  if left_digits == 0:
    return numerals[num % base]
  else:
    return baseThree(left_digits, numerals) + numerals[num % base]

def createFairSquare(high):
  listFairSquare = []
  x = 1
  while(1):
    xb = int(baseThree(x))
    if isPalindrome(xb):
      square = xb*xb
      if square>high:
        break;
      elif isPalindrome(square):
        # print(str(xb) + ' - ' + str(square))
        if square == 121:
          listFairSquare.append(9)
        listFairSquare.append(square)
    x += 1
  # print(listFairSquare)
  return listFairSquare

def findFairSquare(listFairSquare, low, high):
  rt = bisect_right(listFairSquare, high)
  lt = bisect_left(listFairSquare, low)
  return rt-lt

def main():
  inputFile = open('C-large-1.in','r')
  outputFile = open('C-large-1.txt','w')
  high = pow(10,15)
  index = 0
  for inputLine in inputFile:
    if index == 0:
      T = int(inputLine)
      caseNum = 0
      listFairSquare = createFairSquare(high)
    else:
      caseNum += 1
      inputData = inputLine.split(' ')
      low,high = int(inputData[0]),int(inputData[1])
      answer = findFairSquare(listFairSquare, low, high)
      outputStr = 'Case #' + str(caseNum) + ': ' + str(answer) + '\n'
      outputFile.write(outputStr)
    index += 1
  inputFile.close()
  outputFile.close()

if __name__ == '__main__':
  main()