#!/usr/bin/python

import string, sys

def count(needle, char_index, haystack, pos):   
   if char_index >= len(needle) - 1:
      return string.count(haystack, needle[char_index], pos)
   
   char = needle[char_index]
   
   sum = 0
   next_pos = string.find(haystack, char, pos)
   while (next_pos != -1):
      sum += count(needle, char_index + 1, haystack, next_pos + 1)
      
      next_pos = string.find(haystack, char, next_pos + 1)
      
   return sum

def case(haystack):
   needle = "welcome to code jam"
   
   return count(needle, 0, haystack, 0)

def main():
   f = open(sys.argv[1])
   f.readline()
	
   caseNum = 1
   for line in f:
      print "Case #%d: %04d" % (caseNum, case(line) % 10000)
      caseNum += 1

main()
