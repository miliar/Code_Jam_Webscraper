# Author Samvit Majumdar
from collections import deque

def check(l,u):
  c,p = 0,[]
  for n in range(l,u+1):
    d = deque(str(n))
    num = int(''.join(list(d)))
    #print 'For number : ',num
    for e in range(len(d)):
      d.rotate(1)
      #print int(''.join(list(d)))
      n = int(''.join(list(d)))
      if n>=l and n<=u and n>num and (num,n) not in p:
        c+=1
        p.append((num,n))
        #print num,n,c
  return c
f,o = open('inputc'),open('outputc','r+')
l = f.readlines()
a,j = int(l[0]),[]
for k in l[1:]: j.append(map(int,k.split()))
for x,m in zip(xrange(1,a+1),j):
  #print m[0],m[1]
  j =  'Case #%d: ' % (x,) + str(check(m[0],m[1]))
  o.write(j+'\n')
  print j