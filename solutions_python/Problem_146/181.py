import sys
sys.setrecursionlimit(100000)
from itertools import combinations, permutations
from math import ceil,floor,factorial

def nchoosek(n,k):
  return factorial(n)/(factorial(n-k)*factorial(k))

def permValid(p):
  charsFound = set()
  prev = ''
  for i in p:
    car = cars2[i]
    for c in car:
      if c in charsFound and not c==prev:
        return False
      prev = c
      charsFound.add(c)
  return True

def strips(s):
  snew = s[0]
  cs = [1]
  for i in range(1,len(s)):
    if not s[i] == snew[-1]:
      snew = snew + s[i]
      cs.append(0)
    cs[-1]+=1
  return snew 
      
def check():

  cars3 = [ strips(car) for car in cars]
  
  seFound = set()
  
  for car in cars3:
    
    lFound = set()
    prev = ''
    for i,l in enumerate(car):
      if l in lFound and not l==prev:
        #~ print car, i, l , prev, lFound
        return False
      if not i==0 and not i==len(car)-1 and l in seFound:
        #~ print car, i, l , seFound
        return False
      prev = l
      lFound.add(l)
    seFound.add(car[0])
    seFound.add(car[-1])
        
  return True
          
def solve():

  #~ print cars
  #~ print cars2

  if not check():
    return 0

  c = 0

  for p in permutations(range(N)):
    #~ print p , permValid(p)
    if permValid(p):
      c+=1
  
  return c

T = int(raw_input())

for case in range(T):
  
  N = int(raw_input());
  cars = raw_input().split()

  cars2 = []
  for c in cars:
    if len(c)>1:
      cars2.append(c[0]+c[-1])
    else:
      cars2.append(c[0])

  sol = solve()
  
  print 'Case #%d: %s' %(case+1,str(sol))
    
