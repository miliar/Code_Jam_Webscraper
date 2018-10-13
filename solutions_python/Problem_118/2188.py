import sys
from math import sqrt, floor

def is_square(n):
  return sqrt(n).is_integer()

def is_palindrome(n):
  s = str(int(n))
  return s == s[::-1]

def is_fair_and_square(n):
  return is_palindrome(n) and is_square(n) and is_palindrome(sqrt(n))

f = open(sys.argv[1])
o = open("out", 'w')
cases = int(f.readline())

for i in range(cases):
  low, high = [int(n) for n in f.readline().split()]
  result = 0
  for n in range(low, high+1):
    if is_fair_and_square(n):
      result += 1

  o.write("Case #%d: %s\n" % (i+1, result))