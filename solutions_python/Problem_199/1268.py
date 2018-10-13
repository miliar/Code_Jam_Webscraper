def flip(cakeList, start, end):
  for i in range(start, end):
    if cakeList[i] == 1:
      cakeList[i] = 0
    else:
      cakeList[i] = 1

def check(cakeList):
  for i in range(len(cakeList)):
    if cakeList[i] == 0:
      return False
  return True
  
def increaseBegin(cakeList, origStart):
  start = origStart
  while start < len(cakeList):
    if cakeList[start] == 1:
      start = start + 1
    else:
      break
  return start

def decreaseEnd(cakeList, origEnd):
  end = origEnd
  while end > 0:
    if cakeList[end] == 1:
      end = end - 1
    else:
      break
  return end

def preprocess(cakeStr):
  cakeList = []
  for curChar in cakeStr:
    if curChar == '-':
      cakeList.append(0)
    else:
      cakeList.append(1)
  return cakeList

def solve(caseNum, cakeStr, flipLength):
  result = 0
  cakeList = preprocess(cakeStr)
  begin = increaseBegin(cakeList, 0)
  end = decreaseEnd(cakeList, len(cakeList) - 1)
  if begin > end:
    result = 0
  elif begin == end and cakeList[begin] == 1:
    result = 0
  elif begin == end and cakeList[begin] == 0:
    result = "IMPOSSIBLE"
  elif begin + flipLength > end + 1:
    result = "IMPOSSIBLE"
  else:
    while begin < end:
      flip(cakeList, begin, begin + flipLength)
      result = result + 1
      if check(cakeList):
        break
      flip(cakeList, end - flipLength + 1, end + 1)
      result = result + 1
      if check(cakeList):
        break
      oldBegin = begin
      oldEnd = end
      begin = increaseBegin(cakeList, oldBegin)
      end = decreaseEnd(cakeList, oldEnd)
      if oldBegin == begin and oldEnd == end:
        result = "IMPOSSIBLE"
        break
    if check(cakeList) == False:
      result = "IMPOSSIBLE"
  print("Case #" + str(caseNum) + ": " + str(result))

cases = int(input())
for i in range(cases):
  inputList = input().split()
  solve(i + 1, inputList[0], int(inputList[1]))
    