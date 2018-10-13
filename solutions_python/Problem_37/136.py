#!/usr/bin/python

import sys

def convert_to_base(num, base):
   digits = []
   
   remainder = 0
   while num > 0:
      remainder = num % base
      digits += [remainder]
      
      num /= base
   
   return digits

def test_happy(digits, prev, base):         
   sum = 0
   for digit in digits:
      sum += digit ** 2
      
   if sum in prev:
      return False
      
   prev += [sum]
   
   if sum == 1:
      return True
   else:
      next = convert_to_base(sum, base)
      return test_happy([int(x) for x in next], prev, base)

def case(input):
   bases = [int(x) for x in input.strip().split(" ")]
   
   num = 2
   done = False
   while not done:
      temp = True
      x = 0
      while temp and x < len(bases):
         if not test_happy(convert_to_base(num, bases[x]), [0], bases[x]):
            temp = False
         x += 1
         
      if temp == True:
         done = True
      
      if not done:
         num += 1
   
   return num

def main():
   f = open(sys.argv[1])
   f.readline()
	
   caseNum = 1
   for line in f:
      print "Case #%d: %s" % (caseNum, case(line))
      caseNum += 1

if __name__ == '__main__':
   main()
