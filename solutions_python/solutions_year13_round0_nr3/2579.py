import os, sys, math

def isPalindrome(num):
  n = num
  rev = 0
  while num > 0:
    dig = num % 10
    rev = rev * 10 + dig
    num = num / 10
  if n == rev:
    return 1 
  return 0 

# Babylonian Algorithm for determining sqrt, to avoid floating point nonsense
def isSquare(num):
  if num == 0:
    return False
  if num == 1:
    return True
  x = num // 2
  seen = set([x])
  while x * x != num:
    x = (x + (num // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

f = open(sys.argv[1], 'r')
numCases = int(f.readline())


for i in range(numCases):
  counter = 0
  case = f.readline()
  targetRange = case.split(None)
  for j in range(int(targetRange[0]), int(targetRange[1])+1):
    if isPalindrome(j):
      if isSquare(j):
        if isPalindrome(int(math.sqrt(j))):
          counter += 1
  print "Case #%i: %i" % ((i+1), counter)

