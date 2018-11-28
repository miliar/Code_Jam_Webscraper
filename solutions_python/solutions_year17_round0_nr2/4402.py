#!/usr/bin/env python
import sys
import doctest
import fileinput
import math

def is_tidy(n):
  """
  Determines if a number is tidy
  Parameters
  ----------
  n: int
    Number
  res: bool
    True is tidy, False if not tidy
  Returns
  -------
  res: int
    Closest tidy number

  Doc Test
  ----------
  >>> is_tidy(0)
  True
  >>> is_tidy(6)
  True
  >>> is_tidy(10)
  False
  >>> is_tidy(26)
  True
  >>> is_tidy(53)
  False
  >>> is_tidy(366)
  True
  >>> is_tidy(112)
  True
  >>> is_tidy(132)
  False
  >>> is_tidy(1000)
  False
  >>> is_tidy(2220)
  False
  >>> is_tidy(11223344556678)
  True
  >>> is_tidy(11223344554)
  False
  """

  s = str(n)
  for i, c in enumerate(s):
    if i + 1 < len(s) and c > s[i + 1]:
      return False
  return True

def tidy(n):
  """
  Find the next tidy number
  Parameters
  ----------
  n: int
    Upper number
  res: int

  Returns
  -------
  res: int
    Closest tidy number

  Doc Test
  ----------
  >>> tidy(0)
  0
  >>> tidy(6)
  6
  >>> tidy(10)
  9
  >>> tidy(26)
  26
  >>> tidy(53)
  49
  >>> tidy(366)
  366
  >>> tidy(112)
  112
  >>> tidy(132)
  129
  >>> tidy(1000)
  999
  >>> tidy(2220)
  1999
  >>> tidy(12345678)
  12345678
  >>> tidy(123454)
  123449
  >>> tidy(111111111111111110)
  99999999999999999
  """
  if is_tidy(n):
    return n

  s = str(n)

  for i, c in enumerate(s):
    if i + 1 < len(s) and c >= s[i + 1]:
      return n - int(s[i + 1:]) - 1

if __name__ == "__main__":
  # Run the doc test
  doctest.testmod()

  # Read from stdin
  reader = fileinput.input()
  # Ignore the number of inputs
  next(reader)
  i = 1
  for line in reader:
    number = line.strip()
    ans = tidy(int(number))
    print 'Case #{}: {}'.format(i, ans)
    i +=1


