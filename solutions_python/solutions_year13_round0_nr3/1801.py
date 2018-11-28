#!/usr/bin/env python2
import sys
import io
import math

def main():
  s = sys.stdin.read().split()

  T = int(s[0])
  s = s[1:]
  MAX = 10**7
  fas = []
  for i in range(MAX):
    if ispal(i) and ispal(i**2):
      fas += [i**2]

  for i in range(T):
    lb = int(s[i * 2])
    ub = int(s[i * 2 + 1])
    count = 0
    start = 0
    while start < len(fas) and fas[start] < lb:
      start += 1

    end = start
    while end < len(fas) and fas[end] <= ub:
      count += 1
      end += 1

    if start < len(fas):
      print "Case #%d: %d" % (i + 1, count)
    else:
      print "Case #%d: 0" % (i + 1)

def ispal(num):
  num = str(num)
  if len(num) < 2:
    return True
  else:
    return num[0] == num[-1] and ispal(num[1:-1])


if __name__ == '__main__':
  main()
