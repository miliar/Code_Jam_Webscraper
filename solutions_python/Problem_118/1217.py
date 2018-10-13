#!/usr/bin/env python
# Benjamin James Wright

import math

T = input()

for i in xrange(0, T):
   A, B = [int(e) for e in raw_input().split()]
   count = 0
   for j in xrange(A, B+1):
       l = str(j)
       # If it is a palindrome
       if l == l[::-1]:
           l_r = math.sqrt(j)
           # Approximation...
           if int(l_r + 0.5) ** 2 ==  j:
               l_r = str(int(l_r))
               if l_r == l_r[::-1]:
                   count += 1
   print "Case #" + str(i+1) + ": " + str(count)
