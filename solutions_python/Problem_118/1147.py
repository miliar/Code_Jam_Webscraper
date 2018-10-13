#!/usr/bin/python
import sys
import math

def ispal(n):
  arr = []
  while (n > 0):
    arr.append(n % 10)
    n = n/10
  return arr == arr[::-1]

def findmagic(l, h):
  ll = int(math.sqrt(l-1))+1
  hh = int(math.sqrt(h))
  rlt = []
  i = ll
  while i <= hh:
    if ispal(i) and ispal(i*i):
      rlt.append(i*i)
    i = i+1
  return rlt

def main():
  T = int(sys.stdin.readline())
  for i in range(T):
    line = sys.stdin.readline().split(' ')
    low = int(line[0])
    high = int(line[1])
    #print low, high
    magics = findmagic(low, high)
    #print magics
    print 'Case #%d: %d' % (i+1, len(magics))

if __name__ == '__main__':
  main()
