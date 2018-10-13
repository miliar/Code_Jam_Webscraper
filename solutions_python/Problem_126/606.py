#!/usr/bin/python

import sys
import math

if __name__ == '__main__':
  
  filename = sys.argv[1];
  
  with open(filename) as f:
    n = int(f.readline())
    for i in range(0,n):
      name,m = f.readline().split()
      m = int(m)
      
      numberOfCons = 0
      substrings = 0
      wordLength = len(name)
      for j in range(wordLength-1,m-2,-1):
        k = j
        numberOfCons = 0
        while k >= 0:
          if name[k] not in "aeiuo":
            numberOfCons += 1
            #print numberOfCons, name[k], substrings
            if numberOfCons == m:
              substrings += (k+1)
              numberOfCons = 0
              break
          else:
            numberOfCons = 0
            #print numberOfCons, name[k], substrings
            #if m > k: break
            
          k -= 1  
          
      print "Case #%d: %s" % (i + 1, substrings)