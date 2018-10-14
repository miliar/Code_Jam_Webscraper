#!/usr/bin/python

import sys

def case(input, words):
   input = input.strip()
   
   sets = []
   set = []
   setFlag = []
   for c in input:
      if c == "(":
         setFlag = True
      elif c == ")":
         setFlag = False
         sets += [set]
         set = []
      elif setFlag:
         set += c
      else:
         sets += [c]
   
   count = 0
   for word in words:
      i = 0
      valid = True
      while i < len(word) and valid:
         if not word[i] in sets[i]:
            valid = False
         else:
            i += 1 
      
      if valid:
         count += 1
            
   return count

def main():
   f = open(sys.argv[1])
   
   wordLength, wordCount, cases = f.readline().split(' ')
   
   words = []
   for i in range(0, int(wordCount)):
      words += [f.readline().strip()]
    
   caseNum = 1
   for line in f:
      print "Case #%d: %s" % (caseNum, case(line, words))
      caseNum += 1

main()
