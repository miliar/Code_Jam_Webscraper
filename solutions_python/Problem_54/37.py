#!/usr/bin/python
import fractions

fp = open('test.in')

lines = fp.readlines()
lines = lines[1:]

c = 1
for case in lines:
   case = case[:-1]
   elements = case.split(' ')
   elements = elements[1:]
   elements = [long(x) for x in elements]
   m = None
   for x in elements:
      for y in elements:
         if x != y:
            if m == None:
               m = abs(x-y)
            else:
               m = fractions.gcd(abs(x-y), m) 
   res = elements[0] % m
   if res != 0:
      y = m - res
      print "Case #%d: " % c + (y.__str__())
   else:
      print "Case #%d: 0" % c
   c = c + 1
