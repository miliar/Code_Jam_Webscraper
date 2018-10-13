from math import *
f=open("/tmp/A-large.in",'r')   

o=open("out.txt",'w')
T=int(f.readline())


for t in range(T):
 # print t
  l = f.readline().rsplit()
  N = int(l[0])
  K = int(l[1])
  
  o.write("Case #%d: " %(t+1))
  x = pow(2,N)
  if K%x == x-1:
    o.write("ON\n")
  else :
    o.write("OFF\n")
  
