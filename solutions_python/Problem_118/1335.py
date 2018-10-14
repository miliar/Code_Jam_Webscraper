T = input()
from math import ceil,floor

def pld(s):
 s=str(s)
 if(s==s[::-1]):
  return 1
 return 0
 
def do():
 global a,b,nub
 a,b=int(ceil(a**0.5)),int(floor(b**0.5))
 
 i=a
 while i<=b:
  if pld(i) and pld(i*i):
   #print i
   nub+=1
  i+=1
 return nub   
   
for _ in range(T):
 a,b = map(int,raw_input().split())
 nub=0
 print "Case #"+str(_+1)+":",do()