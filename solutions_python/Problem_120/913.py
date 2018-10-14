#!usr/bin/python 
import math 
import time 

t0 = time.clock()
out = open('myfile','w')
total = {}
with   open('inp.txt') as f:
  cases =  int( f.readline())
   
  for case in range(1,cases+1):
     
    
    rad, t = [int(x) for x in f.readline().split() ]
     
    a = 2
    b =  2 * rad - 1
    c =   t * (-1) 
    d = b**2-4*a*c # discriminant
    x = (-b + math.sqrt(d)) / (2 * a)
    x = math.floor(x)
    out.write(  "Case #" + str(case) + ": " + str(int(x)) + "\n")
    
out.close()
f.close()
print ( time.clock() - t0) 
      
     
   