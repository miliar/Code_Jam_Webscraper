#!usr/bin/python 
import math 
import time 

t0 = time.clock()
out = open('myfile','w')

with   open('input.txt') as f:

  cases =  int( f.readline())
  

  for c in range(1,cases+1):
    
    ans = 'YES'
    m, n  = [int(x) for x in f.readline().split()]
    if (m == 1) or (n == 1):
      out.write(  "Case #" + str(c) + ": " + str(ans) + "\n")
      for x in range(0,m):
        f.readline()
       
  
      continue
    want = []
    now =  [] # [[0 for x in range(n)] for y in range(m)] 
    for i in range(0,m):
      temp = [ int(x) for x in f.readline().split() ]
      want.append(temp) 
      
      highest = max(temp)
      now.append([highest for x in range(n)]  )
      
      
    wt = zip(*want) 
    nt = zip(*now)
     
    
    for w,n in zip(wt, nt):
      
      highest = max(w)
       
      n = [x if x <= highest else highest for x in n]
       
       
      if w != tuple(n):
        ans = 'NO'
        break     
     
     
    out.write(  "Case #" + str(c) + ": " + str(ans) + "\n")
    
out.close()
f.close()
print ( time.clock() - t0)