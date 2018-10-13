#!/usr/bin/python
import sys

inp = [l.strip() for l in sys.stdin if l.strip()!='']
T = int(inp[0])
l = 1
for t in range(T):
  line = inp[l].split(" ")
  N=int(line[0])
  pd=int(line[1])
  pg=int(line[2])
#  print (N,pd,pg)

  poss = True;
  if pd>0 and pg==0:
    poss = False
  elif pg==100 and pd<100:
    poss = False
  else:
    num = pd
    den = 100
    i=2
    while i<=50:
      if num%i==0 and den%i==0:
        num/=i
        den/=i
      else:
        i+=1
    if den>N:
      poss = False;
    else:
      pass # possible

  l += 1
  print "Case #%d: %s" % (t+1, "Possible" if poss else "Broken")

