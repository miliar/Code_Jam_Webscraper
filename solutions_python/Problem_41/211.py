#!/usr/bin/python

import sys
import itertools

if not sys.argv[1] :
   exit('I need a file')
F = open(sys.argv[1])
cases= F.readline()[:-1]
for case in range(int(cases)):
   numero=F.readline()[:-1]
   numero2=list(itertools.permutations(numero,len(numero)))
   numero4=[]
   for b in numero2:
     numero4.append(int(''.join(b)))
   #numero4=[]
   #numero4.extend( set(numero3))
   numero4.append(int(numero))
   numero4.sort()
   numero4.reverse()
   numero5=numero4[-1]
   for bb in numero4:
      if bb<=int(numero): break 
      numero5=bb
   while numero5<=int(numero):
   
     tt=str(numero5)
     ttd=[]
     ttd.append(tt[0])
     ttd.append('0')
     ttd.append(tt[1:])
     numero5=int(''.join(ttd))
  
   print 'Case #'+str(case+1)+':',numero5
