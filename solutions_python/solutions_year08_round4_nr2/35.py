import math
import string
import decimal
import psyco

psyco.full()
def abs(n):
    if n>=0:
        return n
    return -n

def duearea(x1,x2,x3,y1,y2,y3):
    return abs((x1*(y3-y2)+x2*(y1-y3)+x3*(y2-y1)))

# inizio corpo

f=open("inputB.txt","r")
o=open("outputB.txt","w")

numcasi=int(f.readline())

i=1
while i<=numcasi:
  
  s=f.readline()
  m=string.split(s)
  N=int(m[0])
  M=int(m[1])
  A=long(m[2])
  merda=0;
  if(A>M*N):
      o.write("Case #%d: IMPOSSIBLE\n" % (i))
      i+=1
      print i
      continue;
      
  for e1 in range(N+1):
      if merda==1:
          break
      for d1 in range(M+1):
          if merda==1:
              break
          for e2 in range(N+1):
              if merda==1:
                  break
              for d2 in range(M+1):
                  if duearea(0,e1,e2,0,d1,d2)==A:
                              merda=1
                              o.write("Case #%d: %d %d %d %d %d %d\n" % (i,0,0,e1,d1,e2,d2))
                              break
  if(merda==1):
      i+=1;
      print i;
      continue;
  
  o.write("Case #%d: IMPOSSIBLE\n" % (i))
                              
  print i;  
  i+=1