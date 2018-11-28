#!/usr/bin/env python
import math

def ispalindrome(x):
  i = 0
  j = len(x) - 1
  while True:
    if i >= j:
      break
    if x[i] != x[j]:
      return False
    i = i + 1
    j = j - 1
  return True
  
def fairsquare(A,B):
  a = long(math.ceil(math.sqrt(A)))
  b = long(math.floor(math.sqrt(B)))
  s = 0L
  for i in range(a, b + 1):
    x = "%d" % i
    if ispalindrome(x):
      x = "%d" % (i * i) # suppress scientific notation
      t = ispalindrome(x)
      #print x,t
      if t:
        s = s + 1
  return s
      
def main():
  cases = int(raw_input())
  for case in range(cases):
    case = case + 1
    tups = raw_input().split()
    A = long(tups[0])
    B = long(tups[1])
    print "Case #%d: %d" % (case, fairsquare(A,B))

main()
