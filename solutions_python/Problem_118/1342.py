#!/usr/bin/python2.7
import sys
import math

def isPoly(num):
  buff = str(num)
  size = len(buff)
  for i in xrange(0, size / 2):
    if buff[i] != buff[size - i - 1]:
      return False
  return True

def process(nums):
  A = nums[0]
  B = nums[1]
  low = int(math.ceil(math.sqrt(A)))
  up = int(math.floor(math.sqrt(B)))
  count = 0
  for i in xrange(low, up + 1):
    if isPoly(i) and isPoly(i * i):
      count = count + 1
  return str(count)

f = open(sys.argv[1])
N = int(f.readline())

for i in xrange(1, N + 1):
  print "Case #" + str(i) + ": " + process(map(lambda str: int(str), f.readline().split()))
