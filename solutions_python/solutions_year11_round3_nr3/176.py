#!/usr/bin/python2
from sys import stdin
#gcd,lcm from http://www.4dsolutions.net/cgi-bin/py2html.cgi?script=/ocn/python/primes.py

def gcd(a,b):
   """Return greatest common divisor using Euclid's Algorithm."""
   while b:      
	a, b = b, a % b
   return a

def lcm(a,b):
   """
   Return lowest common multiple."""
   return (a*b)/gcd(a,b)

def GCD(terms):
   "Return gcd of a list of numbers."
   return reduce(lambda a,b: gcd(a,b), terms)

def LCM(terms):
   "Return lcm of a list of numbers."   
   return reduce(lambda a,b: lcm(a,b), terms)

def factors(x):
  r=[]
  f=2
  while(x>1):
    if(x%f==0):
      if(f not in r):r.append(f)
      x/=f
    else: f+=1
  res=1
  for i in r: res*=i
  return res
# the function to calculate the LCM
def lcm(num1, num2):
    result = num1*num2/gcd(num1,num2)
    return result


C = int(stdin.readline())

for c in range(1,C+1):
  t = map(int,stdin.readline().split())
  f = map(int,stdin.readline().split())
  #l=1
  #r=factors(LCM(f))
  v=True
  for r in range(t[1],t[2]+1):
    v=True
    for o in f:
      if(r%o!=0 and o%r!=0):
        v=False
        break
    if(v==True): break
    #if(v==False): continue
  print "Case #%d:" %c,
  if(v==False): print "NO"
  else: print r
  
