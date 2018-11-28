###########
#  TIDY   #
###########

def numToList(n):
  if n == 0:
    return [0]
  numList = []
  while n > 0:
    numList.append(n % 10)
    n /= 10
  numList.reverse()
  return numList

def listToNum(L):
  num = 0
  for elem in L:
    num *= 10
    num += elem
  return num

def isTidy(n):
  current = n % 10
  n /= 10
  while n > 0:
    nextNum = n % 10
    if nextNum > current:
      return False
    current = nextNum
    n /= 10
  return True

def getXIndex(numList):
  if numList[1] < numList[0]:
    return 0

  xIndex = 0
  for i in range(1, len(numList) - 1):
    if numList[i] > numList[i - 1]:
      xIndex = i
    if numList[i + 1] < numList[i]:
      return xIndex

def tidy(n):
  if isTidy(n):
    return n
  numList = numToList(n)
  xIndex = getXIndex(numList)
  numList[xIndex]  -= 1
  for i in range(xIndex + 1, len(numList)):
    numList[i] = 9
  return listToNum(numList)

def main(tests):
  file = open("tidy_output.txt", "w")
  for i in range(len(tests)):
    sol = tidy(tests[i])
    file.write("Case #" + str(i + 1) + ": " + str(sol) + "\n")
  file.close()

def getInput():
  with open("B-large.in") as f:
    lines = f.readlines()
    cases = int(lines[0][:-1])
    tests = []
    for i in range(1, cases + 1):
      tests.append(int(lines[i].strip()))
  return tests

main(getInput())



