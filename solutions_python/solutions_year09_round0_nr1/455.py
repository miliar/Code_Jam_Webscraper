#!/usr/bin/python
# hfgr 2009, alien problem of codejam 2009


import re

words=[]

F = open('input-largo.txt')
lineas= F.readline()[:-1].split()
L = int(lineas[0])
D = int(lineas[1])
N = int(lineas[2])
for x in xrange(D):
   words.append(F.readline()[:-1])

for case in range(1,N+1):
   count=0
   test = F.readline()[:-1]
   test=test.replace("(","[").replace(")","]")
   p=re.compile(test)
   for a in words:
      if p.match(a): count+=1
   print "Case #"+str(case)+": "+str(count)
