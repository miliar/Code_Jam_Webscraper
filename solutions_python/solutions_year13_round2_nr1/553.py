import sys

def findMinWays(a,j,nList):
  i=0
  ways = 0
  while (1):
    if a == 1:
      return j
    elif j==0:
      return ways
    elif a > nList[i]:
      a += nList.pop(i)
      j -= 1
    else:
      x = findMinWays(a+a-1,j,nList[:])
      y = findMinWays(a,j-1,nList[:j-1])
      if x<y:
        return x+1
      else:
        return y+1
  return ways

def main():
  inputFile = open('A-small-attempt0.in','r')
  outputFile = open('osmos.txt','w')
  index = 0
  for inputLine in inputFile:
    if index == 0:
      numTestCases = int(inputLine)
      caseNum = 0
    elif index%2 == 1:
      # print("---")
      caseNum += 1
      a, n = [int(z) for z in inputLine.split()]
      nList = []
    else:
      nList = [int(z) for z in inputLine.split()]
      nList.sort()
      answer = findMinWays(a,n,nList[:])
      outputStr = 'Case #' + str(caseNum) + ': ' + str(answer) + '\n'
      # print(outputStr)
      outputFile.write(outputStr)
    index += 1
  inputFile.close()
  outputFile.close()

if __name__ == '__main__':
  main()