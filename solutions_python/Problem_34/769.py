# -*- coding: utf-8 -*-
import re

f = open("A.in","r")

s1 = f.readline()
s2 = s1.split()
L=s2[0]
D=s2[1]
N=s2[2]
palabras = []

for i in range(int(D)):
  s1 = f.readline()
  palabras.append(s1[0:len(s1)-1])

for i in range(int(N)):
  s1= f.readline()
  p1= re.compile("\(")
  s3= p1.sub("[",s1)
  p1= re.compile("\)")
  s1= p1.sub("]",s3)
  s1=s1[0:len(s1)-1]
 
  p2= re.compile(s1)
  contador=0
  for j in palabras:
    if p2.match(j):
      contador+=1
  print "Case #"+str(i+1)+": "+str(contador)
    
    
  
  
  



