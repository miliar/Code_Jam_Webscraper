#!/usr/bin/python
import sys

def io():
  with open('input', 'r') as inf:
    with open('output','w') as of:
      lno = 0
      for l in inf:
        lno += 1 
        # Code begins here
        if lno > 1:
          if lno % 2 == 1:
            ls = l.split()
            lsi = [int(i) for i in ls]
            o = solve(lsi)
            if o != 0: 
              ol = "Case #%d: %d" % (lno / 2, o)
            else:
              ol = "Case #%d: NO" % (lno / 2,)
            of.write(str(ol) + '\n')

def getsl(l, ln):
  ret = []
  ret2 = []
  for i in range(2 ** ln):#small problem
    bi = bin(i)[-1:1:-1]
    tl = []
    tl2 = []
    for c in range(min(len(bi), ln)):
      if bi[c] == '1':
        tl.append(l[c])
      else:
        tl2.append(l[c])
    tl2.extend([l[j] for j in range(len(bi), ln)])
    ret2.append(tl2)
    ret.append(tl)
  return ret, ret2

def xsum(l):
  xs = l[0]
  for i in range(1,len(l)):
    xs ^= l[i] 
  return xs
  
def solve(l):
  sls1, sls2 = getsl(l, len(l))
  maxs = 0
  for i in range(len(sls1)):
    sp = sls1[i]
    pp = sls2[i]
    if len(sp) == 0 or len(pp) == 0:
      continue
    s = sum(sp)
    xss = xsum(sp)
    xsp = xsum(pp)
    if xss == xsp:
      if maxs < s:
        maxs = s
  return maxs
  

if __name__ == "__main__":
  io()



