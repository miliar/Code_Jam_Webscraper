import sys, re

def GCD(x, y):
 if x<0: x=-x
 if y<0: y=-y

 if x+y>0:
  g=y
  while x>0:
   g=x
   x=y%x
   y=g
  return g
 else:
  return 0


def my_gcd(c):
  last=c[0]
  for cis in c:
    last=GCD(last,cis);
  return last


N = sys.stdin.readline()

for i in range(0,int(N)):
  ev = sys.stdin.readline().split()
  ev = [int(e) for e in ev[1:len(ev)]]
  m = min(ev)
  ev = [e-m for e in ev]
  g = my_gcd(ev)
  res = (((m/g)+1)*g-m)
  if m%g==0:
    res = ((m/g)*g-m)
  print "Case #%d: %d" % (i+1,res)

