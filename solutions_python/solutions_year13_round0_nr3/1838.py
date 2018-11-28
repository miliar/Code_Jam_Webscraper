from math import sqrt, ceil, floor
import numpy as np

debug = False

def isPalindrome(num):
  s = str(num)
  for i in range(len(s) / 2):
    if s[i] != s[len(s) - 1 - i]:
      return False
  return True


def fairAndSquare():
  T = int(raw_input())
  for case in range(T):
    if debug: print "\nfairAndSquare(): Case #{}".format(case + 1)
    line = raw_input()
    A, B = tuple(int(x) for x in line.split())
    if debug: print "fairAndSquare(): A = {}, B = {}".format(A, B)
    
    a = int(ceil(sqrt(A)))
    b = int(floor(sqrt(B)))
    if debug: print "fairAndSquare(): a = {}, b = {}".format(a, b)
    
    count = 0
    for x in range(a, b + 1):
      if isPalindrome(x) and isPalindrome(x*x):
        count += 1
        if debug: print "fairAndSquare(): [LOOP] x = {}, x^2 = {}".format(x, x*x)
    
    print "Case #{}: {}".format(case + 1, count)


if __name__ == "__main__":
  fairAndSquare()
