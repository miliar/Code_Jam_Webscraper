I,O=open('test.txt','rU'),open('output.txt','w')
W,R=O.write,I.readline

from itertools import combinations
from collections import Counter

def xor(s):
  try: return reduce((lambda x,y: x^y),s)
  except: return s
  
for main in range(int(R())):
  N,biggest = int(R()),0
  line = [int(i) for i in R().split(' ')]
  for i in range(1,N/2+1):
    for j in combinations(line,i):
      k=[]
      for i in (Counter(line)-Counter(j)).items():
        k+=[i[0]]*i[1]
      if xor(j)==xor(k):
        if sum(j)>biggest: biggest = sum(j)
        if sum(k)>biggest: biggest = sum(k)
  if not biggest: biggest = 'NO'
  W('Case #%d: %s\n'%(main+1,biggest))

I.close()
O.close()