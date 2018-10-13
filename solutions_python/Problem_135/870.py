#!/usr/bin/python

tests = int( raw_input() )

for j in range(1, tests + 1):
   r1 = [ [] for i in range(0, 4) ]
   r2 = [ [] for i in range(0, 4) ]

   a1 = int( raw_input() )
   for i in range(0, 4):
      r1[i] = map( int, raw_input().split(' ') )

   a2 = int( raw_input() )
   for i in range(0, 4):
      r2[i] = map( int, raw_input().split(' ') )

   s = set(r1[a1 - 1]).intersection(set(r2[a2 - 1]))

   if len(s) == 1:
      print "Case #{0}: {1}".format(j, list(s)[0])
   elif len(s) == 0:
      print "Case #{0}: Volunteer cheated!".format(j)
   else:
      print "Case #{0}: Bad magician!".format(j)
