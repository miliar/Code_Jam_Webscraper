import sys

def findNumBlackRings(r, t):
  numRings = 0
  while(1):
    paintReq = r + r + 1
    if paintReq > t:
      return numRings
    numRings += 1
    # print("numRings: " + str(numRings) + "; paintReq: " + str(paintReq) + "; t: " + str(t))
    t -= paintReq
    r += 2

def main():
  inputFile = open('A-small-attempt0.in','r')
  outputFile = open('A-small-attempt0.txt','w')
  index = 0
  for inputLine in inputFile:
    if index == 0:
      numTestCases = int(inputLine)
      caseNum = 0
    else:
      # print("---")
      caseNum += 1
      inputData = inputLine.split(' ')
      r,t = int(inputData[0]),int(inputData[1])
      answer = findNumBlackRings(r, t)
      outputStr = 'Case #' + str(caseNum) + ': ' + str(answer) + '\n'
      outputFile.write(outputStr)
    index += 1
  inputFile.close()
  outputFile.close()

if __name__ == '__main__':
  main()