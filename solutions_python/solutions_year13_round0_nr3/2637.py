import sys
from math import *

def IsSquare(num):
  if num == 1:
    return True
  x = num / 2
  seen = set([x])
  while x*x != num:
    x = (x + (num / x)) / 2
    if x in seen: 
      return False
    seen.add(x)
  return True

def IsPalindrome(num):
  strNum = str(num)
  for i in range(len(strNum)):
    if strNum[i] != strNum[len(strNum)-i-1]:
      return False
  return True

# Script
fptr = open(sys.argv[1], "r")
content = fptr.readlines()
numCases = int(content[0])
del content[0]

for case in range(numCases):
  a = int(content[0].split()[0])
  b = int(content[0].split()[1])
  del content[0]
  nums = 0
  for x in range(a, b+1):
    if IsPalindrome(x):
      if IsSquare(x):
        if IsPalindrome(int(sqrt(x))):
          nums += 1
  print 'Case #%d: %d' % (case+1, nums)

