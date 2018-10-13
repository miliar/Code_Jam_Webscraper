#!/usr/bin/python

import sys

def case(number):   
   symbols = set(number)
   
   base = len(symbols)
   if base == 1:
      base = 2
   
   number = list(number)
   
   decoded = {number[0]: 1}
   
   found = False
   i = 1
   while i < len(number) and not found:
      if not number[i] in decoded:
         decoded[number[i]] = 0
         found = True
      i += 1
   
   next = 2
   while i < len(number):
      if not number[i] in decoded:
         decoded[number[i]] = next
         next += 1
      i += 1
   
   number.reverse()
   exp = 0
   sum = 0
   for x in number:
      sum += decoded[x] * base ** exp
      exp += 1
   
   return sum
   

def main():
   f = open(sys.argv[1])
   f.readline()
	
   caseNum = 1
   for line in f:
      print "Case #%d: %s" % (caseNum, case(line.strip()))
      caseNum += 1

main()
