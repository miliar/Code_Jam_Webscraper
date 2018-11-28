n = int(raw_input())

def isPalindrome(x):
  s = str(x)
  return s==s[::-1]

import math,itertools

for x in range(n):
  low,high = map(long,raw_input().split())
  c=0
  square = 1
  while square**2<low:
    square+=1
  while square**2<=high:
    if(isPalindrome(square) and isPalindrome(square**2)):
      c+=1
    square+=1
  print "Case #%s: %s" % (x+1,c)

