import sys
from math import log

if (len(sys.argv) != 2):
  print "Require 1 input file as argument"
  exit(1)
  
inputFile = open(sys.argv[1])
outputFile = open("output.txt", 'w')
N = int(inputFile.readline())

def numDigits(n):
  return int(round(log(n)/log(10)+0.5))

def toInt(lst):
  sum = 0
  for i in range(len(lst)):
    sum += lst[len(lst)-i-1]*10**i
  return sum

def toList(n):
  lst = []
  while (n > 0):
    lst = [n % 10] + lst
    n /= 10
  return lst

for i in range(N):
  inputTXT = inputFile.readline()[:-1]
  outputTXT = ""
  
  # My code here...
  A, B = map(int, inputTXT.split(' '))
  count = 0
  checkedNums = set()
  for j in range(A, B+1):
    digitList = toList(j)
    for k in range(numDigits(j)-1): # If 2 digits then only rotate once, etc.
      digitList = digitList[1:] + [digitList[0]]
      newInt = toInt(digitList)
      if A <= newInt <= B and newInt > j and "%d, %d" % (j, newInt) not in checkedNums:
        count += 1
      checkedNums.add("%d, %d" % (j, newInt))
  outputTXT = str(count)

  outputFile.write("Case #%d: %s\n" % (i+1, outputTXT))
  print "Case #%d: %s" % (i+1, outputTXT)

inputFile.close()
outputFile.close()
