#!/usr/bin/env python

import sys

def sean_add(a, b):
  a = bin(a)[2:][::-1]
  b = bin(b)[2:][::-1]

  sum = ''
  for i in xrange(0, min(len(a), len(b))):
    if (a[i] == '0' and b[i] == '1') \
        or (a[i] == '1' and b[i] == '0'):
      sum += '1'
    else:
      sum += '0'
  if len(a) > len(b):
    sum += a[len(b): ]
  elif len(b) > len(a):
    sum += b[len(a): ]
  return int('0b' + sum[::-1], 2)

def total_value(piece):
  value = 0
  for candy in piece:
    value = sean_add(value, candy)
  return value

def split_candy(num, candies, sean, patrick):
  if num == len(candies):
    return split_candy(num - 1, candies, sean + [int(candies[-num])], patrick)
  elif num > 0:
    value_1 = split_candy(num - 1, candies, sean + [int(candies[-num])], patrick)
    value_2 = split_candy(num - 1, candies, sean, patrick + [int(candies[-num])])
    return max(value_1, value_2)
  else:
    if (total_value(sean) == total_value(patrick)) \
        and (sum(sean) != 0) and (sum(patrick) != 0):
      real_value = max(sum(sean), sum(patrick))
      return real_value
    else:
      return -1

def main():
  filename = sys.argv[1]
  f = open(filename)

  testcase_num = int(f.readline())
  for i in xrange(0, testcase_num):
    candies_num = int(f.readline())
    candies = f.readline().strip().split()
    sean = []
    patrick = []
    value = split_candy(candies_num, candies, sean, patrick)
    if value == -1:
      print 'Case #' + str(i+1) + ': NO'
    else:
      print 'Case #' + str(i+1) + ': ' + str(value)

if __name__ == '__main__':
  main()
