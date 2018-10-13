# @author: Oscar Hong, Duke University
#
# Problem B. Tidy Numbers
# num in non-decreasing order are "tidy"
# find the last tidy num from 1 to N
#
# Input:
# - T (num of test cases, between 1 and 100)
# - N (test case 1, between 1 and 1000 (small data) or 10^18 (large data))
# - N (test case 2)
# - ...
#
# Output:
# - Case #1: y (last tidy num before N)
# - Case #2: y

# helper functions
def makeList(num):
    numStr = str(num)
    numLst = []
    for digit in numStr:
        numLst.append(int(digit))
    return numLst

def checkTidy(numLst):
    lastDigit = 0
    for digit in numLst:
        if digit < lastDigit:
            return False
        lastDigit = digit
    return True

def makeNewNum(numLst):
    if numLst[0] == 0:
        numLst = numLst[1:] # delete leading 0, if it's there
    return int(''.join(str(i) for i in numLst)) # convert numLst back to int

# used for small input sizes
# def getLastTidyNum(n):
#     lastTidyNum = 0
#     for j in xrange(n, 0, -1):
#         numLst = makeList(j)
#         if checkTidy(numLst):
#             lastTidyNum = j
#             break
#     return lastTidyNum

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

# main program
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
input = open("R1_PB_Input.txt", "r")
output = open("R1_PB_Output.txt","w")

t = int(input.readline())

for i in range(1, t + 1):
  n = int(input.readline())
  lastTidyNum = getLastTidyNum(n)
  output.write("Case #{}: {}\n".format(i, lastTidyNum))

output.close()
