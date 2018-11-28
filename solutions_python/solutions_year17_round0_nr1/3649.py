#!/usr/bin/env python
import sys
import doctest
import fileinput

def convert (string):
  """
  Replaces + with 1 and - with 0 in a string
  Parameters
  ----------
  arr : array
    Array of of booleans or 0's and 1's
  Returns
  -------
  arr : array
    Array of inverted values
  Doc Test
  ----------
  >>> convert('')
  []
  >>> convert('-')
  [0]
  >>> convert('+')
  [1]
  >>> convert('-+---')
  [0, 1, 0, 0, 0]
  """
  return map(lambda i: 1 if i == '+' else 0, string)

def invert (arr):
  """
  Inverts the values of boolean  array
  Parameters
  ----------
  arr : array
    Array of of booleans or 0's and 1's
  Returns
  -------
  arr : array
    Array of inverted values
  Doc Test
  ----------
  >>> invert([])
  []
  >>> invert([0])
  [1]
  >>> invert([1])
  [0]
  >>> invert([1, 0, 1, 1, 1])
  [0, 1, 0, 0, 0]
  """
  return map(lambda i: int(not i), arr)


def min_flips(row, k):
  """
  Inverts the values of boolean  array
  Parameters
  ----------
  row: array
    row of pancakes with 1 indicating "+" (happy side), 0 indicating "-" (blank side)
  k: int
  Returns
  -------
  min_flips: int
    Minimum number of flips needed
  Doc Test
  ----------
  >>> min_flips([0, 0, 0, 1, 0, 1, 1, 0], 3)
  3
  >>> min_flips([1, 1, 1, 1, 1], 4)
  0
  >>> min_flips([0, 1, 0, 1, 0], 4)
  -1
  """
  min_num = 0

  for i in xrange(len(row)):
    indx = len(row) - i
    if not row[indx - 1]:
      min_num += 1
      row[indx - k: indx] = invert(row[indx - k: indx])
      if k > indx:
        return -1

  return min_num

if __name__ == "__main__":
  # Run the doc test
  doctest.testmod()

  # Read from stdin
  reader = fileinput.input()
  #ignore the number of inputs
  next(reader)
  i = 1
  for line in reader:
    string, k = line.strip().split()
    ans = min_flips(convert(string), int(k))
    print 'Case #{}: {}'.format(i, ans if ans != -1 else 'IMPOSSIBLE')
    i +=1


