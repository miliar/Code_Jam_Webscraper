#!/usr/bin/python

def solve():
   n = input()
   c = map(int, raw_input().split())

   sum = c[0]

   for i in range(1, n):	
      sum = sum ^ c[i]

   if sum != 0:
      return 'NO'

   c.sort()

   half = n / 2
   sum = 0

   for i in range(1, n):
      sum += c[i]

   return sum
          
for i in range(input()):
    print "Case #%d: %s" % (i+1, solve())
    
    
