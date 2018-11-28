#!/usr/bin/python -tt

import sys

def calculate():
  filename='B-small-attempt0.in'
  f=open(filename,'rU')
  lines=[]
  lines=f.read()
  lines=lines.split()
  #print lines 
  for j in range(int(lines[0])):
    for s in lines[j+1].split(' '):
       if len(s)>1:
          n=long(s)
          while n:
               c=[]
               for digit in str(n):
                 c.append (int(digit))
               #print c
               if all(c[i] <= c[i+1] for i in xrange(len(c)-1)):
                   print 'Case #{}: {}'.format(j+1,''.join(str(v) for v in c))
                   break  
               n=n-1
       else :
           print 'Case #{}: {}'.format(j+1,int(s))


if __name__ == '__main__' :
   sys.stdout = open('smallinput1.out', 'a')
   calculate()
