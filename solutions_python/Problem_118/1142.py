#!usr/bin/python 
import math

out = open('myfile','w')

with   open('input.txt') as f:

  cases =  int( f.readline())
  

  for c in range(1,cases+1):
    ans = 0
    start, finish  = [int(x) for x in f.readline().split()]
    low  = int(math.ceil( math.sqrt(start)))
    high = int(math.floor( math.sqrt(finish)))
    for i in range(low, high+1):
      st = str(i)
      rev = st[::-1]
      if st == rev:
        
        s = str(i * i)
        r = s[::-1]
        if s == r:
             
            ans = ans + 1
          
    
    out.write(  "Case #" + str(c) + ": " + str(ans) + "\n")
 
out.close()
f.close()