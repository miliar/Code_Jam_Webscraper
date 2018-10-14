import math
from copy import copy

def most_bit(num):
  return int(math.floor(math.log(num,2)))

def sumf(a,b):
  return a+b

def xor(a,b):
  return a^b
def toInt(c):
  return int(c)
input  = open('../input/Q_2011_d.in')
CASES  = int(input.readline())
for case in range(CASES):
  input.readline()
  list = map(toInt,input.readline().split(' '))
#retirar elementos ja ordenados nas extremidades
  limit=0
  iMax=max(list)
  iMin=min(list)
  listCop = [a for a in list]
  listCop.sort()
  toRemove=[]
  for i in range(len(list)):
    if list[i]==listCop[i]:
      toRemove.append(i)
  lenRemove=len(toRemove)
  print 'Case #'+str(case+1)+': %.6f'%(len(list)-lenRemove)
  