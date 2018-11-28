#!/usr/bin/env python
import math
import sys

with sys.stdin as fp:
  num_cases = int(fp.readline())

  for i in range(num_cases):
    A_s, B_s = fp.readline().strip().split(' ')
    A = int(A_s)
    B = int(B_s)
    num_digits = len(A_s)

    options = set()

    for digits_to_move in range(1, num_digits):
      shift_left = num_digits - digits_to_move
      for n in range(A, B - 1):
        n_s = str(n) # .....
        m_s = "%s%s" % (n_s[shift_left:], n_s[0:shift_left])
        m = int(m_s)

        if n < m and m <= B:
          #print "shifting %d chars of by %d gives %d" % (digits_to_move, n, m)
          options.add((n, m))

    print "Case #%d: %d" % (i + 1, len(options))
