#!/usr/bin/python

import sys
import fractions

fp = open(sys.argv[1], 'r')

num_cases = int(fp.readline())

for i in range(0, num_cases):
   line = fp.readline()
   words = line.split()

   N, PD, PG = int(words[0]), int(words[1]), int(words[2])

   if PD == 0:
      if PG == 100:
         print "Case #" + str(i + 1) + ": Broken"
      else:
         print "Case #" + str(i + 1) + ": Possible"

   else:
      g = fractions.gcd(PD, 100)

      if N < 100 / g:
         print "Case #" + str(i + 1) + ": Broken"
      else:
         if (PG == 100 and PD < 100) or (PG == 0 and PD > 0):
            print "Case #" + str(i + 1) + ": Broken"
         else:
            print "Case #" + str(i + 1) + ": Possible"
