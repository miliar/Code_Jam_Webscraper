#!/usr/bin/python

def solve(x):
   for i in xrange(x, 0, -1):
      y = str(i)
      l = len(y)
      f = True
      for j in xrange(1, l):
         if(int(y[j]) < int(y[j - 1])):
            f = False
            break
      if(f):
         return i
   assert(False)

n = input()
for i in xrange(1, n + 1):
   print "Case #%d: %d" % (i, solve(input()))