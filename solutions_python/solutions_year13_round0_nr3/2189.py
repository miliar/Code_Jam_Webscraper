#!/usr/bin/python -O

import sys
import os
from math import sqrt

def is_square(n):
  if n == 1:
    return True
  x = n // 2
  seen = set([x])
  while x * x != n:
    x = (x + (n // x)) // 2
    if x in seen:
      return False
    seen.add(x)
  return True

def fairAndSquare(n):
  if is_square(n):
    return palindrome(str(n)) and palindrome(str(int(sqrt(n))))

def palindrome(p):
    return p == p[::-1]

def main(argv=None):

  if argv is None:
    argv = sys.argv

  try:
    f = open(sys.argv[1], 'r')
  except IndexError as e:
    print "Please specify an input file"
    return 127
  except IOError as e:
    print "Could not read file!"
    return 127

  n = int(f.readline())
  n_case = 1
  t = {}
  k = 0

  while n_case <= n:
    T = list(f.readline().rstrip(os.linesep).split())
    A = int(T[0])
    B = int(T[1])
    for j in range(A,B+1):
      if fairAndSquare(j):
        k += 1
    print "Case #" + str(n_case) + ': ' + str(k)
    n_case += 1
    k = 0
  f.close()
  return 0

if __name__ == "__main__":
    sys.exit(main())
