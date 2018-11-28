import sys
from math import sqrt

def getnums(s):
  return [int(s) for s in s.split() if s.isdigit()]

def nextline():
  return sys.stdin.readline()

def palindrome(n):
  s = str(n)
  return s == s[::-1]

def fairandsquare(n):
  if not palindrome(n):
    return False
  rootn = sqrt(n)
  if not rootn.is_integer():
    return False
  if not palindrome(int(rootn)):
    return False
  return True

tests = int(nextline())
for test in range(1, tests+1):
  bottom, top = tuple(getnums(nextline()))
  num = 0
  for n in range(bottom, top+1):
    if fairandsquare(n):
      num += 1

  print "Case #{}: {}".format(test, num)
