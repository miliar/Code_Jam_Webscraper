
def checkTidy(numLst):
    lastDigit = 0
    for digit in numLst:
        if digit < lastDigit:
            return False
        lastDigit = digit
    return True

def makeList(num):
    numStr = str(num)
    numLst = []
    for digit in numStr:
        numLst.append(int(digit))
    return numLst

def makeNewNum(numLst):
    if numLst[0] == 0:
        numLst = numLst[1:] # delete leading 0, if it's there
    return int(''.join(str(i) for i in numLst)) # convert numLst back to int


# use for large input sizes (recursion)
def getLastTidyNum(n):
    numLst = makeList(n)
    if checkTidy(numLst):
        return n
    else: #not tidy yet
        for index, digit in enumerate(numLst):
            nextDigit = numLst[index+1]
            if digit > nextDigit:
                numLst[index] -= 1
                for indexOfFollowingDigit in xrange(index+1, len(numLst)):
                    numLst[indexOfFollowingDigit] = 9
                break
        newN = makeNewNum(numLst)
        return getLastTidyNum(newN)

t = int(input())

for i in range(1, t + 1):
  n = int(input())
  lastTidyNum = getLastTidyNum(n)
  print("Case #{}: {}".format(i, lastTidyNum))
