#! /usr/bin/env python

import numpy as np
import time


def is_palindrome(s):
  for i in range(0, (len(s)/2)+1):
    if s[i] != s[len(s)-i-1]:
      return False
  return True

#
# MAIN FUNCTION
#

# open input
with open('C-small-attempt1.in', 'r') as f:
  numberCases = f.readline().strip()

  for i in range(0, int(numberCases)):
    acc = 0
    [m, M] = [float(x) for x in f.readline().split()]
    n = long(np.ceil(np.sqrt(m)))
    N = long(np.floor(np.sqrt(M)))
    k = n
    while k < N+1:
      K = str(k)
      #if (K[0] == '1' or K[0] == '2'):
      if is_palindrome(K):
        sq = np.power(k, 2)
        if is_palindrome(str(sq)):
          acc += 1
      #else:
        #k = long('1' + '0'*len(K))
      k+=1
    print "Case #" + str(i+1) + ": " + str(acc)