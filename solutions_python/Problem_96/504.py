#!/usr/bin/python

import sys

def calculate(line):
  inp=line.split(" ")
  N=int(inp[0])
  S=int(inp[1])
  p=int(inp[2])
  
  minPoints=3*p-4
  if minPoints<p:
     minPoints=p
  surPoints=3*p-2  
  if surPoints<p:
     surPoints=p  

  counter=0
  surpriseCounter=0
  for n in range(3,N+3):
      result = int(inp[n])
      if result>=surPoints:
         counter+=1
      elif result>=minPoints and surpriseCounter<S:
         counter+=1
         surpriseCounter+=1
  
  return counter

if __name__ == "__main__":
    #findMapping("samples")
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        f = open(fn)
   
    count = int(f.readline())
    for c in range(count): 
        line=f.readline()
        print "Case #%d: %s" %(c+1,calculate(line))

