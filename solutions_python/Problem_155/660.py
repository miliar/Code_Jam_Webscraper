#!/usr/bin/python3
import fileinput

f=fileinput.input()
T=int(f.readline())

out=0

for case in range(T):
  a,b=f.readline().split()
  Smx=int(a)
  count=0
  sm=0
  for i in range(Smx):
   sm+=int(b[i])
#   print(sm,end=" ")
   if sm<i+1:
    count+=1
    sm+=1
   
  
  print("Case #"+str(case+1)+":", count)

     