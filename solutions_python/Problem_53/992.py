#!/usr/bin/python

import sys

def main():
   numCases = sys.stdin.readline()
   numCases = int(numCases)
   cases = []

   for i in range(0, numCases):
      case = sys.stdin.readline()
      case = case.split(' ')
      
      cases.append((int(case[0]), int(case[1])))


   for i in range(0, numCases):
      result = processCase(cases[i])
      print "Case #" + str(i+1) + ": " + result


def processCase(case):
   (numSnappers, snaps) = case
   
   snappers = [False] * numSnappers
   
   for s in range(0, snaps):
      onSoFar = True
      
      i = 0
      while onSoFar and i < numSnappers:
         if(snappers[i] == False):
            onSoFar = False
         
         snappers[i] = not snappers[i]
         i += 1
   
   #print snappers
   
   i = 0
   onSoFar = True
   while onSoFar and i < numSnappers:
      if(snappers[i] == False):
         onSoFar = False
      i += 1
   
   if onSoFar:
      return "ON"
   else:
      return "OFF"
      
   


main()