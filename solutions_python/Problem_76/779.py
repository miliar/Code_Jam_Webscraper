#!/usr/bin/python

import sys

def main():
  # Get T
  line = sys.stdin.readline()
  t = int(line.strip())

  for x in range(t):
    # Get N
    line = sys.stdin.readline()
    n = int(line.strip())

    # Get Ci
    line = sys.stdin.readline()
    col = line.split(' ')
    ci = []
    for i in range(n):
      ci.append(int(col[i]))
    ci.sort()
    #print ci

    # Check
    chk = 0
    for i in range(n):
      chk = chk ^ ci[i]
    #print chk

    # 'NO' case
    if chk > 0:
      print "Case #" + str(x + 1) + ": NO"
    else:
      total = 0
      for i in range(1, n):
        total += ci[i]
      print "Case #" + str(x + 1) + ": " + str(total)

if __name__ == '__main__':
  main()
