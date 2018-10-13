#!/usr/bin/python

t=input()
for i in xrange(t):
  z=raw_input().strip()
  z=[int(x) for x in z]
  if len(z)>1:
    for j in xrange(1,len(z)):
      if z[j]<z[j-1]:
        z[j-1]-=1
        k=j-2
        while k>=0 and z[k]>z[k+1]:
          z[k]-=1
          z[k+1]=9
          k-=1
        for k in xrange(j,len(z)):
          z[k]=9
        break
  if z[0]==0:
    del z[0]
  print "Case #"+str(i+1)+": "+"".join((str(x) for x in z))
