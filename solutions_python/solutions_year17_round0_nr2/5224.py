def tidyUp(numList):
    size = len(numList)
    index = size - 2
    if index < 0:
        return numList
    while index >= 0:
        if numList[index] > numList[index+1]:
            newIndex = index+1
            numList[newIndex] = 9
            checkOrUpdateRight(numList, newIndex)
            numList[index] -= 1
        index -= 1



def checkOrUpdateRight(number, index):
    if index+1 == len(number):
        return
    elif number[index] > number[index+1]:
        number[index] = 9
        number[index+1] = 9
        checkOrUpdateRight(number, index+1)
    else:
        return
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  case = "Case #" + str(i) + ": "
  n = int(raw_input())
  numList = [int(d) for d in str(n)]
  tidyUp(numList)
  print(case + str(int(''.join(map(str, numList)))))

