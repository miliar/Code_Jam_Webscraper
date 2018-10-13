#!/usr/bin/python

import sys
import math

def main():
  # Get T
  line = sys.stdin.readline()
  t = int(line.strip())

  x = 0
  for line in sys.stdin:
    # Get N
    col = line.split(' ')
    n = int(col[0])

    # Get Ri and Pi
    ri = []
    pi = []
    for i in range(n):
      ri.append(col[i * 2 + 1])
      pi.append(int(col[i * 2 + 2]))

    # Run
    oran = 1
    blue = 1
    oran_time = 0
    blue_time = 0
    y = 0
    for i in range(n):
      move_time = 0
      if ri[i] == 'O':
        move_time = math.fabs(pi[i] - oran) - oran_time
        if move_time < 0:
          move_time = 0
        oran_time = 0
        blue_time += move_time + 1
        oran = pi[i]
      elif ri[i] == 'B':
        move_time = math.fabs(pi[i] - blue) - blue_time
        if move_time < 0:
          move_time = 0
        oran_time += move_time + 1
        blue_time = 0
        blue = pi[i]
      y += move_time + 1

    print "Case #" + str(x + 1) + ": " + str(int(y))
    x += 1

if __name__ == '__main__':
  main()
