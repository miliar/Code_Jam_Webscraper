#from time import clock
from math import log
def recycle(a, n, b, t):
  #x=str(n)
  c = 0
  fs=set()
  for i in range(1, t):
    #f = int(x[i:]+x[:i])
    f = n/(10**i) + n%(10**i)*(10**(t-i))
    if a <= n < f <= b and f not in fs:
        fs.add(f)
        c += 1
  return c
  
def recycles(a, b):
  #start=clock()
  t = int(log(a,10))+1
  c = 0
  for i in range(a,b+1):
    c += recycle(a,i,b, t)
  #print clock()-start
  return c
  
t = int(raw_input())
for i in range(t):
  a,b = map(int, raw_input().split())
  print "Case #%d: %s" % (i+1, recycles(a,b))
