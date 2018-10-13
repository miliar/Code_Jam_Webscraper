#!/usr/bin/python

import sys
from itertools import izip_longest


def main(argc, argv):
  ifile = open(argv[1], 'r')

  case = 0
  ifile.readline()

  for line1, line2 in izip_longest(*[ifile]*2):
    case += 1

    R, k, N = map(int, line1.split())
    g = map(int, line2.split())

    money = 0

    load = 0
    runs = 0
    on_board = []

    while runs < R:
      try:
        cg = g.pop(0)
      except IndexError:
        cg = 0

      if cg == 0 or load+cg > k:
        money += load
        runs += 1
        load = 0
        g.extend(on_board)
        on_board = []

      if cg > 0:
        load += cg
        on_board.append(cg)

    print 'Case #' + str(case) + ': ' + str(money)


if __name__ == "__main__":
  main(len(sys.argv), sys.argv)

