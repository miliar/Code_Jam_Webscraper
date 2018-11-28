import math
from math import *
print "hi"

def eval_sum( i,r ) :
  return  2*i*i + (2*r - 1)*i 

f1 = open('g1.dat','r')
s1 = f1.read()
f1.close()
r1 = s1.split('\n')
nt = int(r1[0])
print " "
print nt
s2 = ""
for ti in range(1,nt+1) :
  r2 = r1[ti].split()
  #print r2
  r = int(r2[0])
  t = int(r2[1])
  #print r, t,
  a1 = (-(2*r-1) + sqrt((2*r-1)*(2*r-1) + 8*t))/4.
  i1 = int(a1)

  #print i1, eval_sum(i1,r)
  if eval_sum(i1,r) > t :
    i1 -= 1
  elif eval_sum(i1+1,r) <= t :
    i1 += 1
  print i1
  
  s2 += "Case #" + str(ti) + ": " + str(i1) + "\n"
  
#print int(3.1), int(3.5), int(3.8)
f2 = open('o1.dat','w')
f2.write(s2)
f2.close()
