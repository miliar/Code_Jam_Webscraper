import sys
sys.setrecursionlimit(100000)
from itertools import combinations, permutations
from math import ceil,floor,factorial

def nchoosek(n,k):
  return factorial(n)/(factorial(n-k)*factorial(k))

def xorStrings(a,b):
  n = len(a)
  x = int(a,2)^int(b,2)
  x = bin(x)[2:]
  n2 = n-len(x)
  
  return '0'*n2 + x

def calcand(a,b):
  return a&b
      
def solve():
  #~ print a,b,k
  #~ print bin(a)
  #~ print bin(b)
  #~ print bin(calcand(a,b))
  #~ print calcand(a,b)
  
  #~ c=0
  #~ for i in range(a):
    #~ for j in range(b):
      #~ for m in range(k):
        #~ if calcand(i,j) == m:
          #~ c+=1
  #~ return c
  
  c=0
  for i in range(a):
    for j in range(b):
      if calcand(i,j) < k:
        c+=1
  return c
  
  #~ abin = bin(a)[2:]
  #~ bbin = bin(b)[2:]
  #~ 
  #~ nbits = max(len(abin),len(bbin))
  #~ 
  #~ print abin
  #~ print bbin
  #~ print nbits
  #~ print
  #~ c = 0
  #~ for m in range(k):
    #~ mb = bin(m)[2:]
    #~ c+= 2*nbits - mb.count('1')
  #~ return c
  
   

T = int(raw_input())

for case in range(T):
  
  a,b,k = map(int,raw_input().split());

  sol = str(solve())
  
  print 'Case #%d: %s' %(case+1,sol)
    
