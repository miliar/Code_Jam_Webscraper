#!/usr/bin/env python

import sys

def main():
  T = int(sys.stdin.readline())
  for test in range(1, T + 1):
    line = sys.stdin.readline().split()
    N, Bt, Bp = int(line[0]), line[1::2], map(int, line[2::2])

    # robot = [pozitie, timp]
    orange = [1, 0]
    blue =   [1, 0]

    TIME = 0
    for i in range(N):
      # Asteapta robotul sa ajunga aici
      if Bt[i] == 'O':
        TIME = max(TIME, orange[1] + abs(Bp[i] - orange[0]))
      else:
        TIME = max(TIME, blue[1]   + abs(Bp[i] - blue[0]  ))
      
      # Apasa
      TIME += 1
      # Updateaza starea
      if Bt[i] == 'O':
        orange = [Bp[i], TIME]
      else:
        blue   = [Bp[i], TIME]

    print "Case #%d: %d" % (test, TIME)

  return 0

if __name__ == "__main__":
  main()

