import math
import sys
import re
ipf = open (sys.argv[1], 'r')
opf = open (sys.argv[2], 'w')
T = int (ipf.readline())
def lcm(a,b):
  return a*b/gcd(a,b)
def gcd(a,b):
  if max([a,b]) == 1:
    return 1
  m = max([a,b])
  n = min([a,b])
  if n == 0:
    return m
  if m%n == 0:
    return n
  return gcd(n,m%n)

for t in range (1,T+1):
  n,l,h = map(int,ipf.readline().split())
  notes = map(int,ipf.readline().split())
  
  for i in range(0,n-1):
    if i==0:
      lc = lcm(notes[i],notes[i+1])
      continue
    lc = lcm(lc,notes[i+1])
  print lc
  b = 1
  for i in range(l,h+1):
    for n in notes:
      if n%i != 0 and i%n !=0:
        b = 0
        break
      else:
        b = 1
    if b==1:
      no = i
      break
  if b == 0:
    opf.write("Case #%d: NO\n" % t)
  else:
    opf.write("Case #%d: %d\n" % (t,no))

ipf.close()
opf.close()
