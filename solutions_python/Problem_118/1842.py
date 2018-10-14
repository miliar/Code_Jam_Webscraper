#!/usr/bin/env python
import sys
import math

def isPalindrome(n):
   x = str(n)
   return (x == x[::-1])
   
ncases = int(sys.stdin.readline().strip())

for i in xrange(1, ncases+1):
   count = 0;
   (a, b) = [int(x) for x in sys.stdin.readline().strip().split()]
   
   m = int(math.sqrt(a))
   n = int(math.sqrt(b))
   
   for j in xrange(m, n+1):
      if isPalindrome(j) and isPalindrome(j*j) and (j*j >= a):
         count += 1
         
   print("Case #%d: %d" % (i, count))
   
